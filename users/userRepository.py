
class UserRepository:

    def get_database(self,client, database_name='userdb'):
        return client[database_name]

    def insert_document(self,client, user_data, collection):
        db = self.get_database(client)
        collection = db[collection]
        inserted_id = collection.insert_one(user_data).inserted_id
        return inserted_id