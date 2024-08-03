import cv2

# Capture a frame from the video
video_path = 'video.mp4'  # Replace with your video file path
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
cap.release()

# Save the captured frame to disk
cv2.imwrite(' ijk.jpeg', frame)
