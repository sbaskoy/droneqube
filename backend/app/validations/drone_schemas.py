
from marshmallow import Schema, fields

from app.schemas.Drone import DroneStatus


class CreateDroneSchema(Schema):
    name = fields.String(required=True, validate=lambda x: len(x) >= 4)
    serial_number = fields.String(
        required=False, validate=lambda x: len(x) >= 4)
    status = fields.Enum(DroneStatus, required=False)


class UpdateDroneSchema(Schema):
    name = fields.String(required=False, validate=lambda x: len(x) >= 4)
    serial_number = fields.String(
        required=False, validate=lambda x: len(x) >= 4)
    status = fields.Enum(DroneStatus, required=False)


class AssignDroneToTaskSchema(Schema):
    drone_id = fields.Number(required=True)
