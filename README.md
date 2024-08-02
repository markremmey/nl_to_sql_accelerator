## Pre-requisites:
- SQL Database (if using sample data, use Azure SQL with Adventure Works dataset)
- Azure AI Search

## Instructions 
1. Create an Azure SQL DB using the Adventure Works Sample Dataset (https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms)
![image](https://github.com/user-attachments/assets/97051a38-afc8-4463-b427-2260dd1d048b)

2. Update .env and constants.py with your environment variables
3. Gather sample questions and answers and put in a CSV (as shown in `src/data/sql_query_examples.csv`)
4. Extract Schema from SQL DB - may need to be updated depending on customer scenario. The purpose of this step is to extract a schema description into a .txt file to be used as context for LLM calls for SQL generation.

   `python extract_descriptions.py`

5. Generate vector database

    `python generate_ai_search_vectors.py`

6. Command to start the application
    `streamlit run app.py`

## Authentication Options


## Networking Guidance / Recommendations


# TO DO
- Update authentication
- Add instructions
- auth options - use entra ID rather than DB password
- Consider MySQL, Postgres (could be long-term)
- Networking - currently I have whitelisted
- Move to Azure repo - (keep private)
