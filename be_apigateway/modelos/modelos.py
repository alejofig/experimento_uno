from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import enum

db = SQLAlchemy()


class EstadoEvento(enum.Enum):
    RECIBIDO = 1
    ERROR_AL_PROCESAR = 2
    ENVIADO = 3
    COMPLETADO = 4


class TipoEvento(enum.Enum):
    CLIENTE = 1
    PEDIDO = 2


class Evento(db.Model):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    mensaje = db.Column(db.JSON)
    numero_seguimiento = db.Column(
        db.Integer, db.ForeignKey('numero_seguimiento.id'))
    sns_message_id = db.Column(db.String)
    estado_evento = db.Column(db.Enum(EstadoEvento))
    tipo_evento = db.Column(db.Enum(TipoEvento))


class Numero_seguimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    evento = db.Column(db.Integer, db.ForeignKey('evento.id'))
    __table_args__ = (db.UniqueConstraint('evento', name='_evento_uc'),)
