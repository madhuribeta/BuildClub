# Importing required libraries
import cv2
import numpy as np

p1 = (0, 0)  # top left corner point
pts = []

# Mouse callback function
def mouseClick(event, xPos, yPos, flags, param):
    global p1
    # Left click press event
    if event == cv2.EVENT_LBUTTONDOWN:
        p1 = (xPos, yPos)
        p1 = [p1[0], p1[1]]
        print(p1)
        pts.append(p1)  # Collecting corner points

# Reading image
path = "download2.jpeg"
frame = cv2.imread(path)

# Creating a window to display image/frame
cv2.namedWindow('FRAME')
# This function detects every new event and triggers the "mouseClick" function
cv2.setMouseCallback('FRAME', mouseClick)

while True:
    cv2.imshow('FRAME', frame)
    if len(pts) >= 4:
        pts_src = np.float32(pts[:4])
        pts_dst = np.float32([[0, 0], [200, 0], [200, 400], [0, 400]])
        matrix = cv2.getPerspectiveTransform(pts_src, pts_dst)
        warped = cv2.warpPerspective(frame, matrix, (200, 400))
        cv2.imshow('Warped', warped)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # to quit press 'q'
        break

cv2.destroyAllWindows()