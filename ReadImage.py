import cv2

# Relative or absolute path of the input image file
path = "OIP.jpeg"

# Reading image (by default the flag is 1 if not specified)
image = cv2.imread(path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:
    # Display image in a window
    cv2.imshow("Output", image)

    # Wait until any key press (press any key to close the window)
    cv2.waitKey()

    # Kill all the windows
    cv2.destroyAllWindows()