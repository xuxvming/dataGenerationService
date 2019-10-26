import logging

from flask import request
from flask_restplus import Resource

from controller.restplus import api
from controller.serilizers import user, user_quantity_args, book
from users.data_generator import generate_user, create_user, generate_data

log = logging.getLogger(__name__)

namespace = api.namespace('v1/users', description='users controller')


@namespace.route('/generate/')
class userAPI(Resource):

    @api.marshal_list_with(user)
    @api.expect(user_quantity_args)
    def get(self):

        args = user_quantity_args.parse_args(request)
        res, ids = generate_user(args.get('number'),args.get('db'))
        return res

    @api.expect(user)
    def post(self, name, address, job, age):
        return create_user(name, address, job, age)

@namespace.route('/db')
class GetBookWithUserID(Resource):
    @api.marshal_list_with(book)
    def get(self):
        '''
        :param collection: set this to book_collection
        '''
        return generate_data(collection='book_collection')