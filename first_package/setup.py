from setuptools import setup
import os 
from glob import glob

package_name = 'first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luqman',
    maintainer_email='noshluk2@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'my_first_pub = first_package.1_publisher:main',
                'my_first_sub = first_package.2_subscriber:main',
                'driving_node = first_package.3_driving_node:main',
                'go_to_goal_node = first_package.4_go_to_goal:main',

        ],
    },
)
