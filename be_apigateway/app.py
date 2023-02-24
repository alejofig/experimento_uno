from be_apigateway import create_app
from .modelos import db
from flask_restful import Api
from .vistas import VistaClients, VistaPedidos


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaClients, '/v1/clients/<int:vendedor_id>')
api.add_resource(VistaPedidos, '/v1/pedidos/<int:vendedor_id>')
