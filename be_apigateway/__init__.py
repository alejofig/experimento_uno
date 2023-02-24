from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_ENDPOINT = os.getenv("DB_ENDPOINT")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

db_uri_pro = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_ENDPOINT}:{DB_PORT}/{DB_NAME}"


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri_pro

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
