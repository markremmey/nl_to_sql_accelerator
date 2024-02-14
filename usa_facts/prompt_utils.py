def make_message_system(content: str, role: str = "assistant"):
    return {"role": role, "content": content}


def make_message_user(content: str, role: str = "user"):
    return {"role": role, "content": content}


def generate_nl_to_sql_user_prompt(query):
    prompt = f"""Your response should be an executable query, do not start with '''sql
Provide detailed reasoning behind the PostgreSQL query, please provide it as a comment using -- at the beginning of the line. 

Formatting example:
SELECT some_name, val 
FROM some_table 
WHERE a = number AND b = another_number
-- This query selects some_name and val from some_table where a = number and b = another_number

Queries should return a minimal amount of rows, and should not return more rows than necessary.

User question: {query}

PostgreSQL query:

"""
    return prompt


def generate_nl_to_sql_system_prompt(schema, examples):

    prompt = f"""You are an expert in providing facts from SQL database. 
    Given the user question, produce a PostgreSQL query which, when executed, provides the correct answer to the question. 
    Assume the data is for United States only.
    Only use the tables and schema given below to answer the questions. Learn query patterns from the similar question-answer pairs provided as examples below.
    Directly start your response with the executable query.Do not start with '''sql.
    Do not make up new table and column names. Only use the ones available in the schema below.

    SQL Schema: 
    {schema}

    Examples:
    {examples}
   
    """

    return prompt


def generate_sql_to_nl_system_prompt():

    prompt = """Given the original question, the corresponding PostgreSQL query, and the execution results, produce a truthful and accurate natural language response to the original question, that is only based on the execution results.

Your answer should be detailed and accurate, for numerical responses make sure you infer the appropriate units.
If the question is complex, you can provide a multi-sentence response.
Make sure that you provide a response that is easy to understand.
"""

    return prompt


def generate_sql_to_nl_user_prompt(question, sql_query, sql_query_results):

    prompt = f"""Question: {question}    
SQL Query: {sql_query}
SQL Query Results: {sql_query_results}

"""
    return prompt
