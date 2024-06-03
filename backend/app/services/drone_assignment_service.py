
from app.repositories.drone_assignment_repository import DroneAssignmentRepository, DroneAssignment


class DroneAssignmentService:
    @staticmethod
    def find_by_drone_id_and_task_id(task_id: int, drone_id: int):
        return DroneAssignmentRepository.find_by_drone_id_and_task_id(task_id=task_id, drone_id=drone_id)

    @staticmethod
    def create(data) -> DroneAssignment:
        task_id = data.get("task_id")
        drone_id = data.get("drone_id")
        completed = data.get("completed", False)
        assignment = DroneAssignment(
            task_id=task_id, drone_id=drone_id, completed=completed)
        return DroneAssignmentRepository.add(assignment=assignment)

    @staticmethod
    def filter_by_task(task_id: int):
        return DroneAssignmentRepository.filter_by_task_id(task_id=task_id)

    @staticmethod
    def filter_by_drone(drone_id: int):
        return DroneAssignmentRepository.filter_by_task_id(drone_id=drone_id)
