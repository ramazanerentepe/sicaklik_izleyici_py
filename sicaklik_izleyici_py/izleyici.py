import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class IzleyiciNode(Node):
    def __init__(self):
        super().__init__('izleyici')
        # Bonus: esik degeri parametre (varsayilan 30.0)
        self.declare_parameter('esik', 30.0)
        self.subscription = self.create_subscription(
            Float32, 'sicaklik', self.sicaklik_callback, 10)
        self.get_logger().info('Izleyici dugumu basladi.')

    def sicaklik_callback(self, msg):
        esik = self.get_parameter('esik').value
        if msg.data > esik:
            self.get_logger().warn(
                f'UYARI! Sicaklik yuksek: {msg.data:.2f} C (esik: {esik})')
        else:
            self.get_logger().info(f'Sicaklik: {msg.data:.2f} C')


def main(args=None):
    rclpy.init(args=args)
    node = IzleyiciNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == '__main__':
    main()
