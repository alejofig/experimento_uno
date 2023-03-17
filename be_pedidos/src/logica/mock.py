from src.modelos.declarative_base import Base,engine, session
from src.modelos.modelos import Vendedor
from src.modelos.modelos import Pedido
import random
class Mock():
    
    def __init__(self):
        Base.metadata.create_all(engine)   
        #Este constructor contiene los datos falsos para probar la interfaz
        for i in range(1,10):
            for n in range(0,2):
                self.pedidos = [{"nombre_producto":"ARROZ","direccion_entrega":"Carrera 70 #12-12"},
                    {"nombre_producto":"LENTEJAS","direccion_entrega":"Carrera 70 #12-12"},
                    {"nombre_producto":"FRIJOLES","direccion_entrega":"Carrera 70 #12-12"},
                    {"nombre_producto":"CARNE","direccion_entrega":"Carrera 70 #12-12"}]
                for pedido in self.pedidos:
                    pedido_bd = Pedido(
                        nombre_producto=pedido["nombre_producto"],
                        direccion_entrega=pedido["direccion_entrega"],
                        vendedor = i)
                    session.add(pedido_bd)
                    session.commit()
