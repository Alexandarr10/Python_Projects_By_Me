import pygame
import random

# Initialize Pygame
pygame.init()

# Set window size
window_size = (700, 500)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set title
pygame.display.set_caption("Basketball Game")

# Load basket image
basket_image = pygame.image.load("basket.png")

# Get basket image rect
basket_rect = basket_image.get_rect()

# Set basket position
basket_rect.x = random.randint(0, window_size[0] - basket_rect.width)
basket_rect.y = random.randint(0, window_size[1] - basket_rect.height)

# Set ball position
ball_x = window_size[0] // 2
ball_y = window_size[1] // 2
ball_speed_x = 5
ball_speed_y = 5

# Set font
font = pygame.font.Font(None, 36)

# Set score
score = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for collisions with window borders
    if ball_x < 0 or ball_x > window_size[0]:
        ball_speed_x = -ball_speed_x
    if ball_y < 0 or ball_y > window_size[1]:
        ball_speed_y = -ball_speed_y

    # Check for collisions with basket
    if basket_rect.collidepoint(ball_x, ball_y):
        score += 1
        basket_rect.x = random.randint(0, window_size[0] - basket_rect.width)
        basket_rect.y = random.randint(0, window_size[1] - basket_rect.height)

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw basket
    screen.blit(basket_image, basket_rect)

    # Draw ball
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), 20)

    # Draw score
    score_text = font.render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
