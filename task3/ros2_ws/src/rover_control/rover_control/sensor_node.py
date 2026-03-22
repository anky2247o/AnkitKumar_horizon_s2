import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.publisher_ = self.create_publisher(Int32, 'distance', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = random.randint(0, 100)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Distance Sensor: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
