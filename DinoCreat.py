import cv2
import numpy as np
import random

# Game settings
window_width = 800
window_height = 400
dino_radius = 20
obstacle_width = 20
obstacle_height = 50
initial_obstacle_speed = 5
gravity = 1
jump_strength = 15
speed_increment = 0.01  # Speed increment factor

# Initialize game state
dino_y = window_height - dino_radius - 10
dino_velocity = 0
obstacles = []
score = 0
game_over = False
obstacle_speed = initial_obstacle_speed

def create_obstacle():
    x = window_width
    y = window_height - obstacle_height - 10
    return [x, y]

def draw_game(image, dino_y, obstacles, score):
    # Clear the screen
    image[:] = (255, 255, 255)

    # Draw the dino
    cv2.circle(image, (50, int(dino_y)), dino_radius, (0, 0, 255), -1)

    # Draw the obstacles
    for obstacle in obstacles:
        x1, y1 = int(obstacle[0]), int(obstacle[1])
        x2, y2 = int(obstacle[0] + obstacle_width), int(obstacle[1] + obstacle_height)
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), -1)

    # Draw the score
    cv2.putText(image, f'Score: {score}', (window_width - 200, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

def check_collision(dino_y, obstacles):
    for obstacle in obstacles:
        if obstacle[0] < 50 + dino_radius and obstacle[0] + obstacle_width > 50 - dino_radius:
            if dino_y + dino_radius > obstacle[1]:
                return True
    return False

# Create a window
cv2.namedWindow('Dino Game')

# Main game loop
while True:
    if not game_over:
        # Create a blank image
        image = np.ones((window_height, window_width, 3), dtype=np.uint8) * 255

        # Update dino position
        dino_y += dino_velocity
        dino_velocity += gravity

        # Keep dino on the ground
        if dino_y > window_height - dino_radius - 10:
            dino_y = window_height - dino_radius - 10
            dino_velocity = 0

        # Add new obstacles
        if len(obstacles) == 0 or obstacles[-1][0] < window_width - 200:
            obstacles.append(create_obstacle())

        # Move obstacles
        for obstacle in obstacles:
            obstacle[0] -= obstacle_speed

        # Remove off-screen obstacles
        obstacles = [obstacle for obstacle in obstacles if obstacle[0] > -obstacle_width]

        # Check for collisions
        if check_collision(dino_y, obstacles):
            game_over = True

        # Increment score
        score += 1

        # Increase obstacle speed gradually
        obstacle_speed = initial_obstacle_speed + speed_increment * (score // 100)

        # Draw game
        draw_game(image, dino_y, obstacles, score)

    else:
        cv2.putText(image, 'Game Over', (window_width // 2 - 100, window_height // 2), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3, cv2.LINE_AA)

    # Show the image
    cv2.imshow('Dino Game', image)

    # Handle key events
    key = cv2.waitKey(30) & 0xFF
    if key == ord('q'):
        break
    if key == ord(' ') and dino_y == window_height - dino_radius - 10:
        dino_velocity = -jump_strength

# Close the window
cv2.destroyAllWindows()
