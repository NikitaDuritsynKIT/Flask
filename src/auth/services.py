from flask import jsonify
from database import db
from src.users.models import User
from flask_jwt_extended import create_access_token


def register_user(data):
    try:
        user = User.query.filter_by(email=data["email"]).first()
        if user:
            return jsonify({"error": "This email already exists"}), 400

        new_user = User(email=data["email"], name=data["name"])
        new_user.set_password(data["password"])

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Registration successful!"}), 200
    except:
        return jsonify({"error": "Something went wrong"})


def login_user(data):
    try:
        user = User.query.filter_by(email=data["email"]).first()
        if User.check_password(user, data["password"]):
            print(user.email)
            access_token = create_access_token(identity=user.email)
            return jsonify(access_token=access_token)

        return jsonify({"message": "This password not valid"}), 400
    except:
        return jsonify({"error": "Something went wrong"})
