import cv2
import mediapipe as mp
import face_recognition as fr
import csv
from datetime import datetime

# Initialize video capture
cam = cv2.VideoCapture(0)  # Use 0 for webcam, or replace with video file path

# Frame width and height
width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Initialize MediaPipe face detection
faces = mp.solutions.face_detection.FaceDetection()

# Load and encode template faces
template_faces = {
    "Bean": fr.face_encodings(fr.load_image_file("./task_7/mrBean.png"))[0],
    # Add more templates as needed
}

# Function to update attendance in CSV
def update_attendance(name):
    updated_rows = []
    with open('attendance.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Name'] == name and row['Attendance'] == 'Absent':
                now = datetime.now()
                row['Attendance'] = 'Present'
                row['Date'] = now.strftime("%Y-%m-%d")
                row['Time'] = now.strftime("%H:%M:%S")
            updated_rows.append(row)
    
    with open('attendance.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Attendance', 'Date', 'Time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

while True:
    ret, frame = cam.read()  # Read a frame from the video capture
    if ret:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
        face_results = faces.process(frame_rgb)  # Detect faces

        if face_results.detections:
            for detection in face_results.detections:
                bBox = detection.location_data.relative_bounding_box
                x, y, w, h = int(bBox.xmin * width), int(bBox.ymin * height), int(bBox.width * width), int(bBox.height * height)
                cropped_face = frame_rgb[y:y + h, x:x + w]  # Crop the detected face

                if cropped_face.size > 0:
                    cropped_face_encodings = fr.face_encodings(cropped_face)
                    if cropped_face_encodings:
                        cropped_face_encoding = cropped_face_encodings[0]
                        matches = fr.compare_faces(list(template_faces.values()), cropped_face_encoding)
                        name = "Unknown"

                        if True in matches:
                            match_index = matches.index(True)
                            name = list(template_faces.keys())[match_index]
                            update_attendance(name)
                        
                        # Draw a rectangle and put the name
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the capture and close any OpenCV windows
cam.release()
cv2.destroyAllWindows()
