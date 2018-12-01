#!/usr/bin/env python

from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='ros2_kafka_bridge', node_executable='double_ros2_pub_sub', output='screen'),
        launch_ros.actions.Node(
            package='ros2_kafka_bridge', node_executable='double_kafka_pro_con', output='screen'),
        launch_ros.actions.Node(
            package='ros2_kafka_bridge', node_executable='double_ros2_kafka_bridge', output='screen')])