import cv2
import numpy as np

# Variables to store curve points
points = []
drawing = False

# Mouse callback function
def mouseClick(event, x, y, flags, param):
    global points, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        # Start a new curve
        points = [(x, y)]
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        # Add points to the curve while dragging
        if drawing:
            points.append((x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        # Finalize the curve
        points.append((x, y))
        drawing = False

# Create a black image/frame
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Create a window to display image/frame
cv2.namedWindow('FRAME')

# Set up mouse callback function
cv2.setMouseCallback('FRAME', mouseClick)

while True:
    # Create a copy of the image to draw on
    display_image = image.copy()

    # Draw the curve if points are available
    if len(points) > 1:
        cv2.polylines(display_image, [np.array(points, np.int32)], isClosed=False, color=(0, 255, 0), thickness=2)

    # Display the image/frame
    cv2.imshow('FRAME', display_image)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up and close all OpenCV windows
cv2.destroyAllWindows()