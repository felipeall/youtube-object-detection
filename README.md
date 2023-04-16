# YouTube Object Detection
The YouTube Object Detection is a Python-based application that aims to process YouTube videos and detect objects 
within the video frames using computer vision techniques. The project utilizes state-of-the-art object detection 
algorithms and libraries to automatically identify and localize objects of interest in the video frames.

<div align="center"><img src="https://user-images.githubusercontent.com/20917430/232325915-9e9c8a30-c08c-4a0f-9789-ef560e3a0431.gif" width="700"/></div>

---

### Technologies

**OpenCV**

_[OpenCV (Open Source Computer Vision Library)](https://github.com/opencv/opencv) is a popular open-source computer vision and machine learning library 
for image and video processing. Written in C++ and Python, it offers a wide range of tools for tasks like image 
manipulation, object detection, and camera calibration. Widely used in various fields, OpenCV is known for its 
comprehensive documentation, large community support, and cross-platform compatibility._

**YOLOv4-tiny**

_[YOLO v4 Tiny](https://github.com/AlexeyAB/darknet) is a compact object detection algorithm designed for resource-constrained environments. It offers a 
balance between accuracy and inference speed, with a smaller network architecture optimized for real-time object 
detection. It can be implemented using popular deep learning frameworks and trained on custom datasets for specific 
domains, maintaining accuracy despite its smaller size._

**FastAPI**

_[FastAPI](https://github.com/tiangolo/fastapi) is a modern, fast, and lightweight Python web framework for building APIs. It offers automatic documentation 
generation, data validation, and serialization using type hints, making it highly productive. It also supports 
asynchronous programming and is popular among developers for building scalable APIs with Python._

---

### Running locally (Poetry)
````bash
$ git clone https://github.com/felipeall/youtube-object-detection.git
$ cd youtube-object-detection
$ poetry shell
$ poetry install
$ make run-local
````

### Running locally (Docker)
````bash
$ git clone https://github.com/felipeall/youtube-object-detection.git
$ cd youtube-object-detection
$ make run
````
