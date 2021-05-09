import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
def get_turtlesim_pose(data):
    # print(data)
    global bot_pose
    bot_pose=data
    bot_pose.x=data.x
    bot_pose.y=data.y
    

def send_turtlesim_cmd_vel():
    global bot_pose , pub , desired_pose
    distance_to_goal = sqrt(pow((desired_pose.x - bot_pose.x), 2) +  pow((desired_pose.y - bot_pose.y), 2))
    angle_to_goal    = atan2(desired_pose.y - bot_pose.y, desired_pose.x - bot_pose.x)
    angle_to_turn    = angle_to_goal - bot_pose.theta
    new_vel= Twist()
    new_vel.linear.x = distance_to_goal
    new_vel.angular.z= angle_to_turn
    if (distance_to_goal>=0.5): # as it will never converge and overshoot
        pub.publish(new_vel)



def main(args=None):
    rclpy.init(args=args)

    global node, pub , desired_pose
    node = Node('Go_to_position_node')
    node.create_subscription(Pose,'/turtle1/pose',get_turtlesim_pose,10)
    desired_pose=Pose()
    desired_pose.x = 9.1
    desired_pose.y = 9.1
    pub=node.create_publisher(Twist,'/turtle1/cmd_vel',10)
    node.create_timer(0.5, send_turtlesim_cmd_vel)

    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()
