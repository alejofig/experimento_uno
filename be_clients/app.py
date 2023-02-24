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

handler({
  "Records": [
    {
      "EventSource": "aws:sns",
      "EventVersion": "1.0",
      "EventSubscriptionArn": "arn:aws:sns:us-east-1:727881289392:api_gateway_clientes:494853e1-d7c8-4aa8-b51a-222adede5736",
      "Sns": {
        "Type": "Notification",
        "MessageId": "ef3c9372-df25-5db8-b95c-cf00e057b262",
        "TopicArn": "arn:aws:sns:us-east-1:727881289392:api_gateway_clientes",
        "Subject": "None",
        "Message": "{\"vendedor_id\":1,\"numero_seguimiento\":1}",
        "Timestamp": "2023-02-24T04:29:38.044Z",
        "SignatureVersion": "1",
        "Signature": "q1EzS8WMCKA89g5B5Jc6Ayifk6u9HB8LvzzYl2xnk8xha7126DjjJOKNNv6NQT1jScGqvrDBxRSzL8PGDaDGIw5BxZRTmAPCJ5mJ99rQCpkJHCH6FhrqWYqj9nnuN6kiFvcQ1e2gepqzc6Q0iP2Fbo00YxU5g2S0qkc6uiHgovIQD3n/i50qJcP1wRDbxgchOY3Y5UW0SQV1kFGlQ4zkyLAuCxc9Nz3PbzBnY5BIeIMBHVIwTc3/ugw41eeWz/pQy4WyRRaHzS2D/Dz8ObkZc9kMQEu3kPuQ6C26vkpVrBIFZOHS9QQp86hOJ7SsfLFNfknY5HnBO+Sh8yDke+Oh1Q==",
        "SigningCertUrl": "https://sns.us-east-1.amazonaws.com/SimpleNotificationService-56e67fcb41f6fec09b0196692625d385.pem",
        "UnsubscribeUrl": "https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:727881289392:api_gateway_clientes:494853e1-d7c8-4aa8-b51a-222adede5736",
        "MessageAttributes": {}
      }
    }
  ]
},"")
