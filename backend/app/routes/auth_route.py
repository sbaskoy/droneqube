
""" 
    auth routes
    includes login and register endpoints

"""
from flask import Blueprint

from app.middlewares.validations import validate_request
from app.controllers.auth_controller import AuthController
from app.validations.auth_schemas import LoginSchema, RegisterSchema

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

login_schema = LoginSchema()
register_Schema = RegisterSchema()


@auth_bp.route("/login", methods=["POST"])
@validate_request(login_schema)
def login():
    return AuthController.login()


@auth_bp.route("/register", methods=["POST"])
@validate_request(register_Schema)
def register():
    return AuthController.register()
