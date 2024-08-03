import cv2
import numpy as np

def nothing(x):
    pass

video_path = 'video.mp4'  # Replace with your video file path
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
cap.release()

cv2.namedWindow('Trackbars')
cv2.createTrackbar('LH', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('LS', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('LV', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('UH', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('US', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('UV', 'Trackbars', 255, 255, nothing)

while True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lh = cv2.getTrackbarPos('LH', 'Trackbars')
    ls = cv2.getTrackbarPos('LS', 'Trackbars')
    lv = cv2.getTrackbarPos('LV', 'Trackbars')
    uh = cv2.getTrackbarPos('UH', 'Trackbars')
    us = cv2.getTrackbarPos('US', 'Trackbars')
    uv = cv2.getTrackbarPos('UV', 'Trackbars')
    
    lower_bound = np.array([lh, ls, lv])
    upper_bound = np.array([uh, us, uv])
    
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)
    
    key = cv2.waitKey(1)
    if key == 27:  # Esc key to stop
        break

cv2.destroyAllWindows()
print(f"Lower Bound: {lower_bound}")
print(f"Upper Bound: {upper_bound}")
