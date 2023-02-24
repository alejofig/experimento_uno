from flask_restful import Resource
from ..modelos import db, Evento, TipoEvento, EstadoEvento, Numero_seguimiento
from datetime import datetime


class VistaClients(Resource):
    def post(self, vendedor_id):
        # Enviar el mensaje a la lambda function de clientes

        # Crear el evento en la base de datos
        numero_seguimiento = Numero_seguimiento()
        db.session.add(numero_seguimiento)
        db.session.commit()

        evento = Evento(
            fecha=datetime.utcnow(),
            mensaje={'vendedor_id': vendedor_id,
                     'numero_seguimiento': numero_seguimiento.id},
            sns_message_id='123',
            numero_seguimiento=numero_seguimiento.id,
            tipo_evento=TipoEvento.CLIENTE,
            estado_evento=EstadoEvento.RECIBIDO
        )
        db.session.add(evento)
        db.session.commit()

        numero_seguimiento.evento = evento.id
        db.session.add(numero_seguimiento)
        db.session.commit()

        return {'mensaje': "Se ha recibido el evento te notificaremos cuando se haya procesado",
                "type": "clients"}


class VistaPedidos(Resource):
    def post(self, vendedor_id):
        # Enviar el mensaje a la lambda function de clientes

        # Crear el evento en la base de datos
        numero_seguimiento = Numero_seguimiento()
        db.session.add(numero_seguimiento)
        db.session.commit()

        evento = Evento(
            fecha=datetime.utcnow(),
            mensaje={'vendedor_id': vendedor_id,
                     'numero_seguimiento': numero_seguimiento.id},
            sns_message_id='123',
            numero_seguimiento=numero_seguimiento.id,
            tipo_evento=TipoEvento.PEDIDO,
            estado_evento=EstadoEvento.RECIBIDO
        )
        db.session.add(evento)
        db.session.commit()

        numero_seguimiento.evento = evento.id
        db.session.add(numero_seguimiento)
        db.session.commit()

        return {'mensaje': "Se ha recibido el evento te notificaremos cuando se haya procesado",
                "type": "pedidos"}
