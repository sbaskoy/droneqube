
from app.schemas import db
from enum import Enum
from sqlalchemy_serializer import SerializerMixin


class Roles(Enum):
    Admin = "Admin"
    User = "User"


class Role(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Enum(Roles), unique=True, nullable=False)

    def __repr__(self):
        return f'<Role {self.name}>'



