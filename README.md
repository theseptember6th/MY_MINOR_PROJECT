# Soccer Analysis Using Machine Learning

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
│   └── best.pt                     # YOLOv8 model
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
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/yourusername/SoccerAnalysis.git
   cd SoccerAnalysis
   ```
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
5. **Upload a video through the web interface and process it.**

## Methodology
### **1. Object Detection (YOLOv8)**
- The YOLOv8 model detects players, referees, and the ball in video frames.

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

## Contributors
- **[Your Name]** - Project Lead
- **[Team Member 1]** - Web Development
- **[Team Member 2]** - Machine Learning
- **[Supervisor]** - Research Guidance

## References
- [YOLO Object Detection](https://github.com/ultralytics/yolov8)
- [ByteTrack Multi-Object Tracking](https://github.com/ifzhang/ByteTrack)
- [OpenCV for Computer Vision](https://opencv.org/)
- [Flask Web Development](https://flask.palletsprojects.com/en/2.0.x/)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


# SOCCER ANALYSIS
## Description

Hi there! This is my minor project, **Project Soccer Analysis**. In this project, I have pre-trained a **YOLOv5 model** on my custom dataset to analyze soccer matches. By utilizing this model along with various computer vision techniques, the project can process prerecorded soccer match videos and extract crucial metrics such as:

- **Team Ball Possession**: Determines the percentage of time each team controls the ball during the game.
- **Player Speed and Distance**: Tracks the movement of players, providing insights into their speed and the total distance covered.
- - **Camera Movement Detection**: Identifies and compensates for camera movements, ensuring accurate tracking of players and game metrics regardless of changes in the camera’s position or angle.
  
The project uses the power of deep learning and computer vision to provide faster analysis, helping to extract actionable data from soccer games.
To run the project, make sure you follow the steps below carefully.

## Installation

### Prerequisites
- Python 3.8.5(which i had used) or higher
- Required libraries (see `requirements.txt`)

### Setting Up
1. **Create a `models` folder**: In your project directory, create a folder called `models`. This is where the model file will be stored.

2. **Download the Model**: You will need to download the pre-trained model `best.pt` by following the link below:
   - [Download best.pt](<https://drive.google.com/file/d/1G_bwdCzZAhASvG71qBXzwIa2pw93h0nX/view?usp=sharing>)

3. **Place the Model**: After downloading `best.pt`, move the file into the `models` folder you created.

4. **Install Dependencies**:
   Make sure all dependencies are installed by running:
   ```bash
   pip install -r requirements.txt
