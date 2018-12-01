#!/usr/bin/env python

#----------------------------------------------------------------------------------------
# authors, description, version
#----------------------------------------------------------------------------------------
    # Endre Eres
    # Dummy ROS2 2 Publisher - 2 Subscriber example: double_ros2_pub_sub.py
    # V.1.0.0.
#----------------------------------------------------------------------------------------

import sys
import rclpy
import time
import threading
from std_msgs.msg import String

class double_ros2_pub_sub():

    def __init__(self, args=None):

        rclpy.init(args=args)

        self.node = rclpy.create_node('double_ros2_pub_sub')

        time.sleep(2) # Wait for the bridge to start

        self.i1 = 0
        self.i2 = 0
        self.timer_period_1 = 0.2
        self.timer_period_2 = 0.3
        self.pub1 = self.node.create_publisher(String, 'ros2_to_bridge_topic_1')
        self.pub2 = self.node.create_publisher(String, 'ros2_to_bridge_topic_2')
        self.sub1 = self.node.create_subscription(String, '/bridge_to_ros2_topic_1', self.bridge_callback_1)
        self.sub2 = self.node.create_subscription(String, '/bridge_to_ros2_topic_2', self.bridge_callback_2)
        self.tmr1 = self.node.create_timer(self.timer_period_1, self.timer_callback_1)
        self.tmr2 = self.node.create_timer(self.timer_period_2, self.timer_callback_2)

        rclpy.spin(self.node)
        self.node.destroy_node()
        rclpy.shutdown()

    def timer_callback_1(self):
        msg = String()
        msg.data = 'ROS: Hello World A: {0}'.format(self.i1)
        self.i1 += 1
        self.pub1.publish(msg) 

    def timer_callback_2(self):
        msg = String()
        msg.data = 'ROS: Hello World B: {0}'.format(self.i2)
        self.i2 += 1
        self.pub2.publish(msg) 
    
    def bridge_callback_1(self, topic_1_data):
        self.node.get_logger().info('I heard: [%s]' % topic_1_data.data)

    def bridge_callback_2(self, topic_2_data):
        self.node.get_logger().info('I heard: [%s]' % topic_2_data.data)

if __name__ == '__main__':
    double_ros2_pub_sub()