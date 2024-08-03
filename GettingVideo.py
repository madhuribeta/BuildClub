import cv2

# Open the video capture
cam = cv2.VideoCapture(0)

# Set the width, height, and fps
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cam.set(cv2.CAP_PROP_FPS, 30)

# Retrieve and print the properties
width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cam.get(cv2.CAP_PROP_FPS)

print(f"Resolution: {width} x {height} | Frames per second: {fps}")
print(f"Resolution: {width} x {height} | Frames per second: {fps}")
print(f"Resolution: {width} x {height} | Frames per second: {fps}")
print(f"Resolution: {width} x {height} | Frames per second: {fps}")

# Release the video capture object
cam.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()