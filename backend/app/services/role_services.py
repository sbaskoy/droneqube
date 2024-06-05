

from app.repositories.role_repository import Role, RoleRepository, Roles


class RoleService:
    @staticmethod
    def get_all():
        return RoleRepository.get_all_roles()

    @staticmethod
    def get_role_by_name(role: Roles):
        return RoleRepository.get_role_by_name(role=role)

    @staticmethod
    def create_if_not_exists(data) -> Role:
        name = data.get("name")
        role = RoleService.get_role_by_name(role=name)
        if not role:
            role = Role(name=name)
            return RoleRepository.add_role(role=role)
        return role
