from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

from app import routes
from app import schemas as database
from app.schemas.Role import create_default_roles

from app.middlewares.error_handler import handle_error, handle_app_error
from app.models.app_error import AppError

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
load_dotenv()
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
