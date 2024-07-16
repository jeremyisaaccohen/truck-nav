"""FastAPI to accept post requests and publish to kafka"""
import json

from kafka import KafkaProducer
from kafka.admin import NewTopic

from fastapi import FastAPI, Form
from fastapi import Request

from fastapi.templating import Jinja2Templates

from constants import NUM_PARTITIONS, REPLICATION_FACTOR, BOOTSTRAP_SERVERS, TRAFFIC_TOPIC_NAME

traffic_topic = NewTopic(TRAFFIC_TOPIC_NAME, num_partitions=NUM_PARTITIONS, replication_factor=REPLICATION_FACTOR)

producer = KafkaProducer(bootstrap_servers=[BOOTSTRAP_SERVERS])

app = FastAPI()

templates = Jinja2Templates(directory="templates/")

# producer.send(topic=my_topic.name, value=sample_data)
print("sent")

@app.get('/')
async def root(request: Request):
    return templates.TemplateResponse('index.html', context={'request':request})


@app.post('/')
async def post(request: Request, from_address: str = Form(...), to_address: str = Form(...)):
    print(f"jib request: {request}\njib from{ from_address} to: {to_address}")
    try:
        data = {"from_address": from_address, "to_address":to_address}

        print(data)
        dumped = json.dumps(data)
        encoded = dumped.encode('utf-8')
        print("Encoded data:", data)

        # Assuming producer is set up correctly, this is the Kafka sending part
        producer.send(traffic_topic.name, value=encoded)
        producer.flush()

        return templates.TemplateResponse('index.html', context={'request': request, 'result': f'HERE: {dumped}'})
    except Exception as e:
        print("Error occurred:", e)
        return templates.TemplateResponse('index.html', context={'request': request, 'result': f'Error: {str(e)}'})




print(producer.metrics())

