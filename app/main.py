import cv2
import mediapipe as mp

from hand_tracking import HandTracker

# Create instance of HandTracker
hands = HandTracker(circles_size=5,flip_frame=True,cross_fings_exit=True)

# Capture Video Stream
cap = cv2.VideoCapture(2)

while cap.isOpened():
    # Read the curent frame from the video
    ret, frame = cap.read()
    
    # Stop if there is an error in reading the frame 
    if not ret:
        break
    
    result, frame = hands.find_hands(frame)
    frame, cross_fings_exit = hands.draw_landmarks_on_frame(frame,result)

    if cross_fings_exit:
        break
    
    # Display the current frame
    cv2.imshow('FinMouse', frame)

    # Wait for 20 milliseconds before desplaying the next frame
    # Click 'q' to exit
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Close the camera capture
cap.release()
# Close all OpenCV opened windows
cv2.destroyAllWindows()