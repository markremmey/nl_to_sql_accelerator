import argparse
import os
from dotenv import load_dotenv
import re
from time import perf_counter

import numpy as np
import pandas as pd
import psycopg2
from constants import (
    DB_HOST,
    DB_NAME,
    DB_PORT,
    DB_USER,
    EMBEDDINGS_ENGINE,
    RESOURCE_ENDPOINT,
    GPT4_ENGINE_32k,
)
from src.data.golden_records import golden_records
from openai import AzureOpenAI
from src.utils.prompt_utils import (
    generate_nl_to_sql_system_prompt,
    generate_nl_to_sql_user_prompt,
    generate_sql_to_nl_system_prompt,
    generate_sql_to_nl_user_prompt,
    make_message_system,
    make_message_user,
)
import pyodbc
from retry import retry
from src.utils.database import run_query
from src.utils.metrics import calculate_cosine

# TODO: Add retry
# TODO: Consider reformatting the schema to lower token count and make it more readable
# TODO: What happens with really long sql execution results?
# TODO: Consider using non GT document

load_dotenv()
API_KEY = os.getenv("AOAI_API_KEY")
DB_PASSWORD = os.getenv("DB_PASSWORD")
SKIP_INVALID_GROUND_TRUTH = True


connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={DB_HOST},{DB_PORT};DATABASE={DB_NAME};UID={DB_USER};PWD={DB_PASSWORD}"

# Connect to the SQL Server database
try:
    DB_CONNECTION = pyodbc.connect(connection_string, timeout=30)
    print("Database connection established.")
except Exception as e:
    print(f"An error occurred while connecting to the database: {e}")
    DB_CONNECTION = None


def set_up_client():
    client = AzureOpenAI(
        azure_endpoint=RESOURCE_ENDPOINT,
        api_key=API_KEY,
        api_version="2024-05-01-preview",
    )
    return client

@retry(delay=1, backoff=1.1, tries=5)
def get_embeddings(client, text, model=EMBEDDINGS_ENGINE):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding


def generate_output_df(top_k):
    column_names = [f"top_{num}" for num in range(top_k)]
    return pd.DataFrame(columns=column_names)


def get_top_k_most_similar_examples(
    client, query, embeddings_db, top_k, filter_exact_match=True
):

    embeddings_df = embeddings_db.copy()
    query_embedding = get_embeddings(client, query, EMBEDDINGS_ENGINE)

    embeddings_df["cosine_similarities"] = embeddings_df.question_embeddings.apply(
        lambda x: calculate_cosine(list(x), query_embedding)
    )

    if filter_exact_match:
        embeddings_df = embeddings_df[embeddings_df["question"] != query]
    top_k_most_similar = (
        embeddings_df.sort_values(
            "cosine_similarities", ascending=False, ignore_index=True
        )
        .head(top_k)
        .reset_index(drop=True)
    )

    return top_k_most_similar


def format_examples(df):

    context = [
        f"Question: {q}\nMicrosoft SQL Server Query: {sql}\n\n"
        for q, sql in zip(df["question"], df["sql_query"])
    ]
    return "".join(context)


def remove_sql_markers(sql_string):
    pattern = r"^```sql\n|(?:\n```)(.*)$"
    return re.sub(
        pattern,
        lambda m: "--" + m.group(1) if m.group(1) else "",
        sql_string,
        flags=re.MULTILINE | re.DOTALL,
    )


def call_gpt(client, system_prompt, user_prompt, engine):
    completion_response = client.chat.completions.create(
        model=engine,
        messages=[make_message_system(system_prompt), make_message_user(user_prompt)],
        temperature=0,
    )
    return completion_response.choices[0].message.content


def find_ground_truth_if_it_exists(query):
    return next(
        (
            record["sql_query"]
            for record in golden_records
            if record["question"] == query
        ),
        None,
    )


def run_nl_to_sql(
    input_query,
    client,
    embeddings_db,
    top_k,
    schema,
    previous_try=None,
    retry_error=None,
):
    examples = get_top_k_most_similar_examples(
        client, input_query, embeddings_db, top_k
    )
    print(f"\033[92m{input_query}\033[0m")
    print(f"Found top {top_k} most similar questions:")
    print(examples["question"].values)

    nl_to_sql_system_prompt = generate_nl_to_sql_system_prompt(
        schema, format_examples(examples)
    )

    nl_to_sql_user_prompt = generate_nl_to_sql_user_prompt(input_query)

    if retry_error and previous_try:
        nl_to_sql_user_prompt = f"{nl_to_sql_user_prompt}\n\nYou already tried once with:\n{previous_try}It failed with: {retry_error}\n\n"

    print("nl_to_sql_system_prompt", nl_to_sql_system_prompt)
    print("nl_to_sql_user_prompt", nl_to_sql_user_prompt)
    tic = perf_counter()
    sql_completion = call_gpt(
        client, nl_to_sql_system_prompt, nl_to_sql_user_prompt, GPT4_ENGINE_32k
    )

    sql_to_nl_execution_time = perf_counter() - tic

    sql_completion = remove_sql_markers(sql_completion)
    print("GPT-4 SQL response:")
    print(f"\033[94m{sql_completion}\033[0m")
    print(f"\033[91mNL-to-SQL execution time: {sql_to_nl_execution_time}\033[0m")

    return sql_completion, sql_to_nl_execution_time


