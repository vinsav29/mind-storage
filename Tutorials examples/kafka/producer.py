from aiokafka import AIOKafkaProducer
import asyncio

import json
import time


def serializer(value):
    return json.dumps(value).encode()


async def send_one():
    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:29092',
        value_serializer=serializer,
    )
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    while True:
        time.sleep(1)
        try:
            # Produce message
            data = {"a": 123.4, "b": "some string"}
            await producer.send_and_wait("my_topic", data)
            data = [1, 2, 3, 4]
            await producer.send_and_wait("my_other_topic", data)
        finally:
            # Wait for all pending messages to be delivered or expire.
            pass
            # await producer.stop()

asyncio.run(send_one())