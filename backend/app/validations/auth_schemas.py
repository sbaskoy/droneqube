from marshmallow import Schema, fields


class LoginSchema(Schema):
    username = fields.String(
        required=True, validate=lambda x: 4 <= len(x) <= 25)
    password = fields.String(required=True, validate=lambda x: len(x) >= 6)


class RegisterSchema(Schema):
    username = fields.String(
        required=True, validate=lambda x: 4 <= len(x) <= 25)
    password = fields.String(required=True, validate=lambda x: len(x) >= 6)
    name = fields.String(required=True)
    last_name = fields.String(required=True)
    role = fields.String(required=True)
