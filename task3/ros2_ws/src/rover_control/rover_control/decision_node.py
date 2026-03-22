import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class DecisionNode(Node):
    def __init__(self):
        super().__init__('decision_node')
        self.subscription = self.create_subscription(Int32, 'distance', self.callback, 10)
        self.publisher_ = self.create_publisher(String, 'rover_command', 10)

    def callback(self, msg):
        dist = msg.data
        command = "STOP" if dist < 30 else "MOVE_FORWARD"
        out_msg = String()
        out_msg.data = command
        self.publisher_.publish(out_msg)
        self.get_logger().info(f'Recv: {dist} -> Sent: {command}')

def main(args=None):
    rclpy.init(args=args)
    node = DecisionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
