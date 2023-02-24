import boto3


class SNS:
    def __init__(self, region_name, aws_access_key_id=None, aws_secret_access_key=None):
        self.client = boto3.client(
            'sns',
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

    def publish_message(self, topic_arn, message):
        response = self.client.publish(TopicArn=topic_arn, Message=message)
        message_id = response['MessageId']
        return message_id
