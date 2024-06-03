

from app.schemas import db
from app.schemas.User import User, get_hashed_password


class UserRepository:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(id: int):
        return User.query.get(id)

    @staticmethod
    def get_user_by_username(username: str):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def add_user(user: User, hash_pwd: bool = True):
        if hash_pwd:
            user.password = get_hashed_password(user.password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update_user(user: User):
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user: User):
        db.session.delete(user)
        db.session.commit()
        return user
