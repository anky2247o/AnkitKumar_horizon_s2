import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/root/AnkitKumar_horizon_s2/task3/ros2_ws/install/lv_3'
