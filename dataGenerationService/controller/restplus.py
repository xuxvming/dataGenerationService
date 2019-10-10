import logging

from flask_restplus import Api

from dataGenerationService import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='data generation service',
          description='REST endpoints to generate user data')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500

