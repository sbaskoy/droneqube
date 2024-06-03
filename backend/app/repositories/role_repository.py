

from app.schemas import db
from app.schemas.Role import Role, Roles


class RoleRepository:
    @staticmethod
    def get_all_roles():
        return Role.query.all()

    @staticmethod
    def get_role_by_name(role: Roles):
        return Role.query.filter_by(name=role).first()

    @staticmethod
    def add_role(role: Role):
        db.session.add(Role)
        db.session.commit()
        return role
