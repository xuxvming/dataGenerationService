from pymongo import MongoClient

from settings import MONGO_DB_CONNECTION


class UserDAO:

    client = MongoClient(MONGO_DB_CONNECTION)

    def get_database(self, database_name='user_db'):
        return self.client[database_name]

    def insert_document(self, user_data, collection):
        db = self.get_database()
        collection = db[collection]
        inserted_id = collection.insert_one(user_data).inserted_id
        return inserted_id