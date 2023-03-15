from flask_restful import Api
from vistas import VistaClients, VistaPedidos, VistaResponse, VistaLogIn,VistaSignIn
import serverless_wsgi
from modelos.modelos import db
from flask_jwt_extended import JWTManager

from flask import Flask
from dotenv import load_dotenv
import os


def create_app(config_name):
    application = Flask(__name__)
    application.config['SQLALCHEMY_DATABASE_URI'] = db_uri_pro

    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return application


load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_ENDPOINT = os.getenv("DB_ENDPOINT")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

db_uri_pro = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_ENDPOINT}:{DB_PORT}/{DB_NAME}"

app = create_app('default')
app.config["JWT_ALGORITHM"] = "HS256"
app_context = app.app_context()
app_context.push()
app.config['JWT_SECRET_KEY'] = 'frase-secreta'

db.init_app(app)
db.create_all()
jwt = JWTManager(app)
api = Api(app)
api.add_resource(VistaClients, '/v1/clients/<int:vendedor_id>')
api.add_resource(VistaPedidos, '/v1/pedidos/<int:vendedor_id>')
api.add_resource(VistaResponse, '/v1/response')
api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/login')


def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
