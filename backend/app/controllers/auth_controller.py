"""
auth controller

allows user login and registration.
creates JWT token in login method

"""
from flask import jsonify, request
from flask_jwt_extended import create_access_token
from app.models.app_error import AppError
from app.services.user_service import UserService


class AuthController:
    @staticmethod
    def login():
        json_data = request.get_json()
        username = json_data['username']
        password = json_data['password']
        user = UserService.find_by_username_and_password(
            username=username, password=password)
        access_token = create_access_token(identity=user.id)
        return jsonify({
            "access_token": access_token,
            "user": user.to_dict()
        })

    @staticmethod
    def register():
        json_data = request.get_json()
        username = json_data["username"]

        user = UserService.find_by_username(username=username)
        if user:
            raise AppError("this username is already in use",
                           400, "USERNAME_EXISTS")
        user = UserService.create(json_data)
        access_token = create_access_token(identity=user.id)
        return jsonify({
            "access_token": access_token,
            "user": user.to_dict()
        })
