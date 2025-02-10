from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile

QOS_PROFILE = QoSProfile(depth=1)

class MovementNode(Node):
    """
    The MovementNode class is a ROS2 node that controls the movement of
    my turtle bot robot in Gazebo

    Args:
        Node
    """

    def __init__(self) -> None:
        """
        Initialize the MovementNode class
        """

        super().__init__("movement_node")
        self.get_logger().info("Starting the Movement Node")

        # Publishers
        self.velocity_pub = self.create_publisher(Twist, "/cmd_vel", QOS_PROFILE)

        # timer
        self.create_timer(0.5, self.send_velocity_command)

        self.get_logger().info("Movement Node Initialized")

    def send_velocity_command(self) -> None:
        msg = Twist()

        msg.angular.z = 1.0

        self.velocity_pub.publish(msg)
        self.get_logger().info(f"Robot is turning at {msg.angular.z} m/s about z-axis")
    
def main(args=None) -> None:
    rclpy.init(args=args)

    movement_node = MovementNode()

    rclpy.spin(movement_node)
    movement_node.destroy_node()
    rclpy.shutdown()
