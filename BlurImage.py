import cv2
import matplotlib.pyplot as plt
import numpy as np

# Step 2: Read an image from a location
# Replace 'image_path.jpg' with the path to your image file
image_path = 'OIP 2.jpeg'
image = cv2.imread(image_path)

# Step 3: Convert the image from BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Apply a slight median blur
blurred_image = cv2.medianBlur(image_rgb, 5)

# Step 4: Display the original and processed images using Matplotlib
plt.figure(figsize=(10, 5))

# Original Image
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')

# Blurred Image
plt.subplot(1, 2, 2)
plt.title('Blurred Image')
plt.imshow(blurred_image)
plt.axis('off')

plt.show()