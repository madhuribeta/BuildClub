import cv2
import numpy as np

# Load the image
image = cv2.imread('OIP 3.jpeg')

# Function to apply filters using ColorMaps in OpenCV
def apply_colormap(image, colormap):
    return cv2.applyColorMap(image, colormap)

# Function to zoom the image
def zoom(image, zoom_factor):
    height, width = image.shape[:2]
    centerX, centerY = width // 2, height // 2
    radiusX, radiusY = int(width // (2 * zoom_factor)), int(height // (2 * zoom_factor))

    minX, maxX = centerX - radiusX, centerX + radiusX
    minY, maxY = centerY - radiusY, centerY + radiusY

    cropped = image[minY:maxY, minX:maxX]
    return cv2.resize(cropped, (width, height))

# Function to rotate the image
def rotate(image, angle):
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)
    return cv2.warpAffine(image, rotation_matrix, (width, height))

# Function to blur the image
def blur(image, ksize):
    return cv2.GaussianBlur(image, (ksize, ksize), 0)

# Function to apply sketch effect (edge detection)
def sketch_effect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_gray = cv2.bitwise_not(gray)
    blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)
    inverted_blurred = cv2.bitwise_not(blurred)
    sketch = cv2.divide(gray, inverted_blurred, scale=256.0)
    return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

# Function to crop the image
def crop(image, startX, startY, endX, endY):
    return image[startY:endY, startX:endX]

# Apply filter
filtered_image = apply_colormap(image, cv2.COLORMAP_JET)

# Zoom the image
zoomed_image = zoom(filtered_image, 1.5)

# Rotate the image
rotated_image = rotate(zoomed_image, 45)

# Blur the image
blurred_image = blur(rotated_image, 5)

# Apply sketch effect
sketched_image = sketch_effect(blurred_image)

# Crop the image
cropped_image = crop(sketched_image, 50, 50, 300, 300)

# Save the cropped image
cv2.imwrite('cropped_image.jpg', cropped_image)

# Display the final image
cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()