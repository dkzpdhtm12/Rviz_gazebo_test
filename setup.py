from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'rviz_gazebo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.xacro')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
        (os.path.join('share', package_name, 'urdf', 'plugin'), glob('urdf/plugin/*.xacro')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
        (os.path.join('share', package_name, 'world'), glob('world/*.world')),
        (os.path.join('share', package_name, 'world'), glob('world/*.model')),
        (os.path.join('share', package_name, 'meshes', 'test_robot'), glob('meshes/test_robot/*.dae')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bug_sim',
    maintainer_email='mn03042@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_raw = code.image_raw:main',
        ],
    },
)
