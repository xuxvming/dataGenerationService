import logging

from flask import request
from flask_restplus import Resource

from controller.restplus import api
from controller.serilizers import user, user_quantity_args
from users.user_generator import generate_user, create_user

log = logging.getLogger(__name__)

namespace = api.namespace('v1/users', description='users controller')


@namespace.route('/generate/')
class userAPI(Resource):

    @api.marshal_list_with(user)
    @api.expect(user_quantity_args)
    def get(self):
        # parameter, not path variable
        args = user_quantity_args.parse_args(request)
        res = generate_user(args.get('num'))
        return res

    @api.expect(user)
    def post(self, name, address, job):
        return create_user(name, address, job)
