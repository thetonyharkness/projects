#!/bin/python3

import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake and food variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (width//10)) * 10,
            random.randrange(1, (height//10)) * 10]
food_spawn = True

# Direction
direction = 'RIGHT'
change_to = direction

# Speed and clock
speed = 20
clock = pygame.time.Clock()

# Game Over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    length = len(snake_body) - 3  # Calculate the snake's length
    game_over_surface = my_font.render('Your Score is: {}'.format(length), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (width/2, height/4)
    screen.fill(black)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.quit()
    quit()

# Main function
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validation of direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()
    
    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10,
                    random.randrange(1, (height//10)) * 10]
    food_spawn = True

    # Draw snake and food
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] > width-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > height-10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    # Update the display
    pygame.display.update()
    clock.tick(speed)
