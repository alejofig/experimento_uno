from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String, Boolean, Enum, JSON
from datetime import datetime
import enum

from src.modelos.declarative_base import Base, session


class Pedido(Base):  # To do
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    __tablename__ = 'pedido'
    id = Column(Integer, primary_key=True)
    nombre_producto = Column(String)
    vendedor = Column(Integer, ForeignKey('vendedor.id'))
    direccion_entrega = Column(String)


class TipoEvento(enum.Enum):
    RECIBIDO = 1
    ERROR_AL_PROCESAR = 2
    ENVIADO = 3


class Evento(Base):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    __tablename__ = 'evento'
    id = Column(Integer, primary_key=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    mensaje = Column(JSON)
    numero_seguimiento = Column(Integer)
    sns_message_id = Column(String)
    tipo_evento = Column(Enum(TipoEvento))


class Vendedor(Base):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    __tablename__ = 'vendedor'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)


def create_event(**kwargs):
    evento = Evento(
        mensaje=kwargs["mensaje"],
        numero_seguimiento=kwargs["numero_seguimiento"],
        sns_message_id=kwargs["sns_message_id"],
        tipo_evento=kwargs["tipo_evento"],
    )
    session.add(evento)
    session.commit()
