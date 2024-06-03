

from enum import Enum
from app.schemas import db
from sqlalchemy_serializer import SerializerMixin


class DroneStatus(Enum):
    Available = "Available"
    InActive = "InActive"


class Drone(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    serial_number = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.Enum(DroneStatus),
                       nullable=False, default=DroneStatus.Available)
    task_assignments = db.relationship(
        'DroneAssignment', backref='drone', lazy=True)

    def __repr__(self):
        return f'<Drone {self.name}>'
