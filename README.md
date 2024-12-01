# About the Project
The Smart Traffic Light System project provides an efficient solution for urban traffic management by leveraging the Raspberry Pi Pico microcontroller, USR-E1 Ethernet module, and Yolov5 object detection model. The system is designed to detect and count vehicles (cars and motorbikes) on two roads using two cameras, then automatically adjust the duration of green and red lights based on the traffic density on each road.

<div align="center">
    <img src="PCB Desgin-Giao diện điều khiển-Hoàn thiện mô hình/8_Hoàn thiện mô hình.jpg" alt="Smart Traffic Light System" title="Smart Traffic Light System" width="800">
</div>

<div align="center">
    <img src="PCB Desgin-Giao diện điều khiển-Hoàn thiện mô hình/1_Top layer PCB_Altium.png" alt="Smart Traffic Light System" title="Smart Traffic Light System" width="800">
</div>

# Project Members
This project was developed by Group 8 from class DHDTVT17D at Industrial University of Ho Chi Minh City. Below are the group members and their responsibilities:

<div align="center">
    <img src="PCB Desgin-Giao diện điều khiển-Hoàn thiện mô hình/IMG_0896.JPG" alt="Smart Traffic Light System" title="Smart Traffic Light System" width="800">
</div>

<div align="center">
    
| Name              | Responsibility                                      |
|-------------------|----------------------------------------------------|
| [Hoàng Long](https://github.com/HoangLong69)    | Team Leader, PCB design, component soldering, interface design, and model training  |
| [Kiều Hoàng My](https://github.com/kieuhoangmy) | Model design and preparation for training  |
| [Tạ Quang Khải](https://www.facebook.com/khai.ta.391) | Firmware development and model training  |
| [Phùng Quyền Linh](https://github.com/phungquyenlinh) | Image processing implementation  |
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
    <img src="PCB Desgin-Giao diện điều khiển-Hoàn thiện mô hình/5_Giao diện điều khiển và nhận diện.png" alt="Smart Traffic Light System" title="Smart Traffic Light System" width="800">
</div>

This system not only improves traffic flow but also serves as a research platform for developing more advanced smart traffic solutions in the future.

# Model Training on Local Computer
The YOLOv5 model was trained locally on a high-performance computer with the following specifications:

- **CPU:** Intel Core i7 12700F  
- **RAM:** 32GB  
- **GPU:** NVIDIA RTX 4060 Ti with 16GB VRAM
<div align="center">
    <img src="PCB Desgin-Giao diện điều khiển-Hoàn thiện mô hình/trainning.png" alt="Smart Traffic Light System" title="Smart Traffic Light System" width="800">
</div>

### Training Result:
<div align="center">
    <img src="Group8_trainModel/results.png" alt="Smart Traffic Light System" title="Smart Traffic Light System" width="800">
</div>

### Training Parameters
The training was conducted using the following parameters:  
```python
results = model.train(data='custom_dataset.yaml', epochs=50, device=device, batch=16)


