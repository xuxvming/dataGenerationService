class User:

    def __init__(self,id, name, address, job):
        self.id = id
        self.name = name
        self.address = address
        self.job = job

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'job': self.job
        }
