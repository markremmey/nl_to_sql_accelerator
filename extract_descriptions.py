from constants import (
    DB_HOST,
    DB_NAME,
    DB_PORT,
    DB_USER,
    EMBEDDINGS_ENGINE,
    RESOURCE_ENDPOINT,
    GPT4_ENGINE_32k,
)

import json
import os
import pyodbc
from dotenv import load_dotenv

load_dotenv(override=True)
API_KEY = os.getenv("AOAI_API_KEY")
DB_PASSWORD = os.getenv("DB_PASSWORD")


table_desc_list = []

query="""
SELECT * FROM information_schema.tables WHERE table_type = 'BASE TABLE';
"""

connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={DB_HOST},{DB_PORT};DATABASE={DB_NAME};UID={DB_USER};PWD={DB_PASSWORD}"

# Connect to the SQL Server database
try:
    DB_CONNECTION = pyodbc.connect(connection_string, timeout=30)
    print("Database connection established.")
except Exception as e: 
    print(f"An error occurred while connecting to the database: {e}")
    DB_CONNECTION = None

def run_query(query, connection, timeout=None):
    try:
        return execute_query(query, connection, timeout)
    except Exception as e:
        return handle_database_error(e, connection)


def execute_query(query, connection, timeout):
    with connection.cursor() as cursor:
        if timeout:
            cursor.execute(f"SET LOCK_TIMEOUT {timeout};")
        cursor.execute(query)
        return cursor.fetchall()


def handle_database_error(exception, connection):
    print(f"An error occurred while executing query: {exception}")
    connection.rollback()
    return f"Error: {exception}"


query = """
SELECT table_name 
FROM information_schema.tables 
WHERE table_type = 'BASE TABLE';
"""

# columns_query_template = """
# SELECT column_name, data_type 
# FROM information_schema.columns 
# WHERE table_name = ?;
# """

if DB_CONNECTION:
    sql_execution_result = run_query(query, DB_CONNECTION)
    for row in sql_execution_result:
        print(row)
else:
    print("Database connection not established.")
print(sql_execution_result)

# Function to get columns for a table
def get_columns_for_table(table_name, connection):
    
    columns_query_template = f"""
    SELECT column_name, data_type
    FROM information_schema.columns 
    WHERE table_name = ?;
    """
    
    with connection.cursor() as cursor:
        cursor.execute(columns_query_template, table_name)
        columns = cursor.fetchall()
        return columns

for table_name in sql_execution_result:
    table_desc = {}
    print(f"Table: {table_name}")
    table_desc["table"] = table_name
    table_desc["columns"] = []
    columns = get_columns_for_table(table_name, DB_CONNECTION)
    for column in columns:
        table_desc["columns"].append({"name": column[0], "data_type": column[1]})
        print(f"  Column: {column[0]}, Data Type: {column[1]}")

    table_desc_list.append(table_desc)
print(table_desc_list)

file_path='./descriptions_text.txt'

with open(file_path, 'w') as text_file:
    text_file.write(str(table_desc_list))
    # json.dump(data, json_file, indent=4)
print(f"Data written to {file_path}")


DB_CONNECTION.close()