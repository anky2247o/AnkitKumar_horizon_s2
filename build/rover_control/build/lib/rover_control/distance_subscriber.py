import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class DistanceSubscriber(Node):

    def _init_(self):
        super()._init_('distance_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            '/distance',
            self.listener_callback,
            10
        )
        self.get_logger().info('Distance Subscriber node started...')

    def listener_callback(self, msg):
        self.get_logger().info(f'Received distance: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = DistanceSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if _name_ == '_main_':
    main()
