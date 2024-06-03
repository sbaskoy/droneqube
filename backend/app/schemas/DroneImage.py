
from app.schemas import db
from sqlalchemy_serializer import SerializerMixin


class DroneImage(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    drone_id = db.Column(db.Integer, db.ForeignKey('drone.id'), nullable=False)
    folder = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Integer, nullable=False)

    # task = db.relationship("Task", back_populates="task")

    def __repr__(self):
        return f'<Image {self.folder}/{self.name}>'
