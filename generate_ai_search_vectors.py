from openai import AzureOpenAI
import os
import pandas as pd
from retry import retry
from azure_ai_search_payload import vector_index_payload
import json
from constants import EMBEDDINGS_ENGINE, RESOURCE_ENDPOINT
import requests
from dotenv import load_dotenv

"""
script used to generate an offline DB for embeddings
note: output data as .pkl to keep embedding structure
python generate_embeddings.py <input data path> <output data path> <output file name>
"""
load_dotenv(override=True)

API_KEY = os.getenv("AOAI_API_KEY")  # SET YOUR OWN API KEY HERE
COGSEARCH_API_KEY=os.getenv("AI_COG_SEARCH_KEY")

client = AzureOpenAI(
    azure_endpoint=RESOURCE_ENDPOINT, api_key=API_KEY, api_version="2024-05-01-preview"
)

@retry(delay=1, backoff=1.1, tries=20)
def get_embeddings(text, model=EMBEDDINGS_ENGINE):
    return client.embeddings.create(input=text, model=model).data[0].embedding

# Add embeddings to golden records

golden_record_path = 'src/data/golden_records_questions.csv'

df = pd.read_csv(golden_record_path)
df['id'] = df.index.astype(str)
df["@search.action"] = "upload"
df['embedding'] = df["question"].apply(
    lambda x: get_embeddings(x)
)

golden_record_json = {"value": df.to_dict(orient='records')}


with open('./src/data/golden_records.json', 'w') as file:
    file.write(json.dumps(golden_record_json))

# Define the endpoint and index name
endpoint = "https://cogsearch-remmey.search.windows.net"  # Replace with your actual endpoint
# index_name = "index-embeddings"  # Replace with your actual index name
version="2024-03-01-Preview"
index_name="customer-index"


# Construct the full URL
url = f"{endpoint}/indexes/{index_name}"
print('url:', url)

# Define the headers, if necessary (e.g., for authentication or content type)
headers = {
    'Content-Type': 'application/json',  # Set the content type to JSON if you're sending JSON data
    'api-key': f'{COGSEARCH_API_KEY}' # Replace with your actual token if required
}

params = {
    'api-version': version
}

json_data = json.dumps(vector_index_payload)

print('headers', headers)
print('json_data:', json_data)
print('params:', params)

# Create the Vector Index
response = requests.put(url, headers=headers, data=json_data, params=params)

# Check the response status code
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)

file_path = './src/data/golden_records.json'


with open(file_path, 'r') as file:
    data = json.load(file)

# Upload the golden records with vector embeddings to AI Search
upload_url = f"{endpoint}/indexes/{index_name}/docs/search.index?api-version={version}"

# print("data:", data)
response = requests.post(upload_url, headers=headers, json=data)
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code, response.text)