#!/usr/bin/env python

#----------------------------------------------------------------------------------------
# authors, description, version
#----------------------------------------------------------------------------------------
    # Endre Eres
    # Dummy Kafka consumer: single_kafka_con_1.py
    # V.2.0.0.
#----------------------------------------------------------------------------------------

import time
import json
from kafka import KafkaProducer
from kafka import KafkaConsumer

class single_kafka_con_1():

    def __init__(self):

        time.sleep(2) # Wait for the bridge to start

        self.consumer1 = KafkaConsumer('bridge_to_kafka_topic_1',
                                  bootstrap_servers='localhost:9092',
                                  value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                  auto_offset_reset='latest',
                                  consumer_timeout_ms=2000)

        self.i = 0
        self.main()
    
    def main(self):
        while (1):
            for message in self.consumer1:
                print("I heard %s", message.value)
    
if __name__ == '__main__':
    try:
        single_kafka_con_1()
    except KeyboardInterrupt:
        pass
