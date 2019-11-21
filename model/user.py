class User:

    def __init__(self, name, address, job, age):
        self.name = name
        self.address = address
        self.job = job
        self.age = age

    def serialize(self):
        try:
            res = {
            'name': self.name,
            'address': self.address,
            'job': self.job,
            'age': self.age,
            'isbns': self.isbn,
            'descriptions': self.description,
            'title': self.title
        }
        except AttributeError:
            res = {'name': self.name,
            'address': self.address,
            'job': self.job,
            'age': self.age,}
        return res

    def set_description(self, description):
        self.description = description

    def set_title(self, title):
        self.title = title

    def set_isbn(self, isbn):
        self.isbn = isbn
