

from PIL import Image, ImageDraw, ImageFont
import random
import string

from flask import jsonify

from app.models.app_error import AppError
from sqlalchemy_serializer import SerializerMixin


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
