1. Gather sample questions and answers and put in a CSV (as shown in `src/data/sql_query_examples.csv`)

2. Extract Schema from SQL DB - may need to be updated depending on customer scenario. The purpose of this step is to extract a schema description into a .txt file to be used as context for LLM calls for SQL generation.

   `python extract_descriptions.py`

3. Generate embeddings 

    `python generate_ai_search_vectors.py`

4. Command to start the application
    `streamlit run app.py`

# TO DO
- Update authentication
- Add instructions
