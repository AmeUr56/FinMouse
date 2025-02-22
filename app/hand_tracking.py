import cv2
import mediapipe as mp

from mouse_controle import move_mouse, click_mouse

class HandTracker:
    def __init__(self, mode=False, max_hands=1, model_complexity=1,circles_size=10,cross_fings_exit=False,detection_conf=0.5, tracking_conf=0.5, 
                flip_frame=False):
        """
        Initializes the HandTracker with customizable parameters.

        Parameters:
        - mode (bool): Static image mode (True) or continuous tracking (False).
        - max_hands (int): Maximum number of hands to detect.
        - model_complexity (int): Higher values improve accuracy but slow down performance.
        - circles_size (int): Radius of the Circles
        - cross_fings_exit (int): If True, enable feature of exiting when crossing the fingers.
        - detection_conf (float): Confidence threshold for detecting hands.
        - tracking_conf (float): Confidence threshold for tracking hands.
        - flip_frame (bool): If True, flips the frame horizontally.
        """
        self.hands = mp.solutions.hands.Hands(
            static_image_mode=mode, 
            max_num_hands=max_hands, 
            model_complexity=model_complexity, 
            min_detection_confidence=detection_conf, 
            min_tracking_confidence=tracking_conf
        )
        self.hand_label = "Unknown"
        self.flip_frame = flip_frame
        self.circles_size = circles_size
        self.cross_fings_exit = cross_fings_exit
        
    def find_hands(self, frame):
        """
        Detects hands in the given frame and returns the results

        Parameters:
        - frame (numpy.ndarray): Input frame

        Returns:
        - result (MediaPipe object): Contains detected hand landmarks
        """
        if self.flip_frame:
            # Flip horizontally the frame
            frame = cv2.flip(frame, 1)
        
        # Convert frame from BGR to RGB for MediaPipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Process the RGB frame with the hand detection model
        result = self.hands.process(frame_rgb)
        
        # Get Hand type Left of Right
        if result.multi_hand_landmarks:
            for hand_index, hand_landmarks in enumerate(result.multi_hand_landmarks):
                
                if result.multi_handedness:
                    self.hand_label = result.multi_handedness[hand_index].classification[0].label  # "Left" or "Right"
          
        return result, frame

    def get_landmark_positions(self, result, frame_shape, indices):
        """
        Extracts hand landmark positions as a list of (x, y) coordinates.

        Parameters:
        - result (MediaPipe object): Detection results
        - frame_shape (tuple): Shape of the frame
        - indices (List[int]): indices of the landmarks to get position for.

        Returns:
        - hand_landmarks_list (dict): A dict containing hand landmark positions.
        """
        height, width, _ = frame_shape
        hand_landmarks_list = {}

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                for index in indices:
                    landmark = hand_landmarks.landmark[index]
                    # Convert normalized coordinates to pixels
                    x, y = int(landmark.x * width), int(landmark.y * height)  
                    hand_landmarks_list[f"{index}"] = (x,y)
                            
        return hand_landmarks_list
    
    def draw_landmarks_on_frame(self, frame, result):
        """
        Draws hand landmarks on the frame based on detection results.

        Parameters:
        - frame (numpy.ndarray): The input frame.
        - result (MediaPipe object): The detection result from find_hands().
        
        Returns:
        - frame (numpy.ndarray): The modified frame with drawn landmarks.
        """
        
        # If hands are detected
        if result.multi_hand_landmarks:
            landmarks = self.get_landmark_positions(result,frame.shape,[6,8,9,10,12])
            _, y_6 = landmarks["6"]
            x_8, y_8 = landmarks["8"]
            x_9, y_9 = landmarks["9"]
            _, y_10 = landmarks["10"]
            x_12, y_12 = landmarks["12"]
            
            # Draw Yellow Circles for the two fingers
            cv2.circle(frame, (x_8,y_8), self.circles_size, (0, 39, 255), thickness=cv2.FILLED)
            cv2.circle(frame, (x_12,y_12), self.circles_size, (255, 108, 0), thickness=cv2.FILLED)
            
            # Move Mouse based on ninth landmark
            move_mouse((x_9,y_9))
            # Draw Circle
            cv2.circle(frame, (x_9,y_9), self.circles_size, (99, 180, 40), thickness=cv2.FILLED)
            # Write Mouse Position
            cv2.putText(frame,f"Mouse Position=({x_9},{y_9})", (0,20), cv2.FONT_HERSHEY_DUPLEX, 0.5,(99, 180, 40))
            
            # Left Click
            if y_6 < y_8:
                cv2.putText(frame,"Left Click", (250,20),cv2.FONT_HERSHEY_DUPLEX, 0.5,(0, 39, 255))
                click_mouse('left')
            
            # Right Click
            if y_10 < y_12:    
                cv2.putText(frame,"Right Click", (400,20),cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 108, 0))
                click_mouse('right')

            # Cross fingers Exit Method
            if self.cross_fings_exit:
                if self.hand_label == "Right":
                    if x_8 > x_12:
                        return frame, 1
            
                elif self.hand_label == "Left":
                    if x_8 < x_12:
                        return frame, 1
            
                 
        return frame, 0

    def set_parameters(self, detection_conf=None, tracking_conf=None, max_hands=None):
        """
        Updates the parameters of the HandTracker dynamically.

        Parameters:
        - detection_conf (float): New detection confidence threshold.
        - tracking_conf (float): New tracking confidence threshold.
        - max_hands (int): New maximum number of hands.
        """
        if detection_conf is not None:
            self.hands.min_detection_confidence = detection_conf
        if tracking_conf is not None:
            self.hands.min_tracking_confidence = tracking_conf
        if max_hands is not None:
            self.hands.max_num_hands = max_hands

     