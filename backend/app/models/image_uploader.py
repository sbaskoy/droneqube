

from abc import ABC, abstractmethod
from PIL import Image
from app.schemas.DroneAssignment import DroneAssignment

from app.schemas.DroneImage import DroneImage


class ImageUploader(ABC):
    @abstractmethod
    def upload(self, im: Image, assignment: DroneAssignment, image_name: str) -> DroneImage:
        pass
