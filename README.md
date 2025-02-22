# FinMouse
Computer Vision (CV)-based Finger Mouse Control System

## Mouse Controle
#### get_mouse_position method:
returns the coordinates of the current mouse position.

#### move_mouse method:
Moves the mouse to a position.

#### click_mouse mthod:
Clicks the button # times.

## Hand Tracking:
### HandTracker Class:
Initializes the MediaPipe Hand Tracking with customizable parameters.

#### find_hands method:
Detects hands in the given frame and returns the results of the **hand detection model**, which are **21 landmarks**(points) with three coordinates **(x, y, z)** and **z** is the depth related to camera.

#### get_landmark_positions method:
Extracts hand landmarks positions (x, y) from the result of the model.

#### draw_landmarks_on_frame method:
Draws hands landmarks on the frame based on detection results:
- **Mouse Position**: x and y coordinates.
- **Middle Finger MCP Circle**: to display the position responsible for moving the mouse.
- **Index Finger Tip Circle**: to display the finger responsible for **Left Clicks**.
- **Middle Finger Tip Circle**: to display the finger responsible for **Right Clicks**.

#### set_parameters method:
Updates the parameters of the HandTracker dynamically.

## Additions
#### Cross Fingers Exit method:
If you want to exit press "q" or cross the tops of Middle Finger  and Index Finger.

# Installation & Usage
- 1. Install dependencies:
```
pip install -r requirements.txt
```
- 2. Transfer to 'app' directory:
```
cd app
```
- 3. Run OpenCV Camera Capture
```
python main.py
```

# License
MIT License
Copyright (c) 2025 Ameur