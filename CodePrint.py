#import cv2
import numpy as np

# List to store circle positions
circles = []

# Mouse callback function
def mouseClick(event, xPos, yPos, flags, param):
    global circles
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((xPos, yPos))
        print(f"Circle added at ({xPos}, {yPos})")

# Creating a black image/frame of 500x500 size
frame = np.zeros((500, 500, 3), np.uint8)

# Creating a window to display image/frame
cv2.namedWindow('FRAME')

# This function detects every new event and triggers the "mouseClick" function
cv2.setMouseCallback('FRAME', mouseClick)

while True:
    # Create a copy of the frame to draw circles on
    display_frame = frame.copy()

    # Draw circles on the image
    for (x, y) in circles:
        cv2.circle(display_frame, (x, y), 10, (0, 0, 255), -1)

    # Display the image/frame
    cv2.imshow('FRAME', display_frame)

    # Check if 'q' is pressed to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up and close all OpenCV windows
cv2.destroyAllWindows()