from flask import jsonify
from .models import db, Post
from src.users.models import User

def create_post(data, user_id):
    try:
        user = User.query.filter_by(id=user_id).first()
        data['user_id'] = user_id
        if user:
            new_post = Post(**data)
            db.session.add(new_post)
            db.session.commit()
            return jsonify({"message": "Post created!"}), 200
        return  jsonify({"error": "This user not found"}), 400
    except:
        pass
