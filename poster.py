# Step 1: Import necessary packages
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Step 2: Read an image from a location
# Replace 'image_path.jpg' with the path to your image file
image_path = 'OIP 3.jpeg'
image = cv2.imread(image_path)

# Step 3: Convert the image from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Apply a slight median blur
blurred_image = cv2.medianBlur(image_rgb, 5)

# Step 4: Create a Look-Up Table to map pixel values
n = 4  # Number of levels for posterization
LUT = np.zeros(256, dtype=np.uint8)
step = 256 // n
for i in range(256):
    LUT[i] = (i // step) * step

# Step 5: Map input image pixel values according to the Look Up Table using LUT function
posterized_image = cv2.LUT(blurred_image, LUT)

# Step 6: Display the original and posterized images side-by-side using Matplotlib
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

# Posterized Image
plt.subplot(1, 2, 2)
plt.title('Posterized Image')
plt.imshow(posterized_image)
plt.axis('off')

plt.show()