def run_sql_to_nl(input_query, client, sql_completion):
    # Step 2: SQL->NL
    sql_to_nl_system_prompt = generate_sql_to_nl_system_prompt()
    sql_execution_result = run_query(sql_completion, DB_CONNECTION)
    print(f"\033[94m{sql_execution_result}\033[0m")
    sql_to_nl_user_prompt = generate_sql_to_nl_user_prompt(
        input_query, sql_completion, sql_execution_result
    )

    tic = perf_counter()
    try:
        nl_to_sql_completion = call_gpt(
            client, sql_to_nl_system_prompt, sql_to_nl_user_prompt, GPT4_ENGINE_32k
        )
        nl_to_sql_execution_time = perf_counter() - tic
    # TODO catch only token exception from openai
    except Exception as e:
        nl_to_sql_completion = f"Error: {e}"
        nl_to_sql_execution_time = np.nan

    print(f"SQL-to-NL response:")
    print(f"\033[94m{nl_to_sql_completion}\033[0m")
    print(f"\033[91mSQL-to-NL execution time: {nl_to_sql_execution_time}\033[0m")

    return nl_to_sql_completion, nl_to_sql_execution_time, sql_execution_result

# Create a fun


def run_end_to_end(
    query_csv_path, embeddings_db, top_k, client, output_file_path, schema_desc_path
):

    nl_to_sql_completions = []
    nl_to_sql_execution_times = []
    ground_truths = []
    ground_truth_validities = []
    sql_to_nl_completions = []
    ground_truth_sql_to_nl_completions = []
    sql_to_nl_execution_times = []
    sql_execution_results = []
    ground_truth_sql_execution_results = []
    retries = []

    schema = open(schema_desc_path, "r").read()
    # print(f"Schema description:\n{schema}")
    query_df = pd.read_csv(query_csv_path)
    for input_query in query_df["question"]:
        retry_counter = 0
        # ground_truth = find_ground_truth_if_it_exists(input_query)
        # if ground_truth:
        #     print("Ground Truth SQL:")
        #     print(f"\033[94m{ground_truth}\033[0m")
        # else:
        #     print("No ground truth found")
        # ground_truth_is_invalid = "Error" not in run_query(ground_truth, DB_CONNECTION)

        # Step 1: NL->SQL
        sql_completion, nl_to_sql_execution_time = run_nl_to_sql(
            input_query, client, embeddings_db, top_k, schema
        )
        print(f"SQL completion: {sql_completion}")
        # Step 2: SQL->NL
        (
            sql_to_nl_completion,
            sql_to_nl_execution_time,
            sql_execution_result,
        ) = run_sql_to_nl(input_query, client, sql_completion)
        print(
            f"\033[91mTotal execution time: {sql_to_nl_execution_time + nl_to_sql_execution_time}\033[0m"
        )
        # Single retry flow
        if "error" in str(sql_execution_result).lower():
            retry_counter += 1
            print(f"Error in SQL execution: {sql_execution_result}")
            print(f"Retrying with previous try")
            # Step 1: NL->SQL
            sql_completion, nl_to_sql_execution_retry_time = run_nl_to_sql(
                input_query,
                client,
                embeddings_db,
                top_k,
                schema,
                previous_try=sql_completion,
                retry_error=sql_execution_result,
            )
            # Step 2: SQL->NL
            (
                sql_to_nl_completion,
                sql_to_nl_retry_execution_time,
                sql_execution_result,
            ) = run_sql_to_nl(input_query, client, sql_completion)
            sql_to_nl_execution_time += sql_to_nl_retry_execution_time
            nl_to_sql_execution_time += nl_to_sql_execution_retry_time
        if 'error' in str(sql_to_nl_completion).lower():
            retry_counter += 1
            
            # Modify sql_execution_result to illustrate how long the output was
            sql_execution_result = f"SQL execution produced too may rows, which caused a downstream failure: {len(sql_execution_result)} characters\nAbbreviated execution results: {sql_execution_result[:100]} ... {sql_execution_result[-100:]}"
            
            print(sql_execution_result)
            print(f"Retrying with previous try")
            # Step 1: NL->SQL
            sql_completion, nl_to_sql_execution_retry_time = run_nl_to_sql(
                input_query,
                client,
                embeddings_db,
                top_k,
                schema,
                previous_try=sql_completion,
                retry_error=sql_execution_result,
            )
            # Step 2: SQL->NL
            (
                sql_to_nl_completion,
                sql_to_nl_retry_execution_time,
                sql_execution_result,
            ) = run_sql_to_nl(input_query, client, sql_completion)
            sql_to_nl_execution_time += sql_to_nl_retry_execution_time
            nl_to_sql_execution_time += nl_to_sql_execution_retry_time
            
        # Runs SQL to NL with ground truth
        # (
        #     ground_truth_sql_to_nl_completion,
        #     ground_truth_sql_to_nl_execution_time,
        #     ground_truth_sql_execution_result,
        # ) = run_sql_to_nl(input_query, client, ground_truth)
        
       
        
        print(
            f"\033[91mTotal execution time: {sql_to_nl_execution_time + nl_to_sql_execution_time}\033[0m"
        )

        nl_to_sql_completions.append(sql_completion)
        nl_to_sql_execution_times.append(nl_to_sql_execution_time)
        # ground_truths.append(ground_truth if ground_truth else "Not Found")
        # ground_truth_validities.append(ground_truth_is_invalid)
        sql_to_nl_completions.append(sql_to_nl_completion)
        sql_to_nl_execution_times.append(sql_to_nl_execution_time)
        sql_execution_results.append(str(sql_execution_result))
        # ground_truth_sql_to_nl_completions.append(ground_truth_sql_to_nl_completion)
        # ground_truth_sql_execution_results.append(
        #     str(ground_truth_sql_execution_result)
        # )
        retries.append(retry_counter)

    nl_to_sql_completion_df = pd.DataFrame(nl_to_sql_completions, columns=["SQL Query"])
    # ground_truth_df = pd.DataFrame(ground_truths, columns=["ground_truth"])
    nl_to_sql_execution_time_df = pd.DataFrame(
        nl_to_sql_execution_times, columns=["nl_to_sql_execution_time"]
    )
    ground_truth_validity_df = pd.DataFrame(
        ground_truth_validities, columns=["ground_truth_validity"]
    )
    sql_to_nl_completion_df = pd.DataFrame(
        sql_to_nl_completions, columns=["SQL-to-NL response"]
    )
    sql_to_nl_execution_time_df = pd.DataFrame(
        sql_to_nl_execution_times, columns=["sql_to_nl_execution_time"]
    )
    sql_execution_results_df = pd.DataFrame(
        sql_execution_results, columns=["SQL Query Results"]
    )
    ground_truth_sql_to_nl_completion_df = pd.DataFrame(
        ground_truth_sql_to_nl_completions, columns=["Ground Truth SQL-to-NL response"]
    )
    ground_truth_sql_execution_results_df = pd.DataFrame(
        ground_truth_sql_execution_results,
        columns=["Ground Truth SQL Execution Results"],
    )
    retry_df = pd.DataFrame(retries, columns=["retries"]) 
     
    result = pd.concat(
        [
            query_df,
            nl_to_sql_completion_df,
            # ground_truth_df,
            nl_to_sql_execution_time_df,
            ground_truth_validity_df,
            sql_to_nl_completion_df,
            sql_to_nl_execution_time_df,
            sql_execution_results_df,
            ground_truth_sql_to_nl_completion_df,
            ground_truth_sql_execution_results_df,
            retry_df
        ],
        axis=1,
    )
    result.to_csv(output_file_path, index=False)
    print(f"Results written to {output_file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Find top_k most similar sql queries items given a query"
    )
    parser.add_argument(
        "--embeddings_database_path",
        type=str,
        required=True,
        help="Path to embeddings database generated from generate_embeddings.py",
    )
    parser.add_argument(
        "--query_csv_path", type=str, required=True, help="input query csv"
    )
    parser.add_argument(
        "--top_k",
        type=int,
        required=True,
        help="how many top similar results to be recorded",
    )
    parser.add_argument(
        "--output_file_path", type=str, required=True, help="output file path"
    )
    parser.add_argument(
        "--schema_desc_path", type=str, required=True, help="schema description path"
    )

    args = parser.parse_args()
    client = set_up_client()
    embeddings_db = pd.read_pickle(args.embeddings_database_path)
    run_end_to_end(
        args.query_csv_path,
        embeddings_db,
        args.top_k,
        client,
        args.output_file_path,
        args.schema_desc_path,
    )
