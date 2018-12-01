#!/usr/bin/env python

#----------------------------------------------------------------------------------------
# authors, description, version
#----------------------------------------------------------------------------------------
    # Endre Eres
    # Dummy Kafka producer 1: single_kafka_pro_2.py
    # V.2.0.0.
#----------------------------------------------------------------------------------------

import time
import json
from kafka import KafkaProducer
from kafka import KafkaConsumer

class single_kafka_pro_2():

    def __init__(self):

        time.sleep(2) # Wait for the bridge to start

        self.producer2 = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda m: json.dumps(m).encode('ascii'))

        self.i = 0
        self.main()
    
    def main(self):
        while (1):
            msg = 'KAFKA: Hello World B: {0}'.format(self.i)
            self.i += 1
            self.producer2.send('kafka_to_bridge_topic_2', {"data": msg})
            time.sleep(0.04)
    
if __name__ == '__main__':
    try:
        single_kafka_pro_2()
    except KeyboardInterrupt:
        pass
