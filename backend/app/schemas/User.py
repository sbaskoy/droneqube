"""
    user database schema
    encrypts the user password with sha256 method and verifies the given password
"""
from app.schemas import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin


class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=False, nullable=True)
    last_name = db.Column(db.String(80), unique=False, nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', )

    serialize_rules = ('-role_id', "-password")

    def __repr__(self):
        return f'<User {self.username} - {self.name} {self.last_name}>'

    def set_password(self, new_password):
        self.password = generate_password_hash(
            new_password, method='pbkdf2:sha256')

    def check_password(self, entered_password):
        return check_password_hash(self.password, entered_password)

    def change_password(self, new_password):
        self.set_password(new_password)
        db.session.commit()


def get_hashed_password(password: str) -> str:
    return generate_password_hash(password, method='pbkdf2:sha256')
