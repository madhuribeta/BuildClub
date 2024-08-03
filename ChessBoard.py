import cv2
import numpy as np

# Define the size of the chessboard
rows, cols = 4, 4
square_size = 100  # Size of each square in pixels

# Create an empty image
board_size = rows * square_size
chessboard = np.zeros((board_size, board_size, 3), dtype=np.uint8)

# Fill the chessboard with alternating colors
for row in range(rows):
    for col in range(cols):
        start_x = col * square_size
        start_y = row * square_size
        end_x = start_x + square_size
        end_y = start_y + square_size
        
        if (row + col) % 2 == 0:
            color = (255, 255, 255)  # White
        else:
            color = (0, 0, 0)  # Black
        
        cv2.rectangle(chessboard, (start_x, start_y), (end_x, end_y), color, -1)

# Display the chessboard
cv2.imshow('4x4 Chessboard', chessboard)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the chessboard image
cv2.imwrite('4x4_chessboard.png', chessboard)