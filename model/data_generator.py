import logging
import queue
import random
import time
from multiprocessing import Queue

import pandas as pd
from faker import Faker

from model.DAO import UserDAO
from model.goodreads_client_stub import GoodReadsClientStub
from model.user import User
from settings import GOOD_READS_SECRET, GOOD_READS_API


def generate_user(nums, write_into_database, book_list):
    user_list = []
    fake = Faker()
    id = 0
    inserted_ids = []

    while id < nums:
        book_index = random.randint(0, len(book_list) - 1)
        book_index2 = random.randint(0, len(book_list) - 1)
        user = User(fake.name(), fake.address(), fake.job(), random.randint(10, 100))
        logging.info("Created user: {}".format(user.serialize()))
        user_list.append(user.serialize())
        id += 1
    if write_into_database:
        repo = UserDAO()
        inserted_ids = repo.insert_documents(user_list, 'user_collection')
    return user_list, inserted_ids


def get_user_from_db():
    repo = UserDAO()
    return repo.get_users('user_collection')


def generate_books(book_id_found, book_id_to_search, good_reads):
    while True:
        try:
            book_id = book_id_to_search.get_nowait()
            if book_id >= 2300:
                break
        except queue.Empty:
            break
        else:

            logging.info('Searching book with id {}'.format(book_id))
            book = good_reads.book(book_id)
            book_id_found.put(book._book_dict)
            time.sleep(.5)
    return True

def gen_books(good_reads,user_dao):
    for i in range(1,5000):
        logging.info('Searching book with id {}'.format(i))
        try:
            book = good_reads.book(i)
            user_dao.insert_documents(book._book_dict, 'books', bulk=False)
        except Exception:
            pass

    return

def gen_users(user_dao):
    faker = Faker()
    for i in range(1, 5000):
        isbn_list = []
        description_list = []
        book_titles = []
        for j in range(1,5):
            book_id = random.randint(1,3031)
            book = user_dao.get_book_by_id(book_id)
            while book is None:
                book_id = random.randint(1, 3031)
                book = user_dao.get_book_by_id(str(book_id))
            logging.info('Getting book {}'.format(book_id))
            isbn_list.append(book['isbn'])
            description_list.append(book['description'])
            book_titles.append(book['title'])
        logging.info("Creating user {}".format(i))
        user = User(faker.name(), faker.address(), faker.job(), random.randint(1, 90))
        user.set_description(description_list)
        user.set_description(isbn_list)
        user.set_description(book_titles)
        user_dao.insert_documents(user.serialize(),collection='users',bulk=False)
    return


def generate_data():
    df = pd.read_csv("books.csv", error_bad_lines=False)
    book_id_found = Queue()
    book_id_to_search = Queue()
    processes = []
    good_reads = GoodReadsClientStub(GOOD_READS_API, GOOD_READS_SECRET)

    # for id in df['bookID']:
    #     book_id_to_search.put(id)
    # num = 1
    user_dao = UserDAO()
    gen_users(user_dao)
    return


def get_user(id):
    repo = UserDAO()
    user = repo.get_user_by_id(id)
    if user is None:
        raise (AttributeError, "unable to find the user by id {[]}".format(id))
    user.pop('_id', None)
    logging.info(str(user))
    return user


def create_user(name, address, job, age):
    user = User(name, address, job, age)
    id = random.randint(1,20000)
    user_dao = UserDAO()
    user_dao.insert_documents(user.serialize(),'user',bulk=False)
    user.set_id(id)
    return user.serialize()
