class User:

    def __init__(self, name, address, job, age):
        self.name = name
        self.address = address
        self.job = job
        self.age = age

    def serialize(self):
        return {
            'name': self.name,
            'address': self.address,
            'job': self.job
        }

