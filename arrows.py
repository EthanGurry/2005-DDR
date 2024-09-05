import pygame
import time
from textRenderer import TextRenderer


# Game settings
BPM = 115
target_y = 100  # Y-position where arrows need to match

# Arrow settings
arrow_start_y = 0  # Starting Y-position at the top of the screen
arrow_height = 50  # Height of the arrow image
distance_to_target = target_y - arrow_start_y

# Calculate time per beat in seconds
time_per_beat = 60 / BPM

# Calculate speed in pixels per frame
frames_per_beat = 30 * time_per_beat
speed_pixels_per_frame = distance_to_target / frames_per_beat

'''
# Function to render and display text
def render_text(screen, text, position, duration=0.5, color=(255, 255, 255), font_size=36):
    font = pygame.font.SysFont('Arial', font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)
    pygame.display.flip()
    time.sleep(duration)  # Display text for the specified duration
    '''

class Arrow(pygame.sprite.Sprite):
    def __init__(self, image, position, direction):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.direction = direction
        self.speed = 2

    # method to show miss text above corresponding arrow
    def miss(self, txtRndr, duration=0.75, color=(255,0,0)):
        txtRndr.show_text("MISS!", (self.rect.x, 75), duration, color )
    
    def update(self):
        self.rect.y -= speed_pixels_per_frame
        if self.rect.y < 0:
            self.kill()  # Remove the arrow when it goes off-screen

class ArrowManager:
    def __init__(self, screen):
        self.screen = screen
        self.arrows = pygame.sprite.Group()

    def add(self, x, y, direction):
        img =  'assets/arrows/100-pixels/' + direction + '.png'
        arrow = Arrow(img, (x,y), direction)
        self.arrows.add(arrow)

    def spawn_arrow(self, direction, x, y):
       # Determine position based on direction
        if direction == "left_down":
            x = 100
        elif direction == "left":
            x = 200
        elif direction == "left_up":
            x = 300
        elif direction == "up":
            x = 400
        elif direction == "down":
            x = 500
        elif direction == "right_up":
            x = 600
        elif direction == "right":
            x = 700
        elif direction == "right_down":
            x = 800
        elif direction == "left_down2":
            x = 1020
        elif direction == "left2":
            x = 1120
        elif direction == "left_up2":
            x = 1220
        elif direction == "up2":
            x = 1320
        elif direction == "down2":
            x = 1420
        elif direction == "right_up2":
            x = 1520
        elif direction == "right2":
            x = 1620
        elif direction == "right_down2":
            x = 1720
        self.add(x, y, direction)

    def update(self):
        self.arrows.update()

    def draw(self):
        self.arrows.draw(self.screen)


    def check_collision(self, pygame, joy1, joy2, txtRndr):
        for arrow in self.arrows:
            if abs(arrow.rect.y - 75) < 75:
                # Collision detected - check if the correct key is pressed
                 
                joystick1_pressed = None
                if joy1:
                    if joy1.get_button(0):  
                        joystick1_pressed = "left"
                    elif joy1.get_button(1):  
                        joystick1_pressed = "down"
                    elif joy1.get_button(2): 
                        joystick1_pressed = "up"
                    elif joy1.get_button(3): 
                        joystick1_pressed = "right"
                    elif joy1.get_button(4): 
                        joystick1_pressed = "left_down"
                    elif joy1.get_button(5): 
                        joystick1_pressed = "right_down"
                    elif joy1.get_button(6): 
                        joystic1_pressed = "left_up"
                    elif joy1.get_button(7): 
                        joystick1_pressed = "right_up"
                    elif joy1.get_button(8): 
                        joystick1_pressed = "select"
                    elif joy1.get_button(9): 
                        joystick1_pressed = "back"

                joystick2_pressed = None
                if joy2:
                    if joy2.get_button(0):  
                        joystick2_pressed = "left2"
                    elif joy2.get_button(1):  
                        joystick2_pressed = "down2"
                    elif joy2.get_button(2): 
                        joystick2_pressed = "up2"
                    elif joy2.get_button(3): 
                        joystick2_pressed = "right2"
                    elif joy2.get_button(4): 
                        joystick2_pressed = "left_down2"
                    elif joy2.get_button(5): 
                        joystick2_pressed = "right_down2"
                    elif joy2.get_button(6): 
                        joystic1_pressed = "left_up2"
                    elif joy2.get_button(7): 
                        joystick2_pressed = "right_up2"
                    elif joy2.get_button(8): 
                        joystick2_pressed = "select2"
                    elif joy2.get_button(9): 
                        joystick2_pressed = "back2"
                        
                 
                 # Check for collision with the correct input for player 1
                if arrow.direction == "left" and joystick1_pressed == "left":
                    txtRndr.show_text("HIT!", (200, 75))
                    self.arrows.remove(arrow)
                elif arrow.direction == "down" and joystick1_pressed == "down":
                    txtRndr.show_text("HIT!", (500, 75))
                    self.arrows.remove(arrow)
                elif arrow.direction == "up" and joystick1_pressed == "up":
                    txtRndr.show_text("HIT!", (400, 75))
                    self.arrows.remove(arrow)
                elif arrow.direction == "right" and joystick1_pressed == "right":
                    txtRndr.show_text("HIT!", (700, 75))
                    self.arrows.remove(arrow)
                elif arrow.direction == "left_down" and joystick1_pressed == "left_down":
                    txtRndr.show_text("HIT!", (100, 75))
                    self.arrows.remove(arrow)
                elif arrow.direction == "right_down" and joystick1_pressed == "right_down":
                    txtRndr.show_text("HIT!", (800, 75))
                    self.arrows.remove(arrow)
                elif arrow.direction == "left_up" and joystick1_pressed == "left_up":
                    txtRndr.show_text("HIT!", (300, 75))
                elif arrow.direction == "right_up" and joystick1_pressed == "right_up":
                    txtRndr.show_text("HIT!", (600, 75))
                    self.arrows.remove(arrow)

                # Check for collision with the correct input for player 2
                if arrow.direction == "left2" and joystick2_pressed == "left2":
                    txtRndr.show_text("HIT!", (1120, 75))
                    self.arrows.remove(arrow)
                elif arrow.direction == "down2" and joystick2_pressed == "down2":
                    txtRndr.show_text("HIT!", (1420, 75))
                    self.arrows.remove(arrow)
                elif arrow.direction == "up2" and joystick2_pressed == "up2":
                    txtRndr.show_text("HIT!", (1320, 75))
                    self.arrows.remove(arrow)
                elif arrow.direction == "right2" and joystick2_pressed == "right2":
                    txtRndr.show_text("HIT!", (1620, 75))
                    self.arrows.remove(arrow)
                elif arrow.direction == "left_down2" and joystick2_pressed == "left_down2":
                    txtRndr.show_text("HIT!", (1020, 75))
                    self.arrows.remove(arrow)
                elif arrow.direction == "right_down2" and joystick2_pressed == "right_down2":
                    txtRndr.show_text("HIT!", (1720, 75))
                    self.arrows.remove(arrow)
                elif arrow.direction == "left_up2" and joystick2_pressed == "left_up2":
                    txtRndr.show_text("HIT!", (1220, 75))
                elif arrow.direction == "right_up2" and joystick2_pressed == "right_up2":
                    txtRndr.show_text("HIT!", (1520, 75))
                    self.arrows.remove(arrow)      

            elif arrow.rect.y < 100:
                arrow.miss(txtRndr) # generates miss text
                self.arrows.remove(arrow)







