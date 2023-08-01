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
        schema_info += f"\nTable: '{table_name}'\n"

        # Get the column names and data types for the current table
        cursor.execute(f"PRAGMA table_info('{table_name}');")
        columns = cursor.fetchall()

        for column in columns:
            col_name = column[1]
            col_type = column[2]
            schema_info += f"\tColumn: {col_name}, Type: {col_type}\n"

        # Get the primary key information for the current table
        cursor.execute(f"PRAGMA table_info('{table_name}');")
        primary_keys = [col[1] for col in cursor.fetchall() if col[5] == 1]

        if primary_keys:
            schema_info += f"\tPrimary Key(s): {', '.join(primary_keys)}\n"

        # Get the foreign key information for the current table
        cursor.execute(f"PRAGMA foreign_key_list('{table_name}');")
        foreign_keys = cursor.fetchall()

        if foreign_keys:
            schema_info += "\tForeign Keys:\n"
            for fk in foreign_keys:
                table_to = fk[2]
                col_from = fk[3]
                col_to = fk[4]
                schema_info += f"\t\tFrom: '{table_name}'.{col_from} -> To: {table_to}.{col_to}\n"

    # Close the database connection
    cursor.close()
    conn.close()

    return schema_info




def test():
    # Provide the path to your SQLite database file here
    database_file = "northwind.db"

    # Call the function to get the schema information
    schema_info = get_schema_info(database_file)

    # Print or use the schema_info variable to present the schema details to ChatGPT
    print(schema_info)

test()