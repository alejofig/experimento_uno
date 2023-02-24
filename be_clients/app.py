import json
from src.logica.dar_cliente import DarCliente
from src.logica.mock import Mock
from src.utils import SNS
from src.modelos.modelos import TipoEvento, create_event


def create_event_and_return_message_id(message, event_type, sns_message_id):
    create_event({
        "mensaje": message,
        "numero_seguimiento": message["numero_seguimiento"],
        "sns_message_id": sns_message_id,
        "tipo_evento": event_type
    })


def lambda_handler(event):
    message = json.loads(event['Records'][0]['Sns']['Message'])

    create_event_and_return_message_id(
        message, TipoEvento.RECIBIDO, event['Records'][0]['Sns']['MessageId'])
    Mock()

    clientes_vendedor = DarCliente().dar_clientes_vendedor(message["vendedor_id"])
    sns_queue = SNS("us-east-1")
    message_id = sns_queue.publish_message("response", clientes_vendedor)

    create_event_and_return_message_id(
        clientes_vendedor, TipoEvento.RECEIVE_MESSAGE, message_id)

    return {"message_id": message_id}


if __name__ == "__main__":
    Mock()
    clientes_vendedor = DarCliente().dar_clientes_vendedor(vendedor_id=1)
    print(clientes_vendedor)
