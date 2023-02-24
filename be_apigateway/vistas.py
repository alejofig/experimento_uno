from flask_restful import Resource
from modelos.modelos import db, Evento, TipoSolicitud, EstadoEvento, Numero_seguimiento
from datetime import datetime
from mensajeria.utils import SNS
import json
from flask import request


class VistaClients(Resource):
    def post(self, vendedor_id):
        topico = 'arn:aws:sns:us-east-1:727881289392:api_gateway_clientes'
        # Crear el evento en la base de datos
        numero_seguimiento = Numero_seguimiento()
        db.session.add(numero_seguimiento)
        db.session.commit()

        evento = Evento(
            fecha=datetime.utcnow(),
            mensaje={'vendedor_id': vendedor_id,
                     'numero_seguimiento': numero_seguimiento.id},
            sns_message_id='_',
            numero_seguimiento=numero_seguimiento.id,
            tipo_evento=TipoSolicitud.CLIENTE,
            estado_evento=EstadoEvento.RECIBIDO
        )
        db.session.add(evento)
        db.session.commit()

        numero_seguimiento.evento = evento.id
        db.session.add(numero_seguimiento)
        db.session.commit()

        # Enviar el mensaje a la lambda function de clientes
        message_id = SNS(
            region_name='us-east-1').publish_message(topico, json.dumps(evento.mensaje))

        if bool(message_id):
            evento_enviado = Evento(
                fecha=datetime.utcnow(),
                mensaje={'vendedor_id': vendedor_id,
                         'state': 'Evento enviado por mensaje'},
                sns_message_id=message_id,
                numero_seguimiento=numero_seguimiento.id,
                tipo_evento=TipoSolicitud.CLIENTE,
                estado_evento=EstadoEvento.ENVIADO
            )
            db.session.add(evento_enviado)
            db.session.commit()

            return {'mensaje': "Se ha recibido el evento te notificaremos cuando se haya procesado",
                    "type": "clients"}

        return {"mensaje": "No se ha podido enviar el evento", "type": "clients"}


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
            sns_message_id='_',
            numero_seguimiento=numero_seguimiento.id,
            tipo_evento=TipoSolicitud.PEDIDO,
            estado_evento=EstadoEvento.RECIBIDO
        )
        db.session.add(evento)
        db.session.commit()

        numero_seguimiento.evento = evento.id
        db.session.add(numero_seguimiento)
        db.session.commit()

        return {'mensaje': "Se ha recibido el evento te notificaremos cuando se haya procesado",
                "type": "pedidos"}


class VistaResponse(Resource):
    def post(self):
        # Recibir el mensaje de la lambda function de clientes
        numero_seguimiento_id = request.json['numero_seguimiento']

        # Obtener numero seguimiento
        numero_seguimiento = Numero_seguimiento.query.filter_by(
            id=numero_seguimiento_id).first()
        # obtener evento asociado
        evento_asociado = Evento.query.filter_by(
            id=numero_seguimiento.evento).first()

        evento = Evento(
            fecha=datetime.utcnow(),
            mensaje=request.json['data'],
            sns_message_id='_',
            tipo_evento=evento_asociado.tipo_evento,
            estado_evento=EstadoEvento.COMPLETADO,
        )
        db.session.add(evento)
        db.session.commit()

        return {"mensaje": "Se ha recibido el evento correctamente desde el backend", "type": "response"}
