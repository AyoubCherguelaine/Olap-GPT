from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)

    def __enter__(self):
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

class MyDatabase:
    def __init__(self, connection_string, database_name, collection_name):
        self.connection_string = connection_string
        self.database_name = database_name
        self.collection_name = collection_name

    def insert_document(self, document):
        with MongoDBConnection(self.connection_string) as client:
            collection = client[self.database_name][self.collection_name]
            insert_result = collection.insert_one(document)
            print("Inserted document ID:", insert_result.inserted_id)

    def find_documents(self, query):
        with MongoDBConnection(self.connection_string) as client:
            collection = client[self.database_name][self.collection_name]
            documents = collection.find(query)
            for doc in documents:
                print(doc)

    def update_document(self, query, new_values):
        with MongoDBConnection(self.connection_string) as client:
            collection = client[self.database_name][self.collection_name]
            update_result = collection.update_one(query, new_values)
            print("Modified documents count:", update_result.modified_count)

    def delete_document(self, query):
        with MongoDBConnection(self.connection_string) as client:
            collection = client[self.database_name][self.collection_name]
            delete_result = collection.delete_one(query)
            print("Deleted documents count:", delete_result.deleted_count)


# Usage example
def main():
    connection_string = 'mongodb://localhost:27017/'
    database_name = 'your_database_name'
    collection_name = 'your_collection_name'

    my_db = MyDatabase(connection_string, database_name, collection_name)

    # Insert a document
    document = {"name": "John Doe", "age": 30, "city": "New York"}
    my_db.insert_document(document)

    # Find documents
    query = {"city": "New York"}
    my_db.find_documents(query)

    # Update a document
    query = {"name": "John Doe"}
    new_values = {"$set": {"age": 31}}
    my_db.update_document(query, new_values)

    # Delete a document
    query = {"name": "John Doe"}
    my_db.delete_document(query)

