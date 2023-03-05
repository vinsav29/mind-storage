from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
import asyncio

import json


def deserializer(serialized):
    return json.loads(serialized)


def serializer(value):
    return json.dumps(value).encode()


async def consume():
    consumer = AIOKafkaConsumer(
        'bootstrap-request',
        bootstrap_servers='localhost:9092',
        group_id="bootstrap-request-group",
        value_deserializer=deserializer,
    )
    await consumer.start()

    producer = AIOKafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=serializer,
    )
    await producer.start()

    # async def run():
    #     while True:
    #         try:
    #             print(f"Listening for messages from topics")
    #             # Consume messages
    #             data = await consumer.getmany(timeout_ms=1000)
    #             for tp, msg in data.items():
    #                 print("consumed: ", msg.topic, msg.partition, msg.offset,
    #                       msg.key, msg.value, msg.timestamp)
    #             print("after consuming")
    #             await asyncio.sleep(1)
    #         finally:
    #             # Will leave consumer group; perform autocommit if enabled.
    #             print("finally")
    try:
        while True:
            msg_batch = await consumer.getmany(timeout_ms=1000)

            for tp, msgs in msg_batch.items():
                for record in msgs:
                    if record.topic == "bootstrap-request":
                        data = {"a": 123.4, "b": "some string"}
                        await producer.send_and_wait("bootstrap-response", data)
                        print("kkinda shit")
                        # print(tp, msgs)

            # async with producer.transaction():
            #     commit_offsets = {}
            #     in_msgs = []
            #     for tp, msgs in msg_batch.items():
            #         in_msgs.extend(msgs)
            #         commit_offsets[tp] = msgs[-1].offset + 1
            #
            #     out_msgs = process_batch(in_msgs)
            #     for key, value, timestamp in out_msgs:
            #         await producer.send(
            #             OUT_TOPIC, value=value, key=key,
            #             timestamp_ms=int(timestamp * 1000)
            #         )
            #     # We commit through the producer because we want the commit
            #     # to only succeed if the whole transaction is done
            #     # successfully.
            #     await producer.send_offsets_to_transaction(
            #         commit_offsets, GROUP_ID)
    finally:
        await consumer.stop()
        await producer.stop()

if __name__ == "__main__":
    asyncio.run(consume())

