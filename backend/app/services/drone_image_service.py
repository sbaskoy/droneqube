

from app.repositories.drone_image_repository import DroneImage, DroneImageRepository


class DroneImageService:
    @staticmethod
    def create(data) -> DroneImage:
        task_id = data.get("task_id")
        drone_id = data.get("drone_id")
        folder = data.get("folder")
        name = data.get("name")
        size = data.get("size")
        image = DroneImage(task_id=task_id, drone_id=drone_id,
                           folder=folder,
                           name=name,
                           size=size
                           )
        return DroneImageRepository.add_image(image)

    @staticmethod
    def filter_by_task_id(task_id: int):
        return DroneImageRepository.get_images_by_task_id(task_id=task_id)

    @staticmethod
    def filter_by_drone_id(drone_id: int):
        return DroneImageRepository.get_images_by_drone_id(drone_id=drone_id)
