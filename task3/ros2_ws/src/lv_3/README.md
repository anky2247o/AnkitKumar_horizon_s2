# Level 3 Task: ROS2 Publisher and Subscriber

This project demonstrates basic communication between two ROS2 nodes using a custom Python package named `lv_3`.

## Project Structure
* **Distance Publisher**: Generates random integer values (simulating rover sensor data) and publishes them to the `/distance` topic every second.
* **Distance Subscriber**: Listens to the `/distance` topic and prints the received values to the terminal.

## How to Run

### 1. Build the package
```bash
cd ~/AnkitKumar_horizon_s2/task3/ros2_ws/
colcon build --packages-select lv_3
source install/setup.bash
```

### 2. Run the Publisher
Open a terminal and run:
```bash
ros2 run lv_3 distance_publisher
```

### 3. Run the Subscriber
Open a **new** terminal and run:
```bash
source install/setup.bash
ros2 run lv_3 distance_subscriber
```

## Example Output
```text
Received distance: 10
Received distance: 35
Received distance: 72
```
