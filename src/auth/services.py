from database import db
from src.users.models import User

def register_user(name, email, password):
    user = User.query.filter_by(email=email).first()
    if user:
        return None  # Или можете вернуть ошибку

    new_user = User(email=email, name = name)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return new_user

# def get_user_by_username(username):
#     return User.query.filter_by(username=username).first()

# def check_user_credentials(username, password):
#     user = get_user_by_username(username)
#     if not user or not user.check_password(password):
#         return None
#     return user