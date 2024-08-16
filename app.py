import pandas as pd
import streamlit as st
from src.simple_RAG import run_nl_to_sql, set_up_client, run_sql_to_nl

embeddings_database_path = "./src/data/embeddings_db.pkl"
embeddings_db = pd.read_pickle(embeddings_database_path)
top_k=5
schema = open('src/data/descriptions_text.txt', "r").read()

def main():
    st.title("NL to SQL Accelerator")
    st.write("Ask any Question regarding the Adventure Works DB.")

    user_query = st.text_input("Enter your query:")

    if st.button("Submit"):
        try:
            st.write(f"Query submitted: {user_query}")

            client = set_up_client()

            # Step 1 NL to SQL
            sql_completion, nl_to_sql_execution_time = run_nl_to_sql(
                user_query, client, embeddings_db, top_k, schema
            )
            st.write(f"SQL Query: {sql_completion}")

            # step 2:SQL to NL 
            (
              sql_to_nl_completion,
              sql_to_nl_execution_time,
              sql_execution_result,
            ) = run_sql_to_nl(user_query, client, sql_completion)

            st.write(f"SQL to NL: {sql_to_nl_completion}")


        except Exception as e:
            st.error(f"An error occurred: {e}")
            

if __name__ == "__main__":
    main()