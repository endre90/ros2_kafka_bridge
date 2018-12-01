#!/usr/bin/env python

#----------------------------------------------------------------------------------------
# authors, description, version
#----------------------------------------------------------------------------------------
    # Endre Eres
    # ROS2-Kafka Bridge for topic 1: single_ros2_kafka_bridge_topic_1.py
    # V.2.0.0.
#----------------------------------------------------------------------------------------

import sys
import rclpy
import time
import json
from std_msgs.msg import String
from kafka import KafkaProducer
from kafka import KafkaConsumer

class single_ros2_kafka_bridge_topic_1():

    def __init__(self, args=None):

        rclpy.init(args=args)
        
        self.msg = String()
        self.node = rclpy.create_node('single_ros2_kafka_bridge_topic_1')

        self.pub = self.node.create_publisher(String, 'bridge_to_ros2_topic_1')
        self.sub = self.node.create_subscription(String, 'ros2_to_bridge_topic_1', self.ros2_callback)

        self.producer1 = KafkaProducer(bootstrap_servers='localhost:9092', 
                                       value_serializer=lambda m: json.dumps(m).encode('ascii'))

        self.consumer1 = KafkaConsumer('kafka_to_bridge_topic_1',
                                       bootstrap_servers='localhost:9092',
                                       value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                       auto_offset_reset='latest',
                                       consumer_timeout_ms=2000)

        self.node.destroy_node()
        rclpy.shutdown()

        self.main()
        
    def ros2_callback(self, topic_1_data):
        self.producer1.send('bridge_to_kafka_topic_1', {"data": topic_1_data.data})

    def kafka_callback(self, topic_1_data):
        print(topic_1_data["data"])
        self.msg.data = topic_1_data["data"]
        self.pub.publish(self.msg)
    
    def main(self):
        while True:
            for message in self.consumer1:
                self.kafka_callback(message.value)
        rclpy.spin(self.node)

if __name__ == '__main__':
    try:
        single_ros2_kafka_bridge_topic_1()
    except KeyboardInterrupt:
        pass