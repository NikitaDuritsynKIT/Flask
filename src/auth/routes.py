from flask import Blueprint, request, jsonify
from .services import register_user  # , get_user_by_username, check_user_credentials

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data["name"]
    email = data["email"]
    password = data["password"]

    new_user = register_user(name, email, password)
    if not new_user:
        return (jsonify({"error": f"Email already exists!"}), 400)

    return (jsonify({"message": f"Registration successful!"}), 200)


@auth_bp.route("/login", methods=["POST"])
def login():
    pass

@auth_bp.route("/logout", methods=["POST"])
def logout():
    pass