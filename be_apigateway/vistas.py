import hashlib
from flask_restful import Resource
from modelos.modelos import db, Evento, TipoSolicitud, EstadoEvento, Numero_seguimiento, Vendedor
from datetime import datetime
from mensajeria.utils import SNS
import json
from flask import request
from flask_jwt_extended import jwt_required, create_access_token
import os

def is_valid(api_key):
    if api_key == os.getenv("API_KEY"):
        return True



class VistaLogIn(Resource):

    def post(self):
        contrasena_encriptada = hashlib.md5(
            request.json["contrasena"].encode('utf-8')).hexdigest()
        usuario = Vendedor.query.filter(Vendedor.usuario == request.json["usuario"],
                                       Vendedor.contrasena == contrasena_encriptada).first()
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            token_de_acceso = create_access_token(identity=usuario.id)
            return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso, "id": usuario.id}

class VistaSignIn(Resource):

    def post(self):
        usuario = Vendedor.query.filter(
            Vendedor.usuario == request.json["usuario"]).first()
        if usuario is None:
            contrasena_encriptada = hashlib.md5(
                request.json["contrasena"].encode('utf-8')).hexdigest()
            nuevo_usuario = Vendedor(
                usuario=request.json["usuario"], contrasena=contrasena_encriptada)
            db.session.add(nuevo_usuario)
            db.session.commit()
            # token_de_acceso = create_access_token(identity=nuevo_usuario.id)
            return {"mensaje": "usuario creado exitosamente", "id": nuevo_usuario.id}
        else:
            return "El usuario ya existe", 404

class VistaClients(Resource):

    @jwt_required()
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

    @jwt_required()
    def post(self, vendedor_id):
        topico = 'arn:aws:sns:us-east-1:727881289392:api_gateway_pedidos'
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
                tipo_evento=TipoSolicitud.PEDIDO,
                estado_evento=EstadoEvento.ENVIADO
            )
            db.session.add(evento_enviado)
            db.session.commit()

            return {'mensaje': "Se ha recibido el evento te notificaremos cuando se haya procesado",
                    "type": "pedidos"}

        return {"mensaje": "No se ha podido enviar el evento", "type": "clients"}

        r


class VistaResponse(Resource):
    def post(self):
        if request.json:
            api_key = request.json.get("api_key")
        else:
            return {"message": "Please provide an API key"}, 400
        
        if is_valid(api_key):
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
                numero_seguimiento=numero_seguimiento.id,
                tipo_evento=evento_asociado.tipo_evento,
                estado_evento=EstadoEvento.COMPLETADO,
            )
            db.session.add(evento)
            db.session.commit()

            return {"mensaje": "Se ha recibido el evento correctamente desde el backend", "type": "response"}
        else:
            return {"message": "The provided API key is not valid"}, 403