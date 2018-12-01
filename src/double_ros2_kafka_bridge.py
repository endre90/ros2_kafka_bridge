#!/usr/bin/env python

#----------------------------------------------------------------------------------------
# authors, description, version
#----------------------------------------------------------------------------------------
    # Endre Eres
    # ROS2-Kafka Bridge for 2 Kafka and 2 ROS2 topics: double_ros2_kafka_bridge.py
    # V.2.0.0.
#----------------------------------------------------------------------------------------

import sys
import rclpy
import time
import json
import threading
from std_msgs.msg import String
from kafka import KafkaProducer
from kafka import KafkaConsumer

class double_ros2_kafka_bridge():

    def __init__(self, args=None):

        rclpy.init(args=args)

        self.node = rclpy.create_node('single_ros2_kafka_bridge_topic_1')

        self.pub1 = self.node.create_publisher(String, 'bridge_to_ros2_topic_1')
        self.pub2 = self.node.create_publisher(String, 'bridge_to_ros2_topic_2')
        self.sub1 = self.node.create_subscription(String, '/ros2_to_bridge_topic_1', self.ros2_callback_1)
        self.sub1 = self.node.create_subscription(String, '/ros2_to_bridge_topic_2', self.ros2_callback_2)

        self.producer1 = KafkaProducer(bootstrap_servers='localhost:9092', 
                                       value_serializer=lambda m: json.dumps(m).encode('ascii'))
        
        self.producer2 = KafkaProducer(bootstrap_servers='localhost:9092', 
                                       value_serializer=lambda m: json.dumps(m).encode('ascii'))

        self.consumer1 = KafkaConsumer('kafka_to_bridge_topic_1',
                                  bootstrap_servers='localhost:9092',
                                  value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                  auto_offset_reset='latest',
                                  consumer_timeout_ms=2000)
        
        self.consumer2 = KafkaConsumer('kafka_to_bridge_topic_2',
                                  bootstrap_servers='localhost:9092',
                                  value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                  auto_offset_reset='latest',
                                  consumer_timeout_ms=2000)
                             
        self.reader1()
        self.reader2()

        rclpy.spin(self.node)
        self.node.destroy_node()
        rclpy.shutdown()

    def ros2_callback_1(self, topic_1_data):
        self.producer1.send('bridge_to_kafka_topic_1', {"data": topic_1_data.data})
        print(topic_1_data.data)

    def ros2_callback_2(self, topic_2_data):
        self.producer2.send('bridge_to_kafka_topic_2', {"data": topic_2_data.data})

    def kafka_callback_1(self, topic_1_data):
        msg = String()
        msg.data = topic_1_data["data"]
        self.pub1.publish(msg)
    
    def kafka_callback_2(self, topic_2_data):
        msg = String()
        msg.data = topic_2_data["data"]
        self.pub2.publish(msg)

    def reader1(self):
        def reader1_callback_local():
            while True:
                for message in self.consumer1:
                    self.kafka_callback_1(message.value)
        t1 = threading.Thread(target=reader1_callback_local)
        t1.daemon = True
        t1.start()
    
    def reader2(self):
        def reader2_callback_local():
            while True:
                for message in self.consumer2:
                    self.kafka_callback_2(message.value)
        t2 = threading.Thread(target=reader2_callback_local)
        t2.daemon = True
        t2.start()

if __name__ == '__main__':
    double_ros2_kafka_bridge()