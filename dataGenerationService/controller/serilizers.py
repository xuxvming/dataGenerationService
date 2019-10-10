from flask_restplus import fields
from flask_restplus import reqparse

from dataGenerationService.controller.restplus import api

user = api.model('Users', {
    'id': fields.String(readOnly=True, description='user id'),
    'name': fields.String(required=True, description='user name'),
    'job': fields.String(required=True, description='user job'),
    'address': fields.String(required=True, description='user address'),
    'age': fields.Integer(required=True, description='user age'),
})

user_quantity_args = reqparse.RequestParser()
user_quantity_args.add_argument('num', type=int, required=False, default=1, help='number of users')