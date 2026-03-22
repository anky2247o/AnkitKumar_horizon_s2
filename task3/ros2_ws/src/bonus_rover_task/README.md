# Bonus Rover Task

This package contains a three-node system:
* **Sensor Node**: Publishes raw data.
* **Decision Node**: Processes data and makes logic-based choices.
* **Listener Node**: Logs the final decisions.

## Execution Proof
![Bonus Task Output](./bonus_screenshot.png)

## How to Run
1. Build: `colcon build --packages-select bonus_rover_task`
2. Source: `source install/setup.bash`
3. Run Nodes: Open three terminals and run each node using `ros2 run bonus_rover_task [node_name]`.
