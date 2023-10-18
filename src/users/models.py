from database import db
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash

@dataclass
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    # Другие поля, если они есть...
    posts = db.relationship("Post", backref="author", lazy="dynamic")

    def set_password(self, password):
        self.password = generate_password_hash(password, method='pbkdf2')

    def check_password(self, password):
        return check_password_hash(self.password, password)
    