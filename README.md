Ankit Kumar Horizon S2 Project
Task 1: Rover Kinematics (Python)
Task 2: Arduino Servo Control (Tinkercad)
Task 3: ROS2 Communication (Sensor, Decision, & Listener Nodes)
Task 3: ROS2 Rover Control System= LV_3(folder)
This project implements a three-node communication system using ROS2 Humble to simulate a rover's autonomous decision-making process based on sensor data.

Project Architecture
The system follows a publisher-subscriber model:

Sensor Node: Generates random distance values (0-100m) and publishes to /distance.

Decision Node: Subscribes to /distance, applies logic, and publishes commands to /rover_command.

Command Listener (Bonus): Subscribes to /rover_command and logs the execution status.

Logic Rules
Distance < 30: Publishes STOP

Distance ≥ 30: Publishes MOVE_FORWARD

How to Build and Run
1. Prerequisites
Ensure you have ROS2 Humble installed and colcon build tools:

Bash
sudo apt install ros-humble-ros-base python3-colcon-common-extensions
2. Build the Workspace
From the task3/ros2_ws directory:

Bash
cd ros2_ws
colcon build
3. Run the Nodes
Open three separate terminals, source the environment in each, and run:

Terminal 1 (Sensor):

Bash
source install/setup.bash
ros2 run rover_control sensor_node
Terminal 2 (Decision):

Bash
source install/setup.bash
ros2 run rover_control decision_node
Terminal 3 (Listener/Bonus):

Bash
source install/setup.bash
ros2 run rover_control listener_node
Topics Used
/distance (std_msgs/Int32)

/rover_command (std_msgs/String)

Final Step for You:
Save the file (Ctrl+O, Enter, Ctrl+X).

Add it to your git:

Bash
git add README.md
git commit -m "Added detailed README for Task 3"
Try the push again using the method we discussed.
