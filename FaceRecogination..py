# Import required libraries
import cv2
import mediapipe as mp
import face_recognition as fr

# For video file
cam = cv2.VideoCapture("./task_7/mrBean2.mp4")

# Frame width and height, useful to find exact pixel locations from normalized locations of faces
width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Initialize MediaPipe face detection
faces = mp.solutions.face_detection.FaceDetection()

# Load template face image
template_face = fr.load_image_file("./task_7/mrBean.png")

# Encode input face
face_encoding = fr.face_encodings(template_face)[0]  # We are only providing one face

while True:
    ret, frame = cam.read()  # Reading one frame from the camera object
    
    if ret:  # If frame received proceed
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for encoding
        face_results = faces.process(frame_rgb)  # This returns list of locations for all the faces in the current frame
        
        if face_results.detections:  # If detection is non-empty or if at least one face detected, proceed
            for face in face_results.detections:  # Iterate through each face location
                bBox = face.location_data.relative_bounding_box
                # Collect and convert to integer for drawing rectangle around detected faces
                x, y, w, h = int(bBox.xmin * width), int(bBox.ymin * height), int(bBox.width * width), int(bBox.height * height)
                cropped_face = frame_rgb[y:y + h, x:x + w]  # Getting cropped face
                
                if cropped_face.size > 0:  # To filter out false detection and empty dimensioned crop
                    # Encode the cropped face
                    cropped_face_encoding = fr.face_encodings(cropped_face)
                    
                    if cropped_face_encoding:  # If encoding is not empty
                        match = fr.compare_faces([face_encoding], cropped_face_encoding[0])
                        
                        if match[0]:  # If the face matches the template face
                            # Draw a rectangle around the detected face
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            cv2.putText(frame, "Mr. Bean", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        # Display the resulting frame
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the capture and close any OpenCV windows
cam.release()
cv2.destroyAllWindows()
