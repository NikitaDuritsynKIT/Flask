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
    print(new_user)
    if not new_user:
        return (jsonify({"error": f"Email already exists!"}), 400)

    return (jsonify({"message": f"Registration successful!"}), 200)


# @auth_bp.route('/login', methods=['POST'])
# def login():
#     username = request.form.get('username')
#     password = request.form.get('password')

#     user = check_user_credentials(username, password)
#     if not user:
#         flash('Check your login details and try again.')
#         return redirect(url_for('auth.login'))

#     login_user(user)
#     return redirect(url_for('main.index'))

# @auth_bp.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('main.index'))
