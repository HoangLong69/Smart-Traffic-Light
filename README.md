# About the Project
The Smart Traffic Light System project provides an efficient solution for urban traffic management by leveraging the Raspberry Pi Pico microcontroller, USR-E1 Ethernet module, and Yolov5 object detection model. The system is designed to detect and count vehicles (cars and motorbikes) on two roads using two cameras, then automatically adjust the duration of green and red lights based on the traffic density on each road.

<div align="center">
    <img src="images/traffic_system.png" alt="Smart Traffic Light System" title="Smart Traffic Light System" width="400">
</div>

# Key Features:
* Real-time vehicle detection: Utilizes the Yolov5 model to identify and count cars and motorbikes.
* Intelligent traffic light timing adjustment: Dynamically changes the duration of green and red lights according to traffic density, reducing congestion.
* Ethernet connectivity: The USR-E1 module ensures stable and efficient data transmission.
* Optimized design: The Raspberry Pi Pico ensures low cost and high performance.

# Control interface:
The system includes a user-friendly control interface developed using **PyQt5**, providing the following features:

- **Connect/Disconnect to IP and Port:** Allows users to establish or terminate connections to the traffic light system via specified IP addresses and ports.
- **Send Timing Commands:** Enables users to set and adjust the timing for each traffic light remotely.
- **Plot Graphs from CSV Files:** Provides visualization tools to generate graphs from CSV files, helping to analyze traffic data effectively.

This interface enhances system usability and provides operators with powerful tools to monitor and manage traffic efficiently.
<div align="center">
    <img src="PCB Desgin-Giao diện điều khiển-Hoàn thiện mô hình/IMG_0896.JPG" alt="Smart Traffic Light System" title="Smart Traffic Light System" width="400">
</div>

# Project Members
This project was developed by Group 8 from class DHDTVT17D at Industrial University of Ho Chi Minh City. Below are the group members and their responsibilities:

<div align="center">
    <img src="PCB Desgin-Giao diện điều khiển-Hoàn thiện mô hình/IMG_0896.JPG" alt="Smart Traffic Light System" title="Smart Traffic Light System" width="400">
</div>

| Name              | Responsibility                                      |
|-------------------|----------------------------------------------------|
| **Hoàng Long**    | Team Leader, PCB design, component soldering, interface programming, and model training |
| **Kiều Hoàng My** | Model design and preparation for training          |
| **Tạ Quang Khải** | Firmware development and model training            |
| **Phùng Quyền Linh** | Image processing implementation                 |

This system not only improves traffic flow but also serves as a research platform for developing more advanced smart traffic solutions in the future.
