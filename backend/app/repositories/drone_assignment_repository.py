
from app.schemas import db
from app.schemas.DroneAssignment import DroneAssignment


class DroneAssignmentRepository:
    @staticmethod
    def get_all():
        return DroneAssignment.query.all()

    @staticmethod
    def filter_by_drone_id(drone_id: int):
        return DroneAssignment.query.filter_by(drone_id=drone_id)

    @staticmethod
    def filter_by_task_id(task_id: int):
        return DroneAssignment.query.filter_by(task_id=task_id)

    @staticmethod
    def find_by_drone_id_and_task_id(task_id: int, drone_id: int):
        return DroneAssignment.query.filter_by(drone_id=drone_id, task_id=task_id).first()

    @staticmethod
    def paginate(page: int, per_page: int):
        return DroneAssignment.query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def get_by_id(id: int):
        return DroneAssignment.query.get(id)

    @staticmethod
    def add(item: DroneAssignment):
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def update(item: DroneAssignment):
        db.session.commit()
        return item

    @staticmethod
    def delete(item: DroneAssignment):
        db.session.delete(item)
        db.session.commit()
        return item
