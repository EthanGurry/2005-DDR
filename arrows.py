import pygame
import time
import random
from textRenderer import TextRenderer

# Dictionary for direction to x coordinates
xdict = {'left':200, 'down':500, 'up':400, 'right':700, 'left_down':100, 'right_down':800, 'left_up':300, 'right_up':600,
         'left2':1120, 'down2':1420, 'up2':1320, 'right2':1620, 'left_down2':1020, 'right_down2':1720, 'left_up2':1220, 'right_up2':1520}
# Dictionary for direction to button index
p1dict = {'left':2, 'down':1, 'up':0, 'right':3, 'left_down':8, 'right_down':5, 'left_up':6, 'right_up':7}
p2dict = {'left2':2, 'down2':1, 'up2':0, 'right2':3, 'left_down2':8, 'right_down2':5, 'left_up2':6, 'right_up2':7}

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
        self.rect.y -= 12
        if self.rect.y < 10:
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
        x = xdict[direction]
        self.add(x, y, direction)
    
    def random_spawn(self, direction, y):
        xd = random.choice(["left_down", "left", "left_up", "up", "down", "right_up", "right", "right_down", "left_down2", "left2", "left_up2", "up2", "down2", "right_up2", "right2", "right_down2"])
        x = xdict[xd]
        self.add(x, y, direction)

    def update(self):
        self.arrows.update()

    def draw(self):
        self.arrows.draw(self.screen)

    def check_collision(self, pygame, joy1, joy2, txtRndr):
        for arrow in self.arrows:
            if abs(arrow.rect.y - 75) < 75:
                # Collision detected - check if the correct key is pressed
                index = None
                # checking if arrow is on p2's side
                if '2' in arrow.direction:
                    index = p2dict[arrow.direction]
                    if joy2.get_button(index):
                        txtRndr.show_text("HIT!", (xdict[arrow.direction], 75))
                        self.arrows.remove(arrow)
                else:
                    index = p1dict[arrow.direction]
                    if joy1.get_button(index):
                        txtRndr.show_text("HIT!", (xdict[arrow.direction], 75))
                        self.arrows.remove(arrow)
            elif arrow.rect.y < 100:
                arrow.miss(txtRndr) # generates miss text
                self.arrows.remove(arrow)
           
                





