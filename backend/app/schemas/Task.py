

from app.models.image_uploader import ImageUploader
from app.schemas import db
from sqlalchemy_serializer import SerializerMixin
from app.schemas.DroneImage import DroneImage

from app.utils import generate_noisy_image


class Task(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    drone_assignments = db.relationship(
        'DroneAssignment', backref='task', lazy=True)

    # drone_images = db.relationship('DroneImage', backref='task', lazy=True)

    def __repr__(self):
        return f'<Task {self.name}>'

    def execute(self, uploader: ImageUploader):
        images: list = []
        for assignment in self.drone_assignments:
            image_name = f"{self.name}_{assignment.drone.name}"
            image = generate_noisy_image(640, 640, image_name)
            drone_image = uploader.upload(
                image, assignment=assignment, image_name=image_name)
            images.append(drone_image)
            print(f"{assignment.drone} execute")

        return images
