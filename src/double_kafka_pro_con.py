#!/usr/bin/env python

#----------------------------------------------------------------------------------------
# authors, description, version
#----------------------------------------------------------------------------------------
    # Endre Eres
    # Dummy Kafka 2 Producer - 2 Consumer example: double_kafka_pro_con.py
    # V.2.0.0.
#----------------------------------------------------------------------------------------

import time
import json
import threading
from kafka import KafkaProducer
from kafka import KafkaConsumer

class double_kafka_pro_con():

    def __init__(self):

        time.sleep(5) # Wait for the bridge to start

        self.producer1 = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda m: json.dumps(m).encode('ascii'))
        self.producer2 = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda m: json.dumps(m).encode('ascii'))

        self.consumer1 = KafkaConsumer('bridge_to_kafka_topic_1',
                                  bootstrap_servers='localhost:9092',
                                  value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                  auto_offset_reset='latest',
                                  consumer_timeout_ms=2000)
        
        self.consumer2 = KafkaConsumer('bridge_to_kafka_topic_2',
                                  bootstrap_servers='localhost:9092',
                                  value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                  auto_offset_reset='latest',
                                  consumer_timeout_ms=2000)

        self.i = 0
        self.j = 0

        self.topic1()
        self.topic2()
        self.reader1()
        self.reader2()
        self.main()

    def topic1(self):
        def topic1_callback_local():
            while (1):
                msg = 'KAFKA: Hello World A: {0}'.format(self.i)
                self.i += 1
                self.producer1.send('kafka_to_bridge_topic_1', {"data": msg})
                time.sleep(0.7)
        t1 = threading.Thread(target=topic1_callback_local)
        t1.daemon = True
        t1.start()
    
    def topic2(self):
        def topic2_callback_local():
            while (1):
                msg = 'KAFKA: Hello World B: {0}'.format(self.j)
                self.j += 1
                self.producer2.send('kafka_to_bridge_topic_2', {"data": msg})
                time.sleep(0.5)
        t2 = threading.Thread(target=topic2_callback_local)
        t2.daemon = True
        t2.start()

    def reader1(self):
        def reader1_callback_local():
            while (1):
                for message in self.consumer1:
                    print("I heard %s", message.value)
                    break
                time.sleep(0.01)
        t3 = threading.Thread(target=reader1_callback_local)
        t3.daemon = True
        t3.start()
    
    def reader2(self):
        def reader2_callback_local():
            while (1):
                for message in self.consumer2:
                    print("I heard %s", message.value)
                    break
                time.sleep(0.01)
        t4 = threading.Thread(target=reader2_callback_local)
        t4.daemon = True
        t4.start()
    
    def main(self):
        while (1):
            pass
    
if __name__ == '__main__':
    try:
        double_kafka_pro_con()
    except KeyboardInterrupt:
        pass
