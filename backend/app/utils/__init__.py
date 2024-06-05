

from PIL import Image, ImageDraw, ImageFont
import random
import string

from flask import jsonify

from app.models.app_error import AppError
from sqlalchemy_serializer import SerializerMixin
from app.schemas.Role import Roles


def string_to_enum(string_value, enum_cls):
    for enum_member in enum_cls:
        if string_value in enum_member.value:
            return enum_member
    raise AppError(
        f"'{string_value}' değeri enum'da bulunamadı.", 400, "STATUS_NOT_FOUND")


def generate_serial_number(length=16):
    characters = string.ascii_letters + string.digits

    serial_number = ''.join(random.choice(characters) for _ in range(length))

    return serial_number


def serializable_array_to_json_array(items: list[SerializerMixin], rules=None):
    return jsonify([item.to_dict(rules=rules) for item in items])


def generate_noisy_image(width: int, height: int, text: str = "") -> Image:
    import numpy as np
    from PIL import Image

    noise = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
    noisy_image = Image.fromarray(noise)

    draw = ImageDraw.Draw(noisy_image)

    font = ImageFont.load_default(size=50)

    _, _, text_width, text_height = draw.textbbox((0, 0), text, font=font)

    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    fill_color = (0, 0, 0)
    draw.text((text_x, text_y), text, font=font, fill=fill_color)

    return noisy_image


def create_default_roles():
    from app.services.role_services import RoleService
    existing_roles = RoleService.get_all()
    if not existing_roles:
        RoleService.create_if_not_exists({"name": "Admin"})
        RoleService.create_if_not_exists({"name": "User"})
        print("Default roles craeted")


def create_default_user():
    import os
    username = os.getenv("DEFAULT_USER_USERNAME")
    password = os.getenv("DEFAULT_USER_PASSWORD")
    name = os.getenv("DEFAULT_USER_NAME")
    last_name = os.getenv("DEFAULT_USER_LAST_NAME")
    if (not username or not password or not name or not last_name):
        print("default user not created")
        return
    from app.services.user_service import UserService

    default_user = UserService.find_by_username(username=username)
    if (not default_user):
        UserService.create({
            "username": username,
            "password": password,
            "name": name,
            "last_name": last_name,
            "role": "Admin"
        })
        print("default user created")
