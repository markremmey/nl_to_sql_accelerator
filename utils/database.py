def run_query(query, connection, timeout=None):
    try:
        return execute_query(query, connection, timeout)
    except Exception as e:
        handle_database_error(e, connection)


def execute_query(query, connection, timeout):
    print("Query: ", query)
    with connection.cursor() as cursor:
        if timeout:
            cursor.execute(f"SET statement_timeout TO {timeout};")
        cursor.execute(query)
        return cursor.fetchall()


def handle_database_error(exception, connection):
    print(f"An error occurred while executing query: {exception}")
    connection.rollback()
    return f"Error: {exception}"
