

from app.repositories.drone_repository import Drone, DroneRepository
from app.services.drone_image_service import DroneImage, DroneImageService
from app.schemas.Drone import DroneStatus
from app.utils import generate_serial_number


class DroneService:
    @staticmethod
    def get_all():
        return DroneRepository.get_all_drones()

    @staticmethod
    def paginate(page: int = 1, per_page: int = 20):
        return DroneRepository.paginate(page=page, per_page=per_page)

    @staticmethod
    def create(data) -> Drone:
        name = data.get("name", "")
        serial_number = data.get("serial_number", generate_serial_number())
        status = data.get('status', DroneStatus.Available)

        drone: Drone = Drone(
            name=name, serial_number=serial_number, status=status)

        return DroneRepository.add_drone(item=drone)

    @staticmethod
    def get_drone_images(drone_id: int) -> list[DroneImage]:
        return DroneImageService.filter_by_drone_id(drone_id=drone_id)
