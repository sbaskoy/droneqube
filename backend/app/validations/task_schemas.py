
from marshmallow import Schema, fields


class CreateTaskSchema(Schema):
    name = fields.String(required=True, validate=lambda x: len(x) >= 4)
    description = fields.String(required=True, validate=lambda x: len(x) >= 6)


class UpdateTaskSchema(Schema):
    name = fields.String(required=False, validate=lambda x: len(x) >= 4)
    description = fields.String(required=False, validate=lambda x: len(x) >= 6)


class AssignDroneToTaskSchema(Schema):
    drone_id = fields.Number(required=True)
