import cv2
import numpy as np
import pandas as pd

# Replace these with the coordinates obtained from point_coordinates.py
pts1 = np.float32([(100, 200), (700, 200), (100, 350), (700, 350)])  # Example coordinates
pts2 = np.float32([(0, 0), (800, 0), (0, 400), (800, 400)])

# Get perspective transform matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Set HSV bounds (replace with values from mask.py)
lower_bound = np.array([30, 150, 50])
upper_bound = np.array([90, 255, 255])

def detect_ball(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        return max(contours, key=cv2.contourArea)
    return None

def get_ball_region(y):
    if y < 200:
        return 1
    elif y < 300:
        return 2
    elif y < 350:
        return 3
    else:
        return 'out_of_bound'

def main():
    video = cv2.VideoCapture('video.mp4')
    bounce_count = 0
    last_y = 0
    bounces = []

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        warped_frame = cv2.warpPerspective(frame, matrix, (800, 400))
        ball_contour = detect_ball(warped_frame)

        if ball_contour is not None:
            M = cv2.moments(ball_contour)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                cv2.circle(warped_frame, (cx, cy), 10, (0, 255, 0), -1)

                region = get_ball_region(cy)
                if cy > last_y:
                    # Ball is moving down
                    if last_y < window_height - 10 and cy >= window_height - 10:
                        bounce_count += 1
                        bounces.append((bounce_count, video.get(cv2.CAP_PROP_POS_MSEC) / 1000, region, int(video.get(cv2.CAP_PROP_POS_FRAMES))))
                last_y = cy

        cv2.imshow('Warped Frame', warped_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

    # Save bounces to CSV
    df = pd.DataFrame(bounces, columns=['bounce_number', 'time_of_bounce', 'quadrant_of_bounce', 'frame_number'])
    df.to_csv('bounces.csv', index=False)

if __name__ == "__main__":
    main()
