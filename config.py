import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
FLASK_RUN_PORT = int(os.environ.get("FLASK_RUN_PORT"))


class Config:
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


config = {
    "dev": DevConfig,
    "prod": ProdConfig,
}
