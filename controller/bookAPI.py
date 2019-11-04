from flask_restplus import Resource

from controller.restplus import api
from model.data_generator import generate_data

namespace = api.namespace('v1/books', description='model controller')


@namespace.route('/generate/')
class bookAPI(Resource):
    def get(self):
        return generate_data()

