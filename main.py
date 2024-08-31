import pygame
import random
from Arrow import Arrow
import cv2
import numpy as np
pygame.init()


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('2005 CO.')
clock = pygame.time.Clock()

print("making start screen")

# Fonts for text
font = pygame.font.SysFont('Arial', 60)

# Start screen function
def start_screen():
    screen.fill((0, 0, 0))  # Fill the screen with black
    title_text = font.render('2005 CO. ', True, (255, 255, 255))
    start_text = font.render('Press any key to start', True, (255, 255, 255))
    
    # Get the rectangle for centering
    title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    start_rect = start_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
    
    screen.blit(title_text, title_rect)
    screen.blit(start_text, start_rect)
    
    pygame.display.flip()
    
    # Wait for any key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

print("About to start")
# Run the start screen
start_screen()

# Arrow setup
arrow_images = {
    "up": pygame.image.load('up.png'),
    "down": pygame.image.load('down.png'),
    "left": pygame.image.load('left.png'),
    "right": pygame.image.load('right.png')
}
arrows = pygame.sprite.Group()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate arrows randomly
    if random.randint(1, 20) == 1:  # Example condition to create an arrow
        direction = random.choice(["up", "down", "left", "right"])
        arrow = Arrow(direction, 400, 600)
        arrows.add(arrow)

    # Update
    arrows.update()


    # Draw everything
    screen.fill((0, 0, 0))
    arrows.draw(screen)
    pygame.display.flip()

    clock.tick(30)  # Maintain 30 FPS

pygame.quit()