from flask import Flask
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from database import db

#import modules
from src.users.routes import users_bp
from src.posts.routes import posts_bp
from src.auth.routes import auth_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:zxc@localhost:5432/flask'
app.config["JWT_SECRET_KEY"] = "super-secret"


db.init_app(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

#register modules
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(posts_bp, url_prefix='/posts')
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)