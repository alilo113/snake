import sys
import pygame
import random

pygame.init()

# Screen setup
screen_Info = pygame.display.Info()
size = width, height = screen_Info.current_w, screen_Info.current_h
black = 0, 0, 0
screen = pygame.display.set_mode(size)

# Square parameters (snake)
square_size = 20
speed = 1
move_x, move_y = 0, 0
snake = [(width // 2, height // 2)]  # Snake segments, initially one segment

def reset_game():
    global move_x, move_y, snake, speed
    snake = [(width // 2, height // 2)]
    move_x, move_y = 0, 0
    speed = 1
    reset_apple_position()

def reset_apple_position():
    global apple_x, apple_y
    apple_x, apple_y = random.randint(square_size, width - square_size), random.randint(square_size, height - square_size)

# Initial setup
reset_game()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_x = -speed
                move_y = 0
            elif event.key == pygame.K_RIGHT:
                move_x = speed
                move_y = 0
            elif event.key == pygame.K_UP:
                move_x = 0
                move_y = -speed
            elif event.key == pygame.K_DOWN:
                move_x = 0
                move_y = speed

    # Update snake position based on the direction
    new_head = (snake[0][0] + move_x, snake[0][1] + move_y)
    snake.insert(0, new_head)

    # Check if the snake moves beyond the screen boundaries
    if snake[0][0] < 0 or snake[0][0] > width or snake[0][1] < 0 or snake[0][1] > height:
        reset_game()

    # Check for collision between snake and apple
    distance = ((apple_x - snake[0][0]) ** 2 + (apple_y - snake[0][1]) ** 2) ** 0.5
    if distance < square_size:
        reset_apple_position()
        speed += 0.001  # Increase speed
    else:
        snake.pop()  # If no collision, remove the last segment

    screen.fill(black)  # Fill the screen with black

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], square_size, square_size))

    # Draw the apple
    pygame.draw.circle(screen, (255, 0, 0), (apple_x, apple_y), square_size // 2)

    pygame.display.flip()  # Update the display

pygame.quit()
sys.exit()