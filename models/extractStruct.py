import sqlite3

class DatabaseRepresentation:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        self.db_representation = []

    def get_table_names(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = self.cursor.fetchall()
        return tables

    def get_column_names(self, table_name):
        self.cursor.execute(f"PRAGMA table_info('{table_name}');")
        columns = self.cursor.fetchall()
        return columns

    def get_foreign_key_columns(self, table_name):
        self.cursor.execute(f"PRAGMA foreign_key_list('{table_name}');")
        foreign_keys = self.cursor.fetchall()
        foreign_key_columns = [fk[3] for fk in foreign_keys]
        return foreign_key_columns

    def build_table_representation(self, table_name, columns, foreign_key_columns):
        table_representation = f"{table_name}("
        column_representations = []

        for column in columns:
            column_name = column[1]
            column_type = column[2]

            if column[5] == 1:
                column_representations.append(f"#{column_name}:{column_type}")  # Primary key
            elif column_name in foreign_key_columns:
                column_representations.append(f"${column_name}:{column_type}")  # Foreign key
            else:
                column_representations.append(f"{column_name}:{column_type}")

        table_representation += ",".join(column_representations)
        table_representation += ")"
        return table_representation

    def generate_db_representation(self):
        tables = self.get_table_names()
        db_representation = [] 
        for table in tables:
            table_name = table[0]
            columns = self.get_column_names(table_name)
            foreign_key_columns = self.get_foreign_key_columns(table_name)
            table_representation = self.build_table_representation(table_name, columns, foreign_key_columns)
            db_representation.append(table_representation)
        self.db_representation = db_representation.copy()

    def print_db_representation(self):
        for table_representation in self.db_representation:
            print(table_representation)
            print()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


def test():
    # Usage example:
    db = DatabaseRepresentation('northwind.db')
    db.generate_db_representation()
    db.print_db_representation()
    db.close_connection()


# test()