from flask import Blueprint, request, jsonify
from .services import register_user, login_user  # , get_user_by_username, check_user_credentials

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    result = register_user(data)
    return result


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    result = login_user(data)
    return result