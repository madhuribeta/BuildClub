import cv2

def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordinates: ({x}, {y})")
        points.append((x, y))

video_path = 'video.mp4'  # Replace with your video file path
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
cap.release()

points = []
cv2.imshow('Frame', frame)
cv2.setMouseCallback('Frame', get_coordinates)

print("Click on the four corners of the quadrants in the frame.")
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Quadrant Points:", points)
