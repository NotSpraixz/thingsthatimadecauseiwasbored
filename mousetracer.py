import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define range of red color in HSV
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    
    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv_frame, lower_red, upper_red)
    
    # Find contours of the red objects
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Get the largest contour (assuming it's the object we want)
        largest_contour = max(contours, key=cv2.contourArea)
        
        # Get the center of the largest contour
        M = cv2.moments(largest_contour)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        
        # Move the mouse cursor towards the center of the red object
        screen_width, screen_height = pyautogui.size()
        mouse_x = int(cx * screen_width / frame.shape[1])
        mouse_y = int(cy * screen_height / frame.shape[0])
        pyautogui.moveTo(mouse_x, mouse_y, duration=0.5)
    
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break
        
cap.release()
cv2.destroyAllWindows()
