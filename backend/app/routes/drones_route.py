

""" 
    auth routes
    includes login and register endpoints

"""
from flask import Blueprint,  Flask
from flask_jwt_extended import jwt_required

from app.middlewares.validations import validate_request, role_required
from app.schemas.Role import Roles

from app.validations.drone_schemas import CreateDroneSchema, UpdateDroneSchema
from app.controllers.drone_controller import DroneController

drones_bp = Blueprint("drones", __name__, url_prefix="/drones")

create_drone_schema = CreateDroneSchema()
update_update_Schema = UpdateDroneSchema()


@drones_bp.route("/", methods=["GET"])
@jwt_required()
@role_required(Roles.User)
def list_drones():
    return DroneController.paginate()


@drones_bp.route("/", methods=["POST"])
@validate_request(create_drone_schema)
@jwt_required()
def create_drone():
    return DroneController.create_drone()


@drones_bp.route("<int:drone_id>/images", methods=["GET"])
@jwt_required()
def drone_images(drone_id: int):
    return DroneController.drone_images(drone_id=drone_id)
