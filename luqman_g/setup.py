from setuptools import setup

package_name = 'luqman_g'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luqman',
    maintainer_email='luqman@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        console_scripts': [
                'go_to_position_node = luqman_g.4_go_to_position:main',
                 'publisherfor_turtlesim = luqman_g.3_turtlesim_pub:main',
                 'nonOOP_publisher = luqman_g.2_publisher_nonOOP:main',
                 'OOP_subsciber = luqman_g.2_listener:main',   
                 'subsciber = luqman_g.1_listener_OOP:main',
                 'publisher = luqman_g.1_talker_OOP:main',
        ],
    },
)
