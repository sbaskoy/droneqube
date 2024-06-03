
from functools import wraps
from flask import request
from flask_jwt_extended import get_jwt_identity
from marshmallow import Schema, ValidationError
from app.middlewares.error_handler import handle_validation_error
from app.models.app_error import AppError

from app.schemas.Role import Roles
from app.services.user_service import User, UserService


def validate_request(schema: Schema):
    """
    Flask route'una yapılan istekleri belirli bir Marshmallow şemasına göre doğrulamak için dekoratör.

    Bu dekoratör, istek verilerini belirli bir Marshmallow şeması ile doğrular. Eğer doğrulama başarısız olursa,
    bir ValidationError döner ve uygun bir hata mesajı ve HTTP durum kodu ile yanıt verir.

    Args:
        schema (Schema): Doğrulama için kullanılacak Marshmallow şeması.

    Returns:
        function: Orijinal fonksiyonu sararak doğrulama ekleyen dekoratör.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            json_data = request.get_json()
            try:
                schema.load(json_data)
            except ValidationError as err:
                return handle_validation_error(err)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def role_required(required_role: Roles):
    """
    Flask route'una erişim için belirli bir rol gereksinimini kontrol etmek için dekoratör.

    Bu dekoratör, JWT kullanarak kimliği doğrulanan kullanıcının belirli bir role sahip olup olmadığını kontrol eder.
    Eğer kullanıcı gerekli role sahip değilse, bir yetkilendirme hatası döner.

    Args:
        required_role (Roles): Gerekli olan rol (Roles enum değeri).

    Returns:
        function: Orijinal fonksiyonu sararak rol kontrolü ekleyen dekoratör.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_user_id = get_jwt_identity()
            user: User = UserService.get_user_by_id(id=current_user_id)
            if (user and user.role.name == Roles.Admin):
                return func(*args, **kwargs)

            if user and user.role.name == required_role:
                return func(*args, **kwargs)
            else:
                raise AppError(message="You are not authorized to access",
                               status_code=403, code="NO_PERMISSION")
        return wrapper
    return decorator
