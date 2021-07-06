import rclpy
from rclpy.node import Node
from std_msgs.msg import String

def listen_callback(msg):
    global node
    node.get_logger().info('I listened -> "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    global node
    node = Node('NON_OOP_SUBSCRIBER_node')
    node.create_subscription(String,'NON_OOP_topic',listen_callback,10)
    
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()
    