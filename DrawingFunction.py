import cv2
import numpy as np

def draw_shapes():
    # Create a blank image
    image = np.zeros((500, 500, 3), dtype=np.uint8)

    # Draw a line
    start_point = (50, 50)
    end_point = (200, 50)
    color = (255, 0, 0)  # Blue color in BGR
    thickness = 2
    cv2.line(image, start_point, end_point, color, thickness)

    # Draw an arrowed line
    start_point = (50, 100)
    end_point = (200, 100)
    color = (0, 255, 0)  # Green color in BGR
    thickness = 2
    cv2.arrowedLine(image, start_point, end_point, color, thickness)

    # Draw a rectangle
    top_left = (50, 150)
    bottom_right = (200, 250)
    color = (0, 0, 255)  # Red color in BGR
    thickness = 2
    cv2.rectangle(image, top_left, bottom_right, color, thickness)

    # Draw a circle
    center = (300, 300)
    radius = 50
    color = (255, 255, 0)  # Cyan color in BGR
    thickness = 2
    cv2.circle(image, center, radius, color, thickness)

    # Draw a polygon
    points = np.array([[250, 400], [300, 350], [350, 400]], np.int32)
    points = points.reshape((-1, 1, 2))
    color = (255, 0, 255)  # Magenta color in BGR
    thickness = 2
    isClosed = True
    cv2.polylines(image, [points], isClosed, color, thickness)

    # Put text
    text = 'OpenCV'
    bottom_left = (50, 450)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255)  # White color in BGR
    thickness = 2
    cv2.putText(image, text, bottom_left, font, font_scale, color, thickness)

    # Display the image
    cv2.imshow('Drawing Shapes', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call the function
draw_shapes()