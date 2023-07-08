import sqlite3

class SQLiteConnector:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            print("Connected to database:", self.db_name)
        except sqlite3.Error as e:
            print("Error connecting to database:", e)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from database:", self.db_name)
        else:
            print("No active connection.")

    def execute_query(self, query):
        if self.connection:
            try:
                cursor = self.connection.cursor()
                cursor.execute(query)
                rows = cursor.fetchall()
                cursor.close()
                return rows
            except sqlite3.Error as e:
                print("Error executing query:", e)
                return None
        else:
            print("No active connection.")
            return None


def test():
    # Create a connector instance
    connector = SQLiteConnector("mydatabase.db")

    # Connect to the database
    connector.connect()

    # Execute a query
    result = connector.execute_query("SELECT * FROM mytable")

    # Process the query result
    if result:
        for row in result:
            print(row)

    # Disconnect from the database
    connector.disconnect()

test()
