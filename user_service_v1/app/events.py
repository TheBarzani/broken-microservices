import json
import pika
from shared.config.rabbitmq_config import create_channel
import os
from dotenv import load_dotenv

load_dotenv()
QUEUE_NAME = os.getenv('QUEUE_NAME')

def publish_user_update_event(user_id, email, address):
    channel, connection = create_channel(QUEUE_NAME)
    event = {
        'user_id': user_id,
        'email': email,
        'address': address,
    }
    channel.basic_publish(
        exchange='',
        routing_key=QUEUE_NAME,
        body=json.dumps(event),
        properties=pika.BasicProperties(
            delivery_mode=2,  # Make the message persistent
        )
    )
    print(f"Published event: {event}")
    connection.close()