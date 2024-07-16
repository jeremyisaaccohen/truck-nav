import json

from kafka import KafkaConsumer
from constants import TRAFFIC_TOPIC_NAME, BOOTSTRAP_SERVERS
import psycopg2

from google_maps import get_directions_gmaps

consumer = KafkaConsumer(TRAFFIC_TOPIC_NAME, bootstrap_servers=[BOOTSTRAP_SERVERS], auto_offset_reset='latest')

for message in consumer:
    print("new message in consumer: ", message)
    # Format the values for SQL
    try:
        print(type(message))
        vals = json.loads(message.value.decode())
        print("vals: ", vals)
        from_address = vals['from_address']
        to_address = vals['to_address']

        directions = get_directions_gmaps(from_address, to_address)
        # TODO: If inactive for a few seconds, weve exhausted consumer, print how many weve inserted.
    except:
        print(f"Error parsing {message}")
