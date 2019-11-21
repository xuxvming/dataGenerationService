import logging

from flask import request
from flask_restplus import Resource

from controller.restplus import api
from controller.serilizers import user, user_quantity_args, book
from model.data_generator import generate_user, create_user, generate_data, get_user

log = logging.getLogger(__name__)

namespace = api.namespace('v1/model', description='model controller')


@namespace.route('/generate/')
class userAPI(Resource):

    @api.marshal_list_with(user)
    @api.expect(user_quantity_args)
    def get(self):

        args = user_quantity_args.parse_args(request)
        res, ids = generate_user(args.get('number'),args.get('db'))
        return res
    @api.expect(user)
    def post(self):
        name = request.json['name']
        address = request.json['address']
        job = request.json['job']
        age = request.json['age']
        res = create_user(name, address, job, age)
        return res

@namespace.route('/db')
class GetBookWithUserID(Resource):
    @api.marshal_list_with(book)
    def get(self):
        return generate_data(collection='book_collection')

@namespace.route('/db/user/<string:user_id>')
class GetUserFromDB(Resource):
    @api.marshal_list_with(user)
    def get(self,user_id):
        return get_user(user_id)