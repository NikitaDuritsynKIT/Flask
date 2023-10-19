from flask import Blueprint, request
from .services import create_post
from flask_jwt_extended import jwt_required
posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/create_post/<int:user_id>', methods=['POST'])
@jwt_required()
def create(user_id):
    data = request.get_json()
    result = create_post(data, user_id)
    return result