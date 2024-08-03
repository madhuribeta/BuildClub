import cv2

# Video capture object where 0 is the camera number for a USB camera
# If 0 doesn't work, you might need to change the camera number to get the correct one
cam = cv2.VideoCapture(0)

# For video file, use:
# cam = cv2.VideoCapture('video_file_path')

# For IP camera, use:
# cam = cv2.VideoCapture('IP_Address')

# Get the width, height, and fps of the video capture
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cam.get(cv2.CAP_PROP_FPS)

# Define the output file location and name
output_file = './task_2/recording.MP4'

# Create a VideoWriter object
output = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'MP4V'), fps, (width, height))

while True:
    ret, frame = cam.read()  # Read one frame from the camera object
    if not ret:
        break

    cv2.imshow('Webcam', frame)  # Display the current frame in a window

    output.write(frame)  # Write the current frame to the output file

    # Waits for 1ms and check for the pressed key
    if cv2.waitKey(1) & 0xff == ord('q'):  # Press 'q' to quit the camera
        break

# Release the camera and the output file
cam.release()
output.release()
cv2.destroyAllWindows()  # Close all the active windows