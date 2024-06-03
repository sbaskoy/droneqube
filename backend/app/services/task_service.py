
from app.repositories.task_repository import TaskRepository, Task
from app.services.drone_assignment_service import DroneAssignmentService, DroneAssignment
from app.services.drone_image_service import DroneImage, DroneImageService


class TaskService:
    @staticmethod
    def get_all():
        return TaskRepository.get_all_tasks()

    @staticmethod
    def paginate(page: int = 1, per_page: int = 20):
        return TaskRepository.paginate(page=page, per_page=per_page)

    @staticmethod
    def get_task_by_id(task_id):
        return TaskRepository.get_task_by_id(task_id)

    @staticmethod
    def create_task(data):
        name = data.get("name", "")
        description = data.get("description")
        task = Task(name=name, description=description)
        TaskRepository.add_task(task)
        return task

    @staticmethod
    def update_task(task_id, data):
        task: Task = TaskRepository.get_task_by_id(task_id)
        if task:
            task.name = data.get('name', task.name)
            task.description = data.get('description', task.description)
            TaskRepository.update_task(task)
        return task

    @staticmethod
    def delete_task(task_id):
        task = TaskRepository.get_task_by_id(task_id)
        if task:
            TaskRepository.delete_task(task)
        return task

    @staticmethod
    def assign_drone(task_id: int, drone_id: int) -> DroneAssignment:
        assignment = DroneAssignmentService.find_by_drone_id_and_task_id(
            task_id=task_id, drone_id=drone_id)

        if (assignment):
            return assignment

        return DroneAssignmentService.create({"drone_id": drone_id, "task_id": task_id})

    @staticmethod
    def get_assignments(task_id):
        return DroneAssignmentService.filter_by_task(task_id=task_id)

    @staticmethod
    def get_images(task_id: int) -> list[DroneImage]:
        return DroneImageService.filter_by_task_id(task_id=task_id)
