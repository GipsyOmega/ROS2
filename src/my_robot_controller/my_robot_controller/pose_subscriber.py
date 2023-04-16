import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class PoseSubscriber(Node):

	def __init__(self):
		super().__init__("Pose_Subscriber")
		self.pose_subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.pose_callback, 10)
		self.get_logger().info("Pose Subscriber Node")
		#self.timer_ = self.create_timer(0.5, self.send_velocity_command)
	
	def pose_callback(self, msg: Pose):
		self.get_logger().info("{" + str(msg.x) + str(msg.y) + "}")

def main(args = None):
	rclpy.init(args=args)
	node = PoseSubscriber()
	rclpy.spin(node)
	rclpy.shutdown()

if __name__ == '__main__':
	main()