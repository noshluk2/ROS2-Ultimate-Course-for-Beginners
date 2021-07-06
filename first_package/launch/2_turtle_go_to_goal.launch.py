from  launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        
     Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtle'
        ),
    Node(
            package='first_package',
            executable='go_to_goal_node',
            name='go_to_goal'
        ),

    ])
