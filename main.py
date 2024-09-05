import pygame
import random
import cv2
import numpy as np
from arrows import ArrowManager
from textRenderer import TextRenderer
import time
from midiConverter import notes

# BPM IS 115

# Initialize Pygame
pygame.init()
pygame.joystick.init()

# Create a text render object
txtRndr = TextRenderer(pygame)

# Create a joystick object
joystick1 = pygame.joystick.Joystick(0)
joystick1.init()

# Create a second joystick object
joystick2 = pygame.joystick.Joystick(1)
joystick2.init()

# Dictionary for direction to button index
p1dict = {'left':0, 'down':1, 'up':2, 'right':3, 'left_down':4, 'right_down':5, 'left_up':6, 'right_up':7}
p2dict = {'left2':0, 'down2':1, 'up2':2, 'righ2t':3, 'left_down2':4, 'right_down2':5, 'left_up2':6, 'right_up2':7}


# Set up display
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("DDR Game")

# Set up clock/timing information
clock = pygame.time.Clock()
start_time = time.time()

# Load the song
#pygame.mixer.music.load('5050.mp3')


# Initialize video player
video_path = 'AAU-Highlights.mp4'
cap = cv2.VideoCapture(video_path)

# Start the song
#pygame.mixer.music.play()



# Fonts for text
font = pygame.font.SysFont('Arial', 60)
"""
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
"""

# Arrow Manager
arrow_manager = ArrowManager(screen)

# make hitbox
hitbox = pygame.image.load('assets/hitbox.png')
x = True
# Main game loop
running = True
while running:
    current_time = time.time() - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    # Read a frame from the video
    grabbed, frame = cap.read()
    frame_surface = None

    if grabbed:
        # Convert the frame to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (screen_width, screen_height))
        frame = np.transpose(frame, (1, 0, 2))  # Transpose to (width, height, channels)

        # Create a Pygame Surface from the frame
        frame_surface = pygame.surfarray.make_surface(frame)
    

    # loop through notes to see if an arrow is ready to spawn
    for x in notes:
        # checking when and where to spawn an arrow
        if current_time >= x[3]:  # When it's time to play this note
            direction = x[1]
            arrow_manager.spawn_arrow(direction, screen_width, 1500)
            notes.remove(x)
        
            

    '''
    # Generate arrows randomly
    if random.randint(1, 20) == 1:  # Example condition to create an arrow
        direction = random.choice(["left_down", "left", "left_up", "up", "down", "right_up", "right", "right_down", "left_down2", "left2", "left_up2", "up2", "down2", "right_up2", "right2", "right_down2"])
        arrow_manager.spawn_arrow(direction, screen_width, screen_height)
    '''
    # Update game state
    arrow_manager.update()

    
    # check for collision
    arrow_manager.check_collision(pygame, joystick1, joystick2, txtRndr)
    

    # Draw everything
    screen.fill((0, 0, 0))  # Clear screen
    # Display the frame on the screen
    screen.blit(frame_surface, (0, 0)) 
    txtRndr.render(screen)
    screen.blit(hitbox, (0, 0)) # draw hitbox
    arrow_manager.draw()
    pygame.display.flip()
    clock.tick(30)  # Maintain 30 FPS



cap.release()
pygame.quit()
