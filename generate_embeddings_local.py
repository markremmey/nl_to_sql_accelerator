import argparse
import os

import pandas as pd
from constants import EMBEDDINGS_ENGINE, RESOURCE_ENDPOINT
from data.sql_query_examples_py import sql_query_examples
from openai import AzureOpenAI
from retry import retry

"""
script used to generate an offline DB for embeddings

note: output data as .pkl to keep embedding structure
python generate_embeddings.py <input data path> <output data path> <output file name>
"""

API_KEY = os.getenv("AOAI_API_KEY")  # SET YOUR OWN API KEY HERE

client = AzureOpenAI(
    azure_endpoint=RESOURCE_ENDPOINT, api_key=API_KEY, api_version="2024-05-01-preview"
)

@retry(delay=1, backoff=1.1, tries=20)
def get_embeddings(text, model=EMBEDDINGS_ENGINE):
    return client.embeddings.create(input=text, model=model).data[0].embedding

def generate_embeddings_database(input_data_df, output_data_path):
    print("Number of input examples:%s" % (len(input_data_df)))

    input_data_df["question_embeddings"] = df["question"].apply(
        lambda x: get_embeddings(x)
    )
    print("Embeddings completed.")

    input_data_df.to_pickle(output_data_path)
    print("Wrote embedding database to path: %s" % (output_data_path))


def generate_csv():
    return pd.DataFrame(sql_query_examples)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Given the python list with golden records, return a pkl embeddings database."
    )

    parser.add_argument(
        "--output_data_path",
        type=str,
        help="Output file for embeddings. Must be a .pkl file",
        required=True,
    )
    args = parser.parse_args()

    df = generate_csv()
    generate_embeddings_database(df, args.output_data_path)
