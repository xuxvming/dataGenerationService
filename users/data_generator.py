import logging
import random

import pandas as pd
from faker import Faker

from users.DAO import UserDAO
from users.user import User


def generate_user(nums,write_into_database):
    user_list = []
    fake = Faker()
    id = 0
    inserted_ids = []
    while id < nums:
        user = User(fake.name(), fake.address(), fake.job(),random.randint(10,100))
        logging.info("Created user: {}".format(user.serialize()))
        user_list.append(user.serialize())
        id += 1
    if write_into_database:
        repo = UserDAO()
        inserted_ids = repo.insert_documents(user_list,'user_collection')
    return user_list, inserted_ids

def get_user_from_db():
    repo = UserDAO()
    return repo.get_users('user_collection')

def generate_books():
    df = pd.read_csv("books.csv",error_bad_lines=False)
    return df

def generate_data(collection):
    # use database user id
    book_list = generate_books()
    user_list, ids = generate_user(len(book_list),True)
    if not len(book_list) == len(user_list):
        raise (AssertionError,"Length of users and books are not equal")

    book_list['user_id'] = ids
    book_dict = book_list.to_dict(orient='records')
    repo = UserDAO()
    repo.insert_documents(book_dict,collection)
    return book_dict

def get_user(id):
    repo = UserDAO()
    user = repo.get_user_by_id(id)
    if user == None:
        raise (AttributeError,"unable to find the user by id {[]}".format(id))

    user.pop('_id',None)
    logging.info(str(user))
    return user

def create_user(name, address, job, age):
    return User(name, address, job, age)
