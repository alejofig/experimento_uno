import json
from src.logica.dar_cliente import DarCliente
from src.logica.mock import Mock
from src.utils import SNS
from src.modelos.modelos import TipoEvento, create_event


def create_event_and_return_message_id(message, event_type, sns_message_id):
    create_event(**{
        "mensaje": message,
        "numero_seguimiento": message["numero_seguimiento"],
        "sns_message_id": sns_message_id,
        "tipo_evento": event_type
    })


def handler(event, context):
    print(event)
    message = json.loads(event['Records'][0]['Sns']['Message'])

    create_event_and_return_message_id(
        message, TipoEvento.RECIBIDO, event['Records'][0]['Sns']['MessageId'])
    Mock()

    clientes_vendedor = DarCliente().dar_clientes_vendedor(message["vendedor_id"])
    sns_queue = SNS("us-east-1")
    message_to_send = {"numero_seguimiento": message["numero_seguimiento"],
                                  "data": clientes_vendedor}
    message_id = sns_queue.publish_message("arn:aws:sns:us-east-1:727881289392:response", json.dumps(message_to_send))
    create_event_and_return_message_id(
        message_to_send, TipoEvento.ENVIADO, message_id)
    return {"message_id": message_id}
