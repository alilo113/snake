import pygame
import random

pygame.init()

# Set up the display
width, height = 300, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
green = (0, 255, 0)
red = (255, 0, 0)

# Snake properties
snake_size = 20
snake_segments = [(width // 2, height // 2)]  # List to store snake segments
snake_speed = 15  # Adjust the speed to a manageable pace
snake_dx, snake_dy = 0, 0  # Initial movement direction

# Apple properties
apple_size = 20

# Function to spawn the apple within the playable area
def spawn_apple():
    margin = 20  # Margin from the edges to spawn the apples
    apple_x = random.randint(margin, width - apple_size - margin)
    apple_y = random.randint(margin, height - apple_size - margin)
    return apple_x, apple_y

apple_x, apple_y = spawn_apple()

# Font setup
font = pygame.font.Font(None, 36)
white = (255, 255, 255)
score = 0

def display_text(text, x, y):
    text_surface = font.render(text, True, white)
    screen.blit(text_surface, (x, y))

def reset_game():
    global snake_segments, snake_dx, snake_dy, score, snake_speed
    snake_segments = [(width // 2, height // 2)]
    snake_dx, snake_dy = 0, 0
    score = 0
    snake_speed = 10

def eat_apple():
    global score, snake_speed
    score += 1
    # Add a new segment to the snake's body at the tail position
    snake_segments.append(snake_segments[-1])  # New segment added at the end, it will be updated in the next iteration
    if snake_speed < 20:
        snake_speed += 1

def check_self_collision():
    # Check if the head collides with any segment of the body
    for i in range(1, len(snake_segments)):
        if snake_segments[0] == snake_segments[i]:
            return True
    return False

# Function to handle the snake's direction change
def change_direction(dx, dy):
    global snake_dx, snake_dy
    # Avoid reversing the direction completely
    if (dx != 0 and snake_dx != 0) or (dy != 0 and snake_dy != 0):
        return  # Don't change direction if trying to move opposite to current direction
    snake_dx, snake_dy = dx, dy

# Game loop
running = True
clock = pygame.time.Clock()  # Clock object to control the frame rate
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_direction(-snake_speed, 0)
            elif event.key == pygame.K_RIGHT:
                change_direction(snake_speed, 0)
            elif event.key == pygame.K_UP:
                change_direction(0, -snake_speed)
            elif event.key == pygame.K_DOWN:
                change_direction(0, snake_speed)

    # Update the snake's segments
    for i in range(len(snake_segments) - 1, 0, -1):
        snake_segments[i] = (snake_segments[i - 1][0], snake_segments[i - 1][1])

    snake_segments[0] = (snake_segments[0][0] + snake_dx, snake_segments[0][1] + snake_dy)

    # Reset the game if snake goes beyond the screen or collides with itself
    if (
        snake_segments[0][0] < 0 or snake_segments[0][0] >= width or
        snake_segments[0][1] < 0 or snake_segments[0][1] >= height or
        check_self_collision()
    ):
        reset_game()
        apple_x, apple_y = spawn_apple()  # Respawn the apple within the playable area

    # Check if the snake eats the apple
    if snake_segments[0][0] <= apple_x <= snake_segments[0][0] + snake_size and snake_segments[0][1] <= apple_y <= snake_segments[0][1] + snake_size:
        eat_apple()
        apple_x, apple_y = spawn_apple()  # Respawn the apple within the playable area

    # Draw the snake
    for segment in snake_segments:
        pygame.draw.rect(screen, green, (segment[0], segment[1], snake_size, snake_size))

    # Draw the apple
    pygame.draw.circle(screen, red, (apple_x, apple_y), apple_size // 2)

    display_text("Score: " + str(score), 10, 10)

    pygame.display.flip()
    clock.tick(13)  # Control the frame rate to manage the snake's speed

pygame.quit()