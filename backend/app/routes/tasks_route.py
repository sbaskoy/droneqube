

"""
    auth routes
    includes login and register endpoints

"""
from flask import Blueprint

from flask_jwt_extended import jwt_required

from app.controllers.task_controller import TaskController
from app.middlewares.validations import validate_request


from app.validations.task_schemas import CreateTaskSchema, UpdateTaskSchema, AssignDroneToTaskSchema

tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

create_task_schema = CreateTaskSchema()
update_task_Schema = UpdateTaskSchema()
assign_drone_to_task_Schema = AssignDroneToTaskSchema()


@tasks_bp.route("", methods=["GET"])
@jwt_required()
def list_task():
    return TaskController.paginate()


@tasks_bp.route("", methods=["POST"])
@validate_request(create_task_schema)
@jwt_required()
def create_task():
    return TaskController.create_task()


@tasks_bp.route("<int:task_id>/assign-drone", methods=["POST"])
@validate_request(assign_drone_to_task_Schema)
@jwt_required()
def assign_drone(task_id: int):
    return TaskController.assign_drone(task_id=task_id)


@tasks_bp.route("<int:task_id>/drones", methods=["GET"])
@jwt_required()
def drones_by_task(task_id: int):
    return TaskController.get_task_drones(task_id=task_id)


@tasks_bp.route("<int:task_id>/execute", methods=["POST"])
@jwt_required()
def execute_task(task_id: int):
    return TaskController.execute_task_by_id(task_id=task_id)


@tasks_bp.route("<int:task_id>/images", methods=["GET"])
@jwt_required()
def task_images(task_id: int):
    return TaskController.get_task_images(task_id=task_id)
