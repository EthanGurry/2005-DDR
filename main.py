import pygame
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
p1dict = {'left':2, 'down':1, 'up':0, 'right':3, 'left_down':8, 'right_down':5, 'left_up':6, 'right_up':7}
p2dict = {'left2':2, 'down2':1, 'up2':0, 'right2':3, 'left_down2':8, 'right_down2':5, 'left_up2':6, 'right_up2':7}



# Set up display
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("DDR Game")

# Set up clock/timing information
clock = pygame.time.Clock()

# Initialize video player
video_path = '12 frames test 01.mp4'
cap = cv2.VideoCapture(video_path)
frame_surfaces = []

# Read video data and turn it into pygame surfaces
read = True
#while read:
print('starting preload...')
preloaded = 3000
for i in range(preloaded):
    grabbed, frame = cap.read()
    if grabbed:
        # Convert the frame to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.transpose(frame, (1, 0, 2))  # Transpose to (width, height, channels)

        # Create a Pygame Surface from the frame
        frame_surfaces.append(pygame.surfarray.make_surface(frame))
    else:
        break
print('preload done!')


# Fonts for text
font = pygame.font.SysFont('Alagard', 60)

# Start screen function
def start_screen():
    screen.fill((0, 0, 0))  # Fill the screen with black
    title_text = font.render('2005 CO. ', True, (255, 255, 255))
    start_text = font.render('Press start', True, (255, 255, 255))
    
    # Get the rectangle for centering
    title_rect = title_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
    start_rect = start_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
    
    screen.blit(title_text, title_rect)
    screen.blit(start_text, start_rect)
    
    pygame.display.flip()
    
    # Wait for start key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.JOYBUTTONDOWN and event.button == 9:
                print('pressed start')
                waiting = False


print("About to start")
# Run the start screen
start_screen()

# Arrow Manager
arrow_manager = ArrowManager(screen)

# make hitbox
hitbox = pygame.image.load('assets/hitbox.png')
# Main game loop
running = True
start_time = time.time()
i = 0
while running:
    current_time = time.time() - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    # Read a frame from the video
    if preloaded <= 0:
        grabbed, frame = cap.read()
        frame_surface = None
        if grabbed:
            # Convert the frame to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.transpose(frame, (1, 0, 2))  # Transpose to (width, height, channels)

            # Create a Pygame Surface from the frame
            frame_surface = pygame.surfarray.make_surface(frame)
    

    # loop through notes to see if an arrow is ready to spawn
    for x in notes:
        # checking when and where to spawn an arrow
        if current_time >= x[3]:  # When it's time to play this note
            direction = x[1]
            if current_time >= 576:
                arrow_manager.random_spawn(direction, screen_height)
                notes.remove(x)
            else:
                arrow_manager.spawn_arrow(direction, screen_width, screen_height)
                notes.remove(x)

    # Update game state
    arrow_manager.update()
    
 
    # check for collision
    arrow_manager.check_collision(pygame, joystick1, joystick2, txtRndr)
    

    # Draw everything
    screen.fill((0, 0, 0))  # Clear screen
    
    # Display the frame on the screen
    if preloaded > 0 and frame_surfaces[i] != None:
        screen.blit(frame_surfaces[i], (0, 0)) 
    else:
        screen.blit(frame_surface, (0, 0))
    
    txtRndr.render(screen)
    screen.blit(hitbox, (0, 0)) # draw hitbox
    arrow_manager.draw()
    pygame.display.flip()
    clock.tick(10)  # Maintain 30 FPS
    i += 1 # increase counter for img sequence
    preloaded -= 1 # decrease counter for how many frames are preloaded


cap.release()
pygame.quit()
