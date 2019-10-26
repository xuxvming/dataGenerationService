from flask_restplus import fields
from flask_restplus import reqparse

from controller.restplus import api

user = api.model('Users', {
    'name': fields.String(required=True, description='user name'),
    'job': fields.String(required=True, description='user job'),
    'address': fields.String(required=True, description='user address'),
    'age': fields.Integer(required=True, description='user age'),
})

book = api.model('Books',{
    'bookID':fields.String(description='book id'),
    'title':fields.String(description='book title'),
    'authors':fields.String(description='book authors'),
    'average_rating':fields.String(description='book average_rating'),
    'isbn':fields.String(description='book isbn'),
    'language_code':fields.String(description='book language_code'),
    'num_pages':fields.String(description='book num_pages'),
    'ratings_count':fields.String(description='book ratings_count'),
    'text_reviews_count':fields.String(description='book text_reviews_count'),
    'user_id':fields.String(description='user id'),
})
user_quantity_args = reqparse.RequestParser()
user_quantity_args.add_argument('number', type=int, required=False, default=1, help='number of users')
user_quantity_args.add_argument('db', type=bool, required=False, default=False, help='populate generated records to database, default false')