import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
PORT = os.environ.get("PORT")
FLASK_RUN_PORT = int(PORT)



class Config:
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
    OIDC_CLIENT_SECRETS = 'client_secrets.json'

    # GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    # GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
    # GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
    # OIDC_COOKIE_SECURE = False
    # OIDC_CALLBACK_ROUTE = '/oidc/callback'
    # OIDC_CALLBACK_ROUTE = ['openid', 'email', 'profile']


class DevConfig(Config):
    OIDC_COOKIE_SECURE = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


class ProdConfig(Config):
    OIDC_COOKIE_SECURE = False
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


config = {
    "dev": DevConfig,
    "prod": ProdConfig,
}
