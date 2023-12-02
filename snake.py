import pygame
import random

pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
green = (0, 255, 0)
red = (255, 0, 0)

# Snake properties
snake_size = 20
snake_x, snake_y = width // 2, height // 2  # Starting position of the snake
snake_speed = 0.8
snake_dx, snake_dy = 0, 0  # Initial movement direction

# Apple properties
apple_size = 20
apple_x, apple_y = random.randint(0, width - apple_size), random.randint(0, height - apple_size)  # Random position for the apple

# Font setup
font = pygame.font.Font(None, 36)  # You can change the font and size here
white = (255, 255, 255)  # Define color for the text
score = 0  # Initialize score counter

# Function to render text
def display_text(text, x, y):
    text_surface = font.render(text, True, white)
    screen.blit(text_surface, (x, y))

def reset_game():
    global snake_x, snake_y, snake_dx, snake_dy, apple_x, apple_y, score
    snake_x, snake_y = width // 2, height // 2
    snake_dx, snake_dy = 0, 0
    apple_x, apple_y = random.randint(0, width - apple_size), random.randint(0, height - apple_size)
    score = 0  # Reset score when the game resets

def eat_apple():
    global apple_x, apple_y, score
    apple_x, apple_y = random.randint(0, width - apple_size), random.randint(0, height - apple_size)
    score += 1  # Increment the score when the snake eats an apple

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Fill the screen with black

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -snake_speed
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = snake_speed
                snake_dy = 0
            elif event.key == pygame.K_UP:
                snake_dy = -snake_speed
                snake_dx = 0
            elif event.key == pygame.K_DOWN:
                snake_dy = snake_speed
                snake_dx = 0

    snake_x += snake_dx
    snake_y += snake_dy

    # Reset the game if snake goes beyond the screen
    if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
        reset_game()

    # Check if the snake eats the apple
    if snake_x <= apple_x <= snake_x + snake_size and snake_y <= apple_y <= snake_y + snake_size:
        eat_apple()

    # Draw the snake
    pygame.draw.rect(screen, green, (snake_x, snake_y, snake_size, snake_size))

    # Draw the apple
    pygame.draw.circle(screen, red, (apple_x, apple_y), apple_size // 2)

    # Render and display text in the top-left corner
    display_text("Score: " + str(score), 10, 10)  # Display the score

    pygame.display.flip()  # Update the screen

pygame.quit()