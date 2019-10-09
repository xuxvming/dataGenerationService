from flaskWebApp.controller.restplus import api
from flask_restplus import fields

user = api.model('Users', {
    'id': fields.Integer(readOnly=True, description='user id'),
    'name': fields.String(required=True, description='user name'),
    'job': fields.String(required=True, description='user job'),
    'address': fields.String(required=True, description='user address'),
})
