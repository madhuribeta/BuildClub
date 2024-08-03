# Importing OpenCV Library
import cv2
# Relative or absolute path of the input image file
path = "OIP 3.jpeg"
# reading image (by default the flag is 1 if not specidied)
image = cv2.imread(path)
size = image.shape
width = int(size[0]/2)
height = int(size[1]/2)
image_resize = cv2.resize(image,(height,width))
# Display image in a window
cv2.imshow("Output",image)
cv2.imshow("Resize",image_resize)
# Wait until any key press (press any key to close the window)
cv2.waitKey()
# kill all the windows
cv2.destroyAllWindows()
