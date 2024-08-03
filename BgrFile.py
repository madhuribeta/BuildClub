import cv2
import numpy as np

# Initial values for the trackbars
red_value = 0
green_value = 0
blue_value = 0

def update_image(val):
    global red_value, green_value, blue_value, image
    
    # Update the values from the trackbars
    red_value = cv2.getTrackbarPos('Red', 'Image Window')
    green_value = cv2.getTrackbarPos('Green', 'Image Window')
    blue_value = cv2.getTrackbarPos('Blue', 'Image Window')

    # Create an image with the updated colors
    color_image = np.zeros((500, 500, 3), dtype=np.uint8)
    color_image[:] = [blue_value, green_value, red_value]  # BGR format
    
    # Display the updated image
    cv2.imshow('Image Window', color_image)

# Create a window to display the image
cv2.namedWindow('Image Window')

# Create trackbars for Red, Green, and Blue
cv2.createTrackbar('Red', 'Image Window', 0, 255, update_image)
cv2.createTrackbar('Green', 'Image Window', 0, 255, update_image)
cv2.createTrackbar('Blue', 'Image Window', 0, 255, update_image)

# Initialize the image
update_image(0)

while True:
    # Wait for key events and exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up and close all OpenCV windows
cv2.destroyAllWindows()