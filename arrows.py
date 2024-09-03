import pygame

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

class Arrow(pygame.sprite.Sprite):
    def __init__(self, image, position, direction):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.direction = direction
        self.speed = 2
    
    def update(self):
        self.rect.y -= speed_pixels_per_frame
        if self.rect.y < 0:
            self.kill()  # Remove the arrow when it goes off-screen

class ArrowManager:
    def __init__(self, screen):
        self.screen = screen
        self.arrows = pygame.sprite.Group()

    def spawn_arrow(self, direction, x, y):
       # Determine position based on direction
        if direction == "left_down":
            position = (30, y)
        elif direction == "left":
            position = (94, y)
        elif direction == "left_up":
            position = (158, y)
        elif direction == "up":
            position = (222, y)
        elif direction == "down":
            position = (286, y)
        elif direction == "right_up":
             position = (350, y)
        elif direction == "right":
            position = (414, y)
        elif direction == "right_down":
            position = (478, y)
        elif direction == "left_down2":
            position = (898, y)
        elif direction == "left2":
            position = (962, y)
        elif direction == "left_up2":
            position = (1026, y)
        elif direction == "up2":
            position = (1090, y)
        elif direction == "down2":
            position = (1154, y)
        elif direction == "right_up2":
             position = (1218, y)
        elif direction == "right2":
            position = (1282, y)
        elif direction == "right_down2":
            position = (1346, y)
        arrow = Arrow('arrow.png', position, direction)
        self.arrows.add(arrow)

    def update(self):
        self.arrows.update()

    def add(self, x, y, direction):
        arrow = Arrow('down.png', (x,y), direction)
        self.arrows.add(arrow)

    def draw(self):
        self.arrows.draw(self.screen)

    def check_collision(self, pygame):
        for arrow in self.arrows:
            if abs(arrow.rect.y - 100) < 50:
                # Collision detected - check if the correct key is pressed
                keys = pygame.key.get_pressed()
                if arrow.direction == "left" and keys[pygame.K_LEFT]:
                    print("Left arrow hit!")
                    self.arrows.remove(arrow)
                elif arrow.direction == "right" and keys[pygame.K_RIGHT]:
                    print("Right arrow hit!")
                    self.arrows.remove(arrow)
                elif arrow.direction == "up" and keys[pygame.K_UP]:
                    print("Up arrow hit!")
                    self.arrows.remove(arrow)
                elif arrow.direction == "down" and keys[pygame.K_DOWN]:
                    print("Down arrow hit!")
                    self.arrows.remove(arrow)
            elif arrow.rect.y < 100:
                print("MISSED!!!!")
                self.arrows.remove(arrow)


