# truck-nav
GPS or static route generation for commercial vehicles

### Setup

poetry install --no-root     

`cd Downloads/kafka/kafka_2.13-3.7.0/`

Start the ZooKeeper service 

`$ bin/zookeeper-server-start.sh config/zookeeper.properties`

And in another terminal, start the Kafka broker service:

`$ bin/kafka-server-start.sh config/server.properties`

`fastapi run [FILE].py --reload`

reload flag useful for live reloads of changes in src