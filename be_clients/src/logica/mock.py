from src.modelos.declarative_base import Base,engine, session
from src.modelos.modelos import Vendedor
from src.modelos.modelos import Cliente
import random

class Mock():
    def __init__(self):
        Base.metadata.create_all(engine)   
        for i in range(0,100):
            self.clientes = [{"nombre":"Roberto","zona":"chapinero","foto_visita":"link_foto"},
                {"nombre":"Camilo","zona":"kennedy","foto_visita":"link_foto"},
                {"nombre":"Dario","zona":"bosa","foto_visita":"link_foto"},
                {"nombre":"Francisco","zona":"centro","foto_visita":"link_foto"}]
            for cliente in self.clientes:
                cliente_bd = Cliente(
                    nombre=cliente["nombre"],
                    zona = cliente["zona"],
                    foto_visita = cliente["foto_visita"],
                    vendedor = random.choice([v.id for v in session.query(Vendedor).all()])     
                )
                session.add(cliente_bd)
                session.commit()
