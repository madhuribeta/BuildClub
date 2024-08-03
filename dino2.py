import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GROUND_HEIGHT = SCREEN_HEIGHT - 70
GRAVITY = 0.6
JUMP_STRENGTH = -12

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dino Game')

# Load images
dino_image = pygame.image.load('dino.png')  # Ensure you have a valid path to the image
cactus_image = pygame.image.load('cactus.png')  # Ensure you have a valid path to the image

# Dino class
class Dino:
    def __init__(self):
        self.image = dino_image
        self.x = 50
        self.y = GROUND_HEIGHT - self.image.get_height()
        self.vel_y = 0
        self.jumping = False

    def jump(self):
        if not self.jumping:
            self.vel_y = JUMP_STRENGTH
            self.jumping = True

    def update(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y

        if self.y > GROUND_HEIGHT - self.image.get_height():
            self.y = GROUND_HEIGHT - self.image.get_height()
            self.jumping = False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Cactus class
class Cactus:
    def __init__(self):
        self.image = cactus_image
        self.x = SCREEN_WIDTH
        self.y = GROUND_HEIGHT - self.image.get_height()

    def update(self):
        self.x -= 10

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def off_screen(self):
        return self.x < -self.image.get_width()

# Main game function
def game():
    clock = pygame.time.Clock()
    dino = Dino()
    cacti = []
    score = 0

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump()

        dino.update()

        if random.randint(1, 60) == 1:
            cacti.append(Cactus())

        for cactus in cacti:
            cactus.update()
            if cactus.off_screen():
                cacti.remove(cactus)
                score += 1

        for cactus in cacti:
            if dino.x + dino.image.get_width() > cactus.x and dino.x < cactus.x + cactus.image.get_width():
                if dino.y + dino.image.get_height() > cactus.y:
                    running = False

        dino.draw(screen)
        for cactus in cacti:
            cactus.draw(screen)

        # Draw ground
        pygame.draw.line(screen, BLACK, (0, GROUND_HEIGHT), (SCREEN_WIDTH, GROUND_HEIGHT), 2)

        # Draw score
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    game()
