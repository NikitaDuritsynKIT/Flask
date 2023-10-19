from flask import Blueprint, request
from .models import db, Post
from flask_jwt_extended import jwt_required

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/create_post', methods=['POST'])
@jwt_required()
def create_post():
    
    pass

@posts_bp.route('/delete_post/<int:id>', methods=['DELETE'])
def delete_post(id):
    # Здесь код для удаления поста
    pass