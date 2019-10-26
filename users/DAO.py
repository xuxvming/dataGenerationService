import ssl

from pymongo import MongoClient

from settings import MONGO_DB_CONNECTION


class UserDAO:

    client = MongoClient(MONGO_DB_CONNECTION,ssl_cert_reqs=ssl.CERT_NONE)

    def get_database(self, database_name='user_db'):
        return self.client[database_name]

    def insert_documents(self, dataset, collection):
        db = self.get_database()
        collection = db[collection]
        inserted_ids = collection.insert_many(dataset).inserted_ids
        return inserted_ids

    def drop_collection(self,collection):
        db = self.get_database()
        db.drop_collection(collection)

    def get_users(self,collection):
        db = self.get_database()
        collection = db[collection]
        users = collection.find({})
        res = []
        for user in users:
            res.append(user)
        return res
