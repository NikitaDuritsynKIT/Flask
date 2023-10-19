from flask import Blueprint, request
from .models import db, User

users_bp = Blueprint("users", __name__)

@users_bp.route("/delete_user/<int:id>", methods=["DELETE"])
def delete_user(id):
    # Здесь код для удаления пользователя
    pass
