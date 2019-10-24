import uuid
class User:

    def __init__(self, name, address, job, age):
        self.id = uuid.uuid4()
        self.name = name
        self.address = address
        self.job = job
        self.age = age

    def serialize(self):
        return {
            '_id': self.id,
            'name': self.name,
            'address': self.address,
            'job': self.job
        }
