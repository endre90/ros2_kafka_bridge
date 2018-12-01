#!/usr/bin/env python

#----------------------------------------------------------------------------------------
# authors, description, version
#----------------------------------------------------------------------------------------
    # Endre Eres
    # Dummy ROS2 Publisher - Subscriber example: single_ros2_pub_sub_1.py
    # V.1.0.0.
#----------------------------------------------------------------------------------------

import sys
import rclpy
import time
from std_msgs.msg import String

class single_ros2_pub_sub_1():

    def __init__(self, args=None):

        rclpy.init(args=args)

        self.msg = String()
        self.node = rclpy.create_node('single_ros2_pub_sub_1')

        self.i = 0
        self.timer_period = 1.0
        self.pub = self.node.create_publisher(String, 'ros2_to_bridge_topic_1')
        self.sub = self.node.create_subscription(String, '/bridge_to_ros2_topic_1', self.bridge_callback)
        self.tmr = self.node.create_timer(self.timer_period, self.timer_callback)

        self.node.destroy_node()
        rclpy.shutdown()

        rclpy.spin(self.node)

    def timer_callback(self):
        self.msg.data = 'ROS: Hello World A: {0}'.format(self.i)
        self.i += 1
        self.pub.publish(self.msg) 
    
    def bridge_callback(self, topic_1_data):
        self.node.get_logger().info('I heard: [%s]' % data.topic_1_data)

if __name__ == '__main__':
    try:
        single_ros2_pub_sub_1()
    except KeyboardInterrupt:
        pass