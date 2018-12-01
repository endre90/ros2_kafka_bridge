#!/usr/bin/env python

from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='ros2_kafka_bridge', node_executable='single_kafka_con_1', output='screen'),
        launch_ros.actions.Node(
            package='ros2_kafka_bridge', node_executable='single_kafka_con_2', output='screen'),
        launch_ros.actions.Node(
            package='ros2_kafka_bridge', node_executable='single_kafka_pro_1', output='screen'),
        launch_ros.actions.Node(
            package='ros2_kafka_bridge', node_executable='single_kafka_pro_2', output='screen'),
        launch_ros.actions.Node(
            package='ros2_kafka_bridge', node_executable='single_ros2_pub_sub_1', output='screen'),
        launch_ros.actions.Node(
            package='ros2_kafka_bridge', node_executable='single_ros2_pub_sub_2', output='screen'),
        launch_ros.actions.Node(
            package='ros2_kafka_bridge', node_executable='single_ros2_kafka_bridge_topic_1', output='screen'),
        launch_ros.actions.Node(
            package='ros2_kafka_bridge', node_executable='single_ros2_kafka_bridge_topic_2', output='screen')])