

from flask import jsonify
from marshmallow import ValidationError
from app.models.app_error import AppError


def handle_error(error, status_code):
    """
    Genel hata işleyici.

    Bu işlev, yakalanan herhangi bir hatayı alır ve standart bir hata yanıtı oluşturur.

    Args:
        error (Exception): Yakalanan hata nesnesi.
        status_code (int): HTTP durum kodu.

    Returns:
        tuple: JSON formatında hata yanıtı ve HTTP durum kodu.
    """
    response = {
        "error": {
            "message": str(error),
            "type": error.__class__.__name__,
            "status_code": status_code
        }
    }
    return jsonify(response), status_code


def handle_app_error(error: AppError,):
    """
    Özel AppError hata işleyici.

    Bu işlev, yakalanan AppError nesnesini alır ve standart bir hata yanıtı oluşturur.

    Args:
        error (AppError): Yakalanan AppError nesnesi.

    Returns:
        tuple: JSON formatında hata yanıtı ve HTTP durum kodu.
    """
    response = {
        "error": {
            "message": str(error.message),
            "type": error.code,
            "status_code": error.status_code
        }
    }
    return jsonify(response), error.status_code


def handle_validation_error(err: ValidationError):
    """
    Doğrulama hatası işleyici.

    Bu işlev, Marshmallow tarafından yakalanan doğrulama hatalarını alır ve standart bir hata yanıtı oluşturur.

    Args:
        err (ValidationError): Yakalanan doğrulama hatası nesnesi.

    Returns:
        tuple: JSON formatında hata yanıtı ve HTTP durum kodu.
    """
    response = {
        "error": {
            "message": err.messages,
            "type": "ValidationError",
            "status_code": 400
        }
    }
    return jsonify(response), 400
