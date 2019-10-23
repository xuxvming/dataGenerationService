import random

from faker import Faker

from users.user import User
from users.userDAO import client as DAO
from users.userRepository import UserRepository


def generate_user(nums,write_into_database=True):
    user_list = []
    fake = Faker()
    id = 0
    while id <= nums:
        user = User(fake.name(), fake.address(), fake.job(),random.randint(10,100))
        if write_into_database:
            repo = UserRepository()
            repo.insert_document(DAO,user_data=user.serialize(),collection='user_collection')
        user_list.append(user)
        id += 1
    return user_list


def create_user(name, address, job):
    return User(name, address, job)
