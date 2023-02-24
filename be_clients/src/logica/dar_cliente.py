from src.modelos.declarative_base import Base,engine,session
from src.modelos.modelos import Cliente
from src.modelos.modelos import Evento
from src.modelos.modelos import Vendedor
from datetime import datetime


class DarCliente:
    def __init__(self):
        Base.metadata.create_all(engine)    

    def dar_clientes_vendedor(self,vendedor_id: int):
        clientes = [elem.as_dict() for elem in session.query(Cliente).filter(Cliente.vendedor == vendedor_id)]
        return clientes  
    
