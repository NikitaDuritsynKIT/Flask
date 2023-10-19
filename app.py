from flask import Flask
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from database import db
from config import FLASK_RUN_PORT, config

from flask_jwt_extended import JWTManager


# import modules
from src.users.routes import users_bp
from src.posts.routes import posts_bp
from src.auth.routes import auth_bp

app = Flask(__name__)
app.config.from_object(config["dev"])


# setup extensions
jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

# register modules
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(posts_bp, url_prefix="/posts")
app.register_blueprint(auth_bp, url_prefix="/auth")


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=FLASK_RUN_PORT)
