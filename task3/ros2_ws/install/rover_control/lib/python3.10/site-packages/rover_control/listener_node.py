import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener_node')
        self.sub = self.create_subscription(String, 'rover_command', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'Executing: {msg.data} (Wheels turning...)')

def main(args=None):
    rclpy.init(args=args)
    node = ListenerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
