import pygame
import random
import cv2
import numpy as np
from arrows import ArrowManager

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("DDR Game")
clock = pygame.time.Clock()

# Load the song
#pygame.mixer.music.load('5050.mp3')

# Initialize video player
video_path = 'AAU-Highlights.mp4'
cap = cv2.VideoCapture(video_path)

# Start the song
#pygame.mixer.music.play()

# Arrow Manager
arrow_manager = ArrowManager(screen)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read a frame from the video
    grabbed, frame = cap.read()

    if grabbed:
        # Convert the frame to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.transpose(frame, (1, 0, 2))  # Transpose to (width, height, channels)

        # Create a Pygame Surface from the frame
        frame_surface = pygame.surfarray.make_surface(frame)

        # Display the frame on the screen
        screen.blit(frame_surface, (0, 0))

    # Generate arrows randomly
    if random.randint(1, 20) == 1:  # Example condition to create an arrow
        direction = random.choice(["up", "down", "left", "right"])
        arrow_manager.spawn_arrow(direction)

    # Update game state
    arrow_manager.update()

    # Draw everything
    arrow_manager.draw()
    pygame.display.flip()
    clock.tick(30)  # Maintain 30 FPS

cap.release()
pygame.quit()
