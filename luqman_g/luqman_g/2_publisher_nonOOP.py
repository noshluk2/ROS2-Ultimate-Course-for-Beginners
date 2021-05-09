import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def timed_callback():
    global node ,pub
    msg = String()
    msg.data = ("Message from nonOOP Publisher")
    pub.publish(msg)
    

def main(args=None):
    rclpy.init(args=args)

    global node, pub
    node = Node('NON_OOP_PUBLISHER_node')
    pub=node.create_publisher(String,'NON_OOP_topic',10)
    node.create_timer(0.2, timed_callback)

    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()