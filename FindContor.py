# Import required libraries
import cv2
import numpy as np

# Input video file
cam = cv2.VideoCapture('./task_5/ball.wmv')

while True:
    # Read a frame from the video
    ret, frame = cam.read()
    
    # Break the loop if no frame is read (end of video)
    if not ret:
        break
    
    # Convert the frame to HSV color space for masking
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define lower and upper bounds for color in HSV
    lowerBound = np.array([110, 80, 134])  # Lower bound for color
    upperBound = np.array([150, 255, 255])  # Upper bound for color
    
    # Create a mask using the color range
    mask = cv2.inRange(frameHSV, lowerBound, upperBound)
    
    # Find contours on the masked frame
    ballContours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Iterate through each contour
    for ballContour in ballContours:
        area = cv2.contourArea(ballContour)
        if area > 500:  # Filter out small contours that could be noise
            x, y, w, h = cv2.boundingRect(ballContour)  # Get position and size of bounding box
            # Draw a rectangle around the detected ball
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Display the mask and the original frame with detected ball
    cv2.imshow('mask', mask)
    cv2.imshow('Ball', frame)
    
    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()