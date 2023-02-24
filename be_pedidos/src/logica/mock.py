from src.modelos.declarative_base import Base,engine, session
from src.modelos.modelos import Vendedor
from src.modelos.modelos import Pedido
import random
class Mock():
    
    def __init__(self):
        Base.metadata.create_all(engine)   
        #Este constructor contiene los datos falsos para probar la interfaz
        self.vendedores = [
            {"nombre":"Alejandro"},
            {"nombre":"Beatriz"},
            {"nombre":"Daniela"},
            {"nombre":"Juan"}]
        self.pedidos = [{"nombre_producto":"ARROZ"},
            {"nombre_producto":"LENTEJAS"},
            {"nombre_producto":"FRIJOLES"},
            {"nombre_producto":"CARNE"}]
        for vendedor in self.vendedores:
            vendedor_bd = Vendedor(
                nombre=vendedor["nombre"]
            )
            session.add(vendedor_bd)
            session.commit()
        for pedido in self.pedidos:
            pedido_bd = Pedido(
                nombre_producto=pedido["nombre_producto"],
                vendedor = random.choice([v.id for v in session.query(Vendedor).all()])
            )
            session.add(pedido_bd)
            session.commit()
