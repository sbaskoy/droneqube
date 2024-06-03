
from app.schemas import db
from sqlalchemy_serializer import SerializerMixin


class DroneAssignment(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    drone_id = db.Column(db.Integer, db.ForeignKey('drone.id'), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)

    serialize_rules = ('-task.drone_assignments', '-drone.task_assignments')

    def __repr__(self):
        return f'<DroneAssignment Task:{self.task_id}, Drone:{self.drone_id}, Completed:{self.completed}>'
