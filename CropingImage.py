import cv2
import numpy as np

# Variables to store the cropping rectangle
start_point = None
end_point = None
cropping = False

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global start_point, end_point, cropping, image, clone

    if event == cv2.EVENT_LBUTTONDOWN:
        # Start the cropping rectangle
        start_point = (x, y)
        cropping = True
        clone = image.copy()

    elif event == cv2.EVENT_MOUSEMOVE:
        # Draw a rectangle on the image as the mouse is dragged
        if cropping:
            image = clone.copy()
            cv2.rectangle(image, start_point, (x, y), (0, 255, 0), 2)
            cv2.imshow('Image Window', image)

    elif event == cv2.EVENT_LBUTTONUP:
        # Finalize the cropping rectangle
        end_point = (x, y)
        cropping = False
        cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)
        cv2.imshow('Image Window', image)

        # Crop the image
        if start_point and end_point:
            x1, y1 = start_point
            x2, y2 = end_point
            cropped_image = clone[y1:y2, x1:x2]
            cv2.imwrite('cropped_image.jpg', cropped_image)
            print('Cropped image saved as cropped_image.jpg')

# Read an image
image = cv2.imread('OIP.jpeg')  # Change 'input_image.jpg' to your image path
clone = image.copy()

# Create a window to display the image
cv2.namedWindow('Image Window')

# Set the mouse callback function
cv2.setMouseCallback('Image Window', mouse_callback)

while True:
    # Display the image
    cv2.imshow('Image Window', image)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up and close all OpenCV windows
cv2.destroyAllWindows()