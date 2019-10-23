from pymongo import MongoClient

class UserDAO:

    def __init__(self):
        client = MongoClient()

    def get_database(self, database_name='user_db'):
        return self.client[database_name]

    def insert_document(self, user_data, collection):
        db = self.get_database(self.client)
        collection = db[collection]
        inserted_id = collection.insert_one(user_data).inserted_id
        return inserted_id