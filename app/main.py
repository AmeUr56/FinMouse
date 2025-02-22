import cv2

# Capture Video Stream
cap = cv2.VideoCapture(2)

while cap.isOpened():
    # Read the curent frame from the video
    ret, frame = cap.read()
    
    # Stop if there is an error in reading the frame 
    if not ret:
        break
    
    # Flip horizontally the frame
    flipped_horiz_frame = cv2.flip(frame, 1)
    
    # Add Text to the image
    cv2.putText(flipped_horiz_frame,"FinMouse",(0, 20),cv2.FONT_HERSHEY_DUPLEX, 1,(46, 204, 113))
    
    # Display the current frame 
    cv2.imshow('FinMouse', flipped_horiz_frame)
    
    # Wait for 30 milliseconds before desplaying the next frame
    # Click 'q' to exit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Close the camera capture
cap.release()
# Close all OpenCV opened windows
cv2.destroyAllWindows()