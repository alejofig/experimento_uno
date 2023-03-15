from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import enum

db = SQLAlchemy()


class EstadoEvento(enum.Enum):
    RECIBIDO = 1
    ERROR_AL_PROCESAR = 2
    ENVIADO = 3
    COMPLETADO = 4


class TipoSolicitud(enum.Enum):
    CLIENTE = 1
    PEDIDO = 2

class Vendedor(db.Model):  

    __tablename__ = "vendedor_ag"

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50))
    identificacion = db.Column(db.Integer, nullable=True)
    contrasena = db.Column(db.String(50))

class Evento(db.Model):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    __tablename__ = 'evento_ag'

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    mensaje = db.Column(db.JSON)
    numero_seguimiento = db.Column(
        db.Integer, db.ForeignKey('numero_seguimiento_ag.id'))
    sns_message_id = db.Column(db.String)
    estado_evento = db.Column(db.Enum(EstadoEvento))
    tipo_evento = db.Column(db.Enum(TipoSolicitud))


class Numero_seguimiento(db.Model):
    __tablename__ = 'numero_seguimiento_ag'
    id = db.Column(db.Integer, primary_key=True)
    evento = db.Column(db.Integer, db.ForeignKey('evento_ag.id'))
