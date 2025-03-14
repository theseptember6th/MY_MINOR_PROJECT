## Description
Hi there! This is my minor project, **Project Soccer Analysis**. In this project, I have pre-trained a **YOLOv5 model** on my custom dataset to analyze soccer matches. By utilizing this model along with various computer vision techniques, the project can process prerecorded soccer match videos and extract crucial metrics.

## Overview
This project focuses on analyzing soccer matches using machine learning techniques. It employs YOLO for object detection, ByteTrack for player tracking, K-Means clustering for team assignment, and various computer vision techniques for ball possession estimation, speed calculation, and perspective transformation. The system is integrated with a Flask-based web application for easy interaction.

## Features
- **Player & Ball Detection**: Uses YOLO for detecting players, referees, and the ball.
- **Multi-Object Tracking**: ByteTrack tracks players and ball across multiple frames.
- **Team Assignment**: K-Means clustering assigns team colors based on jersey colors.
- **Ball Possession Estimation**: Identifies which player and team has control of the ball.
- **Camera Movement Compensation**: Optical flow is used to adjust tracking based on camera motion.
- **Perspective Transformation**: Converts detected positions to real-world coordinates.
- **Speed & Distance Calculation**: Computes player movement speed and total distance covered.
- **Web-Based Interface**: A Flask web application allows users to upload videos and view analyzed results.

## Project Structure
```
SoccerAnalysis/
│-- app.py                         # Flask server for the web application
│-- main1.py                       # Core processing script
│-- models/
│   └── best.pt                     # YOLOv5 model
│-- stubs/
│   ├── track_stubs.pkl             # Stored player tracking data
│   ├── camera_movement_stub.pkl    # Stored camera movement data
│-- static/
│   ├── css/style.css               # Stylesheet
│   ├── js/script.js                # JavaScript for UI interactions
│-- templates/
│   └── index.html                  # Web interface
│-- utils.py                         # Helper functions
│-- trackers.py                      # Player and ball tracking implementation
│-- camera_movement_estimator.py     # Camera motion estimation
│-- view_transformer.py              # Perspective transformation
│-- speed_and_distance_estimator.py  # Speed and distance computation
│-- team_assigner.py                 # Team color assignment
│-- player_ball_assigner.py          # Ball possession detection
│-- README.md                        # Project documentation
```

## Installation & Setup
1. **Clone/Download the Repository:**

2. **Create a Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate   # For Linux/macOS
   venv\Scripts\activate      # For Windows
   ```
3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Flask Application:**
   ```sh
   python app.py
   ```
5. **Upload a video of 30 sec or less beacause otherwise it will take a lot of time for processing through the web interface and process it.**

## Methodology
### **1. Object Detection (YOLOv8)**
- The YOLOv5 model detects players, referees, and the ball in video frames.

### **2. Object Tracking (ByteTrack)**
- Assigns unique track IDs to detected objects across multiple frames.

### **3. Team Assignment (K-Means Clustering)**
- Uses K-Means clustering to classify players into teams based on their jersey colors.

### **4. Ball Possession Calculation**
- Determines the closest player to the ball and assigns possession.

### **5. Camera Movement Estimation**
- Optical flow is used to detect global movement and adjust tracking accordingly.

### **6. Perspective Transformation**
- Transforms detected positions into real-world coordinates.

### **7. Speed and Distance Calculation**
- Computes the speed and distance covered by each player.

### **8. Web Integration (Flask)**
- Provides a user-friendly web interface for uploading and analyzing videos.

## Future Enhancements
- **Real-time Processing**: Optimize the system for live match analysis.
- **Enhanced Tracking**: Improve re-identification of players across occlusions.
- **Larger Dataset**: Train the YOLO model on a larger dataset for better accuracy.
- **Event Detection**: Identify key moments like goals, fouls, and passes.
- **3D Field Mapping**: Use depth estimation to enhance movement analysis.


## References
- [YOLO Object Detection](https://github.com/ultralytics/yolov5)
- [ByteTrack Multi-Object Tracking](https://github.com/ifzhang/ByteTrack)
- [OpenCV for Computer Vision](https://opencv.org/)
- [Flask Web Development](https://flask.palletsprojects.com/en/2.0.x/)





