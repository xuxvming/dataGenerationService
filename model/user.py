class User:
    id = None
    title = None
    description = None
    isbns = None

    def __init__(self, name, address, job, age):
        self.name = name
        self.address = address
        self.job = job
        self.age = age

    def serialize(self):

        if self.title is None:
            res = {'name': self.name,
                   'address': self.address,
                   'job': self.job,
                   'age': self.age,
                   'id': self.id}
        else:
            res = {
            'name': self.name,
            'address': self.address,
            'job': self.job,
            'age': self.age,
            'isbns': self.isbn,
            'descriptions': self.description,
            'title': self.title}
        return res

    def set_description(self, description):
        self.description = description

    def set_title(self, title):
        self.title = title

    def set_isbn(self, isbn):
        self.isbn = isbn

    def set_id(self,id):
        self.id = id
