

from flask import jsonify, request
from app.models.app_error import AppError
from app.schemas.Drone import Drone, DroneStatus
from app.schemas import db
from app.schemas.DroneImage import DroneImage
from app.services.drone_service import DroneService, Drone
from app.utils import serializable_array_to_json_array


class DroneController:
    @staticmethod
    def paginate():
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        drones = DroneService.paginate(page, per_page)
        return serializable_array_to_json_array(drones,
                                                rules=("-task_assignments.drone", '-task_assignments.task_id', '-task_assignments.drone_id'))

    @staticmethod
    def create_drone():
        json_data = request.get_json()
        drone = DroneService.create(json_data)
        return jsonify(drone.to_dict())

    @staticmethod
    def drone_images(drone_id: int):
        images = DroneService.get_drone_images(drone_id=drone_id)
        return serializable_array_to_json_array(images, rules=('-task', '-drone', '-drone_id'))
