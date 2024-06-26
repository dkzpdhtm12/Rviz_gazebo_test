from launch_ros.actions import Node
from launch import LaunchDescription
from launch.conditions import IfCondition
from launch_ros.substitutions import FindPackageShare
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution

def generate_launch_description():

    urdf_path = PathJoinSubstitution(
        [FindPackageShare("rviz_gazebo"), "urdf", "car_gazebo_add_lidar.urdf.xacro"]
    )

    world_path = PathJoinSubstitution(
        [FindPackageShare("rviz_gazebo"), "world", "test_gazebo_worlds.world"]
    )

    rviz_config_path = PathJoinSubstitution(
        [FindPackageShare('rviz_gazebo'), 'rviz', 'gazebo_rviz2.rviz']
    )

    return LaunchDescription([

        DeclareLaunchArgument(
            name='urdf',
            default_value=urdf_path,
            description='URDF path'
        ),

        DeclareLaunchArgument(
            name='use_sim_time',
            default_value='true',
            description='Use simulation time'
        ),

        DeclareLaunchArgument(
            name='rviz',
            default_value='true',
            description='Run rviz'
        ),

        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so', world_path],
            output='screen'
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path],
            condition=IfCondition(LaunchConfiguration("rviz")),
            parameters=[{'use_sim_time': LaunchConfiguration('use_sim_time')}]
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[
                {
                    'use_sim_time': LaunchConfiguration('use_sim_time'),
                    'robot_description': Command(['xacro ', LaunchConfiguration('urdf')])
                }
            ],
            remappings=[('tf', 'gazebo_tf'), ('joint_states', 'gazebo_joint_states'), ('robot_description', 'gazebo_robot_description')]
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='urdf_spawner',
            output='screen',
            arguments=["-topic", "gazebo_robot_description", "-entity", "car",
                        "-x", "0.0", "-y", "0.0", "-z", "0.0"]
        ),

        # Node(
        #     package='test_world',
        #     executable='image_raw',
        #     name='image_raw',
        #     output='screen',
        # ),
    ])
