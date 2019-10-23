# Flask settings
FLASK_SERVER_NAME = 'localhost:8080'
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False


MONGO_DB_CONNECTION = "mongodb+srv://admin:pwd@adaptive-application-eorih.gcp.mongodb.net/test?retryWrites=true&w=majority"