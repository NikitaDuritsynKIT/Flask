from flask import Blueprint, request, jsonify
from .services import register_user  # , get_user_by_username, check_user_credentials
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

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
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    
    # validation
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


# @auth_bp.route("/logout", methods=["POST"])
# def logout():
#     pass