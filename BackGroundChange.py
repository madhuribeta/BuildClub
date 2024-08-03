import cv2
import numpy as np

def remove_green_screen(frame, background):
    # Convert the frame to the HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the green color range
    lower_green = np.array([35, 40, 40])
    upper_green = np.array([85, 255, 255])
    
    # Create a mask for the green color
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    # Invert the mask
    mask_inv = cv2.bitwise_not(mask)
    
    # Use the mask to extract the foreground (non-green screen areas)
    fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    # Use the inverse mask to extract the background area
    bg = cv2.bitwise_and(background, background, mask=mask)
    
    # Combine the foreground and the new background
    result = cv2.add(fg, bg)
    
    return result

def main():
    # Capture video from the webcam
    cap = cv2.VideoCapture(0)

    # Load the background image and resize it to match the video resolution
    background = cv2.imread('OIP 2.jpeg')
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture video")
        return
    
    background = cv2.resize(background, (frame.shape[1], frame.shape[0]))

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Remove green screen and replace with background
        result = remove_green_screen(frame, background)
        
        # Display the result
        cv2.imshow('Green Screen Removal', result)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()