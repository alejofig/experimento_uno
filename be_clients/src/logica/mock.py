from src.modelos.declarative_base import Base,engine, session
from src.modelos.modelos import Vendedor
from src.modelos.modelos import Cliente
import random
class Mock():
    
    def __init__(self):
        Base.metadata.create_all(engine)   
        #Este constructor contiene los datos falsos para probar la interfaz
        # self.vendedores = [
        #     {"nombre":"Alejandro"},
        #     {"nombre":"Beatriz"},
        #     {"nombre":"Daniela"},
        #     {"nombre":"Juan"}]
        # self.clientes = [{"nombre":"Roberto","zona":"chapinero","estado_cuenta":True},
        #     {"nombre":"Camilo","zona":"kennedy","estado_cuenta":True},
        #     {"nombre":"Dario","zona":"bosa","estado_cuenta":True},
        #     {"nombre":"Francisco","zona":"centro","estado_cuenta":True}]
        # for vendedor in self.vendedores:
        #     vendedor_bd = Vendedor(
        #         nombre=vendedor["nombre"]
        #     )
        #     session.add(vendedor_bd)
        #     session.commit()
        # for cliente in self.clientes:
        #     cliente_bd = Cliente(
        #         nombre=cliente["nombre"],
        #         zona = cliente["zona"],
        #         estado_cuenta = cliente["estado_cuenta"],
        #         vendedor = random.choice([v.id for v in session.query(Vendedor).all()])
        #     )
        #     session.add(cliente_bd)
        #     session.commit()
