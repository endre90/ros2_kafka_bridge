from setuptools import setup

package_name = 'ros2_kafka_bridge'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[
        'src.single_ros2_pub_sub_1',
        'src.single_ros2_pub_sub_2',
        'src.single_kafka_pro_1',
        'src.single_kafka_pro_2',
        'src.single_kafka_con_1',
        'src.single_kafka_con_2',
        'src.single_ros2_kafka_bridge_topic_1',
        'src.single_ros2_kafka_bridge_topic_2',
        'src.double_ros2_pub_sub',
        'src.double_kafka_pro_con',
        'src.double_ros2_kafka_bridge',
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Endre Eros',
    author_email='endre@todo.com',
    maintainer='Endre Eros',
    maintainer_email='endre@todo.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='ROS2 Kafka Bridge Examples',
    license='',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'single_ros2_pub_sub_1 = src.single_ros2_pub_sub_1:single_ros2_pub_sub_1',
            'single_ros2_pub_sub_2 = src.single_ros2_pub_sub_2:single_ros2_pub_sub_2',
            'single_kafka_pro_1 = src.single_kafka_pro_1:single_kafka_pro_1',
            'single_kafka_pro_2 = src.single_kafka_pro_2:single_kafka_pro_2',
            'single_kafka_con_1 = src.single_kafka_con_1:single_kafka_con_1',
            'single_kafka_con_2 = src.single_kafka_con_2:single_kafka_con_2',
            'single_ros2_kafka_bridge_topic_1 = src.single_ros2_kafka_bridge_topic_1:single_ros2_kafka_bridge_topic_1',
            'single_ros2_kafka_bridge_topic_2 = src.single_ros2_kafka_bridge_topic_2:single_ros2_kafka_bridge_topic_2',
            'double_ros2_pub_sub = src.double_ros2_pub_sub:double_ros2_pub_sub',
            'double_kafka_pro_con = src.double_kafka_pro_con:double_kafka_pro_con',
            'double_ros2_kafka_bridge = src.double_ros2_kafka_bridge:double_ros2_kafka_bridge',
        ],
    },
)
