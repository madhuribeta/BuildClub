import cv2
import mediapipe as mp

# Video capture object where 0 is the camera number for a USB camera
# For video file, use this:
cam = cv2.VideoCapture("./task_7/mrBean.mp4")

# Frame width and height, will be useful later to find exact pixel locations
width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Creating a face detector object from Mediapipe solutions
faces = mp.solutions.face_detection.FaceDetection()

while True:
    ret, frame = cam.read()  # Reading one frame from the camera object
    if ret:  # If frame received proceed
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
        
        faceResults = faces.process(frameRGB)  # This returns list of detections
        
        if faceResults.detections:  # If detection is not None
            for face in faceResults.detections:  # Iterate through faces
                bBox = face.location_data.relative_bounding_box

                # Splitting into variables and converting to integers
                x, y, w, h = (int(bBox.xmin * width), int(bBox.ymin * height), 
                              int(bBox.width * width), int(bBox.height * height))
                
                # Drawing the bounding box around the face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Display the frame with the bounding boxes
        cv2.imshow('Webcam', frame)
        
        # Waits for 1ms and checks for the pressed key
        if cv2.waitKey(1) & 0xff == ord('q'):  # Press 'q' to quit the camera
            break

cam.release()  # Close the camera
cv2.destroyAllWindows()  # Close all the active windows
