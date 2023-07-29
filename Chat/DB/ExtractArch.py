import sqlite3

def get_schema_info(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Retrieve the list of tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema_info = "Database Schema Information:\n"

    # Loop through each table and fetch the column information
    for table in tables:
        table_name = table[0]
        schema_info += f"\nTable: {table_name}\n"

        # Get the column names and data types for the current table
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        for column in columns:
            col_name = column[1]
            col_type = column[2]
            schema_info += f"\tColumn: {col_name}, Type: {col_type}\n"

    # Close the database connection
    cursor.close()
    conn.close()

    return schema_info


def test():
    # Provide the path to your SQLite database file here
    database_file = "path/to/your/database.sqlite"

    # Call the function to get the schema information
    schema_info = get_schema_info(database_file)

    # Print or use the schema_info variable to present the schema details to ChatGPT
    print(schema_info)
