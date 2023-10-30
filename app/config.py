import asyncio

#env variable
KAFKA_BOOTSTRAP_SERVERS= "localhost:9093"
KAFKA_TOPIC="kafka"
KAFKA_CONSUMER_GROUP="group_id"
loop =asyncio.get_event_loop()