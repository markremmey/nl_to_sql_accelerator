1. Create an Azure SQL DB using the Adventure Works Sample Dataset (https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms)
![image](https://github.com/user-attachments/assets/97051a38-afc8-4463-b427-2260dd1d048b)

2. Gather sample questions and answers and put in a CSV (as shown in `src/data/sql_query_examples.csv`)

3. Extract Schema from SQL DB - may need to be updated depending on customer scenario. The purpose of this step is to extract a schema description into a .txt file to be used as context for LLM calls for SQL generation.

   `python extract_descriptions.py`

4. Generate embeddings 

    `python generate_ai_search_vectors.py`

5. Command to start the application
    `streamlit run app.py`

# TO DO
- Update authentication
- Add instructions
