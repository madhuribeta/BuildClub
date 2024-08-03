import cv2
import numpy as np

# Variables to store rectangle information
start_point = None
end_point = None
drawing = False

# Mouse callback function
def mouseClick(event, x, y, flags, param):
    global start_point, end_point, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        # Record the starting point
        start_point = (x, y)
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        # Update the end point if we are drawing
        if drawing:
            end_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        # Finalize the rectangle
        end_point = (x, y)
        drawing = False
        cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)  # Draw rectangle on image

# Create a black image/frame
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Create a window to display image/frame
cv2.namedWindow('FRAME')

# Set up mouse callback function
cv2.setMouseCallback('FRAME', mouseClick)

while True:
    # Display the image/frame
    cv2.imshow('FRAME', image)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up and close all OpenCV windows
cv2.destroyAllWindows()