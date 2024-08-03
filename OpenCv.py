import cv2
import numpy as np

# Callback function for trackbar
def nothing(value):
    print(f"Trackbar Value: {value}")

# Create a black image/frame
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Create a window to display image/frame
cv2.namedWindow('Trackbar Window')

# Create a trackbar in the window
cv2.createTrackbar('Slider', 'Trackbar Window', 0, 100, nothing)

while True:
    # Display the image/frame
    cv2.imshow('Trackbar Window', image)

    # Wait for key events and exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up and close all OpenCV windows
cv2.destroyAllWindows()