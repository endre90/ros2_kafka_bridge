# ros2_kafka_bridge

Examples on how to make yuor ROS2-Kafka bridges.

1. Download Confluent and unpack it somewhere
2. install kafka-python with: pip3 instal kafka-python
3. Might need bson: sudo pip install pymongo
4. export PATH=/path-to-confluent/bin:$PATH
5. Make sure that you have java 1.8
6. If not java 1.8, install it and change to it with: sudo update-alternatives –config java
7. confluent start

# Examples:
An issue with ros2 launch exists for this package, so avoid ros2 launch if you see this message. Or, make a bash script for launching.
1. Joined demo:
    1. ros2 launch ros2_kafka_bridge double_kafka_pro_con
    2. ros2 launch ros2_kafka_bridge double_ros2_pub_sub
    3. ros2 launch ros2_kafka_bridge double_ros2_kafka_bridge
2. Separated demo: run all scripts w/ a 'separated' tag