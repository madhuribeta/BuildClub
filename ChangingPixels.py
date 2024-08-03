import cv2
import numpy as np

# Read the image
image = cv2.imread('OIP 2.jpeg')  # Replace 'input_image.jpg' with your image file path

# Check the dimension of the image
print('Image array dimension:', image.shape)

# Access a specific pixel at the 5th row and 5th column
pixel = image[5, 5]
print('A pixel at (5, 5):', pixel)

# Extract a small region from the image (top left corner with 10x10 pixels)
new_image = image[:10, :10]

# Split the channels
B = new_image[:, :, 0]
G = new_image[:, :, 1]
R = new_image[:, :, 2]

# Print the channels
print('Blue Channel')
print(B)
print('Green Channel')
print(G)
print('Red Channel')
print(R)