from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([  
        DeclareLaunchArgument(
            'target_frame', default_value='ball',
            description='Target frame name.'
        ), 
        Node(
            package='learning_tf2_py',
            executable='tf2_to_cmd_vel',
            name='listener',
            parameters=[
                {'target_frame': LaunchConfiguration('target_frame')}
            ]
        ),
    ])
