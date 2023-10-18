from flask import Blueprint, request
from .models import db, Post

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/create_post', methods=['POST'])
def create_post():
    # Здесь код для создания поста
    pass

@posts_bp.route('/delete_post/<int:id>', methods=['DELETE'])
def delete_post(id):
    # Здесь код для удаления поста
    pass