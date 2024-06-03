

from app.schemas import db
from app.schemas.Drone import Drone


class DroneRepository:
    @staticmethod
    def get_all_drones():
        return Drone.query.all()

    @staticmethod
    def paginate(page: int, per_page: int):
        return Drone.query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def get_drone_by_id(id: int):
        return Drone.query.get(id)

    @staticmethod
    def get_drone_by_serial_number(serial_number: str):
        return Drone.query.filter_by(serial_number=serial_number).first()

    @staticmethod
    def add_drone(item: Drone):
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def update_drone(drone: Drone):
        db.session.commit()
        return drone

    @staticmethod
    def delete_drone(drone: Drone):
        db.session.delete(drone)
        db.session.commit()
        return drone
