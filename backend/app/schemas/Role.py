
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


def create_default_roles():
    existing_roles = Role.query.all()
    if not existing_roles:
        # Veri yoksa Admin ve User rollerini ekle
        admin_role = Role(name=Roles.Admin)
        user_role = Role(name=Roles.User)

        db.session.add(admin_role)
        db.session.add(user_role)
        db.session.commit()
        print("Admin ve User rolleri başarıyla eklendi.")
