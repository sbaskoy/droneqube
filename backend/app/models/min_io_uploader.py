
import os
from minio import Minio
from PIL import Image
import tempfile
from datetime import datetime
from app.models.image_uploader import ImageUploader
from app.schemas.DroneImage import DroneImage
from app.schemas.DroneAssignment import DroneAssignment
from app.schemas import db

from app.utils import generate_noisy_image


MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
MINIO_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME")


class MinIoUploader(ImageUploader):

    def __init__(self) -> None:
        super().__init__()
        self.client = Minio(MINIO_ENDPOINT,
                            access_key=MINIO_ACCESS_KEY,
                            secret_key=MINIO_SECRET_KEY,
                            )

    def create_bucket_to_min_io(self, bucket_name: str):
        found = self.client.bucket_exists(bucket_name=bucket_name)
        if not found:
            self.client.make_bucket(bucket_name)

    def save_image_to_database(self, assignment: DroneAssignment, image_size: int, image_name: int, folder: str):
        drone_image = DroneImage(task_id=assignment.task_id, drone_id=assignment.drone_id,
                                 folder=folder,
                                 name=image_name,
                                 size=image_size
                                 )
        db.session.add(drone_image)
        db.session.commit()
        return drone_image

    def upload(self, im: Image, assignment: DroneAssignment, image_name: str):
        self.create_bucket_to_min_io(MINIO_BUCKET_NAME)
        current_time = datetime.now()

        formatted_time = current_time.strftime('%Y%m%d_%H%M%S')
        drone_name = assignment.drone.name
        object_name = f"{drone_name}/{image_name}_{formatted_time}.jpg"

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        temp_file_path = temp_file.name

        im.save(temp_file_path)
        im_size = os.path.getsize(temp_file_path)
        self.client.put_object(
            bucket_name=MINIO_BUCKET_NAME,
            object_name=object_name,
            data=open(temp_file_path, 'rb'),
            length=im_size,
            content_type='image/jpeg',
        )
        return self.save_image_to_database(
            assignment, im_size, object_name, drone_name)

    def upload_test_image(self):
        im = generate_noisy_image(640, 640)
        self.upload(im, "test_drone", "test_image")
        print("Image uploaded")
