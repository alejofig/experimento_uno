from src.modelos.declarative_base import Base,engine,session
from src.modelos.modelos import Pedido
from src.modelos.modelos import Evento
from src.modelos.modelos import Vendedor
from datetime import datetime


class DarPedido:
    def __init__(self):
        Base.metadata.create_all(engine)    

    def dar_pedidos_vendedor(self,vendedor_id: int):
        clientes = [elem.as_dict() for elem in session.query(Pedido).filter(Pedido.vendedor == vendedor_id)]
        return clientes  
    def modificar_direccion(self,message):
        pedido = session.query(Pedido).filter(Pedido.vendedor == message["vendedor"],
                                              Pedido.id == message["pedido_id"]).first()
        if pedido:
            pedido.direccion_entrega =message["direccion_entrega"]
            session.add(pedido)
            session.commit()
        return pedido.as_dict()