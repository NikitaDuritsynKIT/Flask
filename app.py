from flask import Flask
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from database import db
from config import FLASK_RUN_PORT, config
from flask_jwt_extended import JWTManager
from flask_oidc import OpenIDConnect


# import modules
from src.users.routes import users_bp
from src.posts.routes import posts_bp
from src.auth.routes import auth_bp

app = Flask(__name__)
app.config.from_object(config["dev"])
app.secret_key = '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'

# setup extensions
db.init_app(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
jwt = JWTManager(app)
oidc = OpenIDConnect(app)

# register modules
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(posts_bp, url_prefix="/posts")
app.register_blueprint(auth_bp, url_prefix="/auth")


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=FLASK_RUN_PORT)


@app.route('/')
def index():
    if oidc.user_loggedin:
        return 'Welcome %s' % oidc.user_getfield('email')
    else:
        return 'Not logged in'

@app.route('/login')
@oidc.require_login
def login():
    return 'Welcome %s' % oidc.user_getfield('email')