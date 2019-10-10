import random

from faker import Faker

from flaskWebApp.users.user import User


def generate_user(nums):
    user_list = []
    fake = Faker()
    id = 0;
    while id <= nums:
        user = User(fake.name(), fake.address(), fake.job(),random.randint(10,100))
        user_list.append(user)
        id += 1
    return user_list


def create_user(name, address, job):
    return User(name, address, job)
