import logging

from flask_restplus import Resource
from flask import Response
import json
from flaskWebApp.users.user_generator import generate_user
from flaskWebApp.controller.restplus import api
from flaskWebApp.controller.serilizers import user

log = logging.getLogger(__name__)

namespace = api.namespace('v1/users',description = 'users controller')

@namespace.route('/generate/<int:number>')
class userAPI(Resource):

    @api.marshal_list_with(user)
    def get(self, number):
        res = generate_user(number)
        return res