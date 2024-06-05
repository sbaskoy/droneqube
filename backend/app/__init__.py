from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flask_cors import CORS
import os
from app import routes
from app import schemas as database
from app.schemas.Role import create_default_roles

from app.middlewares.error_handler import handle_error, handle_app_error
from app.models.app_error import AppError

load_dotenv()

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

allowed_origins = os.getenv('ALLOWED_ORIGINS').split(',')

CORS(app,
     origins=allowed_origins,
     supports_credentials=True,
     allow_headers=["Content-Type", "Authorization",
                    "Access-Control-Allow-Credentials"],
     methods=["GET", "POST", "DELETE", "OPTIONS"]
     )


jwt = JWTManager(app)


with app.app_context():
    database.init(app)
    routes.set_routes(app)
    create_default_roles()
    # upload_test_image()


@app.errorhandler(AppError)
def unhandled_exception(error):
    return handle_app_error(error)


if (not app.config["DEBUG"]):
    @app.errorhandler(Exception)
    def unhandled_exception(error):
        return handle_error(error, 500)


# @app.after_request
# def handle_options(response):
#     response.headers.add('Content-Type', 'application/json')
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Methods',
#                          'PUT, GET, POST, DELETE, OPTIONS')
#     response.headers.add('Access-Control-Allow-Headers',
#                          'Content-Type,Authorization')
#     response.headers.add('Access-Control-Expose-Headers',
#                          'Content-Type,Content-Length,Authorization,X-Pagination')
#     print("After request", response)
#     return response
