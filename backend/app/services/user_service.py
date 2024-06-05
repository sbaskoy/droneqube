
from app.models.app_error import AppError
from app.repositories.user_repository import User, UserRepository
from app.services.role_services import  RoleService, Roles
from app.utils import string_to_enum


class UserService:
    @staticmethod
    def get_all():
        return UserRepository.get_all_users()

    @staticmethod
    def get_user_by_id(id: int) -> User | None:
        return UserRepository.get_user_by_id(id=id)

    @staticmethod
    def create(data) -> User:
        username = data.get("username")
        password = data.get("password")
        name = data.get("name")
        last_name = data.get("last_name")
        role_string = data.get("role")
        role = RoleService.get_role_by_name(
            role=string_to_enum(role_string, Roles))
        if not role:
            raise AppError(
                message=f"Role '{role_string}' does not exist", status_code=400, code="ROLE_NOT_FOUND")
        user = User(
            name=name,
            last_name=last_name,
            username=username,
            password=password,
            role=role,
        )
        return UserRepository.add_user(user=user)

    @staticmethod
    def find_by_username_and_password(username: str, password: str) -> User:
        user = UserRepository.get_user_by_username(username=username)
        if not user or not user.check_password(password):
            raise AppError(message="Username or password incorrect",
                           status_code=401, code="INVALID_USERNAME_PASSWORD",)
        return user

    @staticmethod
    def find_by_username(username: str) -> User:
        user = UserRepository.get_user_by_username(username=username)
        return user
