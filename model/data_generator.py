import logging
import queue
import random
import time
from multiprocessing import Process, Queue

import pandas as pd
from faker import Faker

from model.DAO import UserDAO
from model.goodreads_client_stub import GoodReadsClientStub
from model.user import User
from settings import GOOD_READS_SECRET, GOOD_READS_API, NUM_PROCESSES


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
        except queue.Empty:
            break
        else:

            logging.info('Searching book with id {}'.format(book_id))
            book = good_reads.book(book_id)
            book_id_found.put(book._book_dict)
            time.sleep(.5)
    return True


def generate_data():
    df = pd.read_csv("books.csv", error_bad_lines=False)
    book_id_found = Queue()
    book_id_to_search = Queue()
    processes = []
    good_reads = GoodReadsClientStub(GOOD_READS_API, GOOD_READS_SECRET)

    for id in df['bookID']:
        book_id_to_search.put(id)
    num = 1
    user_dao = UserDAO()
    while num < NUM_PROCESSES:
        process = Process(target=generate_books, args=(book_id_found,book_id_to_search, good_reads))
        processes.append(process)
        process.start()
        num += 1

    for process in processes:
        process.join()
    user_dao.insert_documents(book_id_found,'book',bulk=True)
    return book_id_found


def get_user(id):
    repo = UserDAO()
    user = repo.get_user_by_id(id)
    if user is None:
        raise (AttributeError, "unable to find the user by id {[]}".format(id))
    user.pop('_id', None)
    logging.info(str(user))
    return user


def create_user(name, address, job, age):
    return User(name, address, job, age)
