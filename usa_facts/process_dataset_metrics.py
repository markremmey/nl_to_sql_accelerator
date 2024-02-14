import argparse
import os

import pandas as pd
import psycopg2
from constants import RESOURCE_ENDPOINT
from openai import AzureOpenAI
from tqdm.auto import tqdm
from utils.metrics import (
    end_to_end_groundedness,
    end_to_end_relevance,
    evaluate_similarity,
    gpt_sql_critic_score,
    is_sql_execution_empty,
)

tqdm.pandas()

API_KEY = os.getenv("AOAI_API_KEY")
DB_PASSWORD = os.getenv("DB_PASSWORD")
METRICS_OUTPUT_DIRECTORY = "metrics"
METRICS_LIST = [
    "nl_to_sql_execution_time",
    "sql_to_nl_execution_time",
    "SQL Execution Exact Match",
    "SQL Query Execution Validity",
    "SQL Query Critic Score",
    "SQL Execution Is Empty",
    "Ground Truth SQL Executed vs Generated SQL cosine similarity",
    "Ground Truth SQL Execution Is Empty",
    "SQL Query Exact Match",
    "E2E Groundedness",
    "E2E Relevance",
    "retries",
]


def set_up_client():
    client = AzureOpenAI(
        azure_endpoint=RESOURCE_ENDPOINT,
        api_key=API_KEY,
        api_version="2023-07-01-preview",
    )
    return client


def save_report(df, basename):
    # Saves report with mean values on numerical metrics
    with open(f"{METRICS_OUTPUT_DIRECTORY}/metrics_{basename}_report.txt", "w") as f:
        f.write(str(df[METRICS_LIST].mean()))


def read_results_file(results_file_path):
    return pd.read_csv(results_file_path, encoding="utf-8")


def save_results(df, basename):
    # Code to save the results
    metrics_results_file_path = f"{METRICS_OUTPUT_DIRECTORY}/metrics_{basename}"
    df.to_csv(metrics_results_file_path)
    print(f"Metrics saved to {metrics_results_file_path}")


def save_human_review(df, basename):
    # Save Human reviewable file
    df[["question", "SQL Query", "SQL Query Results", "SQL-to-NL response"]].to_csv(
        f"{METRICS_OUTPUT_DIRECTORY}/human_review_{basename}"
    )
    print(
        f"Human reviewable file saved to {METRICS_OUTPUT_DIRECTORY}/human_review_{basename}"
    )


def create_metrics(results_file_path, client):
    basename = os.path.basename(results_file_path)
    print(f"Creating metrics for {basename}")
    df = read_results_file(results_file_path)

    df["E2E Groundedness"] = df.progress_apply(
        lambda row: end_to_end_groundedness(
            row["SQL Query"],
            row["SQL Query Results"],
            row["SQL-to-NL response"],
            client,
        ),
        axis=1,
    )
    df["E2E Relevance"] = df.progress_apply(
        lambda row: end_to_end_relevance(
            row["question"], row["SQL-to-NL response"], client
        ),
        axis=1,
    )
    df["SQL Query Execution Validity"] = df["SQL Query Results"].progress_apply(
        lambda x: "error" not in str(x).lower()
    )

    df["SQL Execution Exact Match"] = (
        df["SQL Query Results"] == df["Ground Truth SQL Execution Results"]
    )

    df["SQL Query Exact Match"] = df.progress_apply(
        lambda row: row["SQL Query"] == row["ground_truth"],
        axis=1,
    )
    df[
        "Ground Truth SQL Executed vs Generated SQL cosine similarity"
    ] = df.progress_apply(
        lambda row: evaluate_similarity(
            row["SQL Query Results"], row["Ground Truth SQL Execution Results"], client
        ),
        axis=1,
    )
    df["SQL Query Critic Score"] = df.progress_apply(
        lambda row: gpt_sql_critic_score(
            row["question"], row["SQL Query"], row["SQL Query Results"], client
        ),
        axis=1,
    )

    df["SQL Execution Is Empty"] = df.progress_apply(
        lambda row: is_sql_execution_empty(row["SQL Query Results"]),
        axis=1,
    )

    df["Ground Truth SQL Execution Is Empty"] = df.progress_apply(
        lambda row: is_sql_execution_empty(row["Ground Truth SQL Execution Results"]),
        axis=1,
    )

    save_results(df, basename)
    save_report(df, basename)
    save_human_review(df, basename)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Perform comprehensive evaluation of NL-to-SQL."
    )
    parser.add_argument(
        "--results_path",
        type=str,
        help="Path to csv file with required output",
        required=True,
    )

    args = parser.parse_args()
    client = set_up_client()
    create_metrics(args.results_path, client)
