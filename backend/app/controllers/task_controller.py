import os
from flask import jsonify, request
from app.models.app_error import AppError
from app.models.image_uploader import ImageUploader
from app.schemas.Task import Task
from app.models.min_io_uploader import MinIoUploader
from app.services.task_service import TaskService, Task
from app.utils import generate_noisy_image, serializable_array_to_json_array


class TaskController:
    @staticmethod
    def paginate():

        page = int(request.args.get('page', 1))
        per_page = int(request.args.get(
            'per_page', os.getenv("PER_PAGE_ITEM")))
        tasks = TaskService.paginate(page, per_page)
        return serializable_array_to_json_array(tasks, rules=('-drone_assignments.task', '-drone_assignments.drone_id', '-drone_assignments.task_id'))

    @staticmethod
    def create_task():
        json_data = request.get_json()
        task = TaskService.create_task(json_data)
        return jsonify(task.to_dict())

    @staticmethod
    def assign_drone(task_id: int):
        json_data = request.get_json()
        drone_id = json_data['drone_id']
        assignment = TaskService.assign_drone(
            task_id=task_id, drone_id=drone_id)
        return jsonify(assignment.to_dict(rules=('-task_id', "-drone_id")))

    @staticmethod
    def get_task_drones(task_id: int):
        assignments = TaskService.get_assignments(task_id=task_id)
        return serializable_array_to_json_array(assignments)

    @staticmethod
    def execute_task_by_id(task_id: int):
        task = TaskService.get_task_by_id(task_id=task_id)
        if not task:
            raise AppError(message="Task not found",
                           status_code=400, code="TASK_NOT_FOUND")
        images = TaskController.execute(task, MinIoUploader())
        return serializable_array_to_json_array(images)

    @staticmethod
    def execute(task: Task, uploader: ImageUploader):
        images: list = []
        for assignment in task.drone_assignments:
            image_name = f"{task.name}_{assignment.drone.name}"
            image = generate_noisy_image(640, 640, image_name)
            drone_image = uploader.upload(
                image, assignment=assignment, image_name=image_name)
            images.append(drone_image)
            print(f"{assignment.drone} execute")

        return images

    @staticmethod
    def get_task_images(task_id: int):
        images = TaskService.get_images(task_id=task_id)
        return serializable_array_to_json_array(images, rules=('-task', '-drone', '-task_id'))
