

from app.schemas import db
from app.schemas.DroneImage import DroneImage


class DroneImageRepository:
    @staticmethod
    def get_all_images():
        return DroneImage.query.all()

    @staticmethod
    def get_images_by_task_id(task_id: int):
        return DroneImage.query.filter_by(task_id=task_id)

    @staticmethod
    def get_images_by_drone_id(drone_id: int):
        return DroneImage.query.filter_by(drone_id=drone_id)

    @staticmethod
    def add_image(image: DroneImage):
        db.session.add(image)
        db.session.commit()

    @staticmethod
    def delete_user(image: DroneImage):
        db.session.delete(image)
        db.session.commit()
