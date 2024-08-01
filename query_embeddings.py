import requests
import os
from dotenv import load_dotenv
import json
from retry import retry
from openai import AzureOpenAI
from constants import EMBEDDINGS_ENGINE, RESOURCE_ENDPOINT
from src.simple_RAG import run_nl_to_sql, set_up_client, run_sql_to_nl, get_top_k_most_similar_examples

load_dotenv(override=True)

API_KEY = os.getenv("AOAI_API_KEY")  # SET YOUR OWN API KEY HERE
COGSEARCH_API_KEY=os.getenv("AI_COG_SEARCH_KEY")

endpoint = "https://cogsearch-remmey.search.windows.net"
index_name="customer-index"
version="2023-11-01"

url = f"{endpoint}/indexes/{index_name}/docs/search?api-version={version}"

headers = {
  "Content-Type": "application/json",
  "api-key": f"{COGSEARCH_API_KEY}"
}

client = AzureOpenAI(
    azure_endpoint=RESOURCE_ENDPOINT,
    api_key=API_KEY,
    api_version="2024-05-01-preview",
)

@retry(delay=1, backoff=1.1, tries=5)
def get_embeddings(client, text, model=EMBEDDINGS_ENGINE):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

vector = get_embeddings(client, "How many products are in the Adventure Works database?")
# vector=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
# print(vector)

data={
  "count": True,
  "select": "sql_query",
  "vectorQueries": [
    {
      "vector": vector,
      "k": 7,
      "fields": "embedding",
      "kind": "vector",
      'exhaustive': True
    }
  ]
}
print(headers)
print('url', url)
print('data:', data)
# print(json.dumps(data))
response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)