import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor')
        self.publisher_ = self.create_publisher(Float32, 'sicaklik', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Sensor dugumu basladi.')

    def timer_callback(self):
        msg = Float32()
        msg.data = random.uniform(20.0, 40.0)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Yayinlanan sicaklik: {msg.data:.2f} C')


def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
