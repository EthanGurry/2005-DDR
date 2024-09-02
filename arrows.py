import pygame

class Arrow(pygame.sprite.Sprite):
    def __init__(self, image, position, direction):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.direction = direction
        self.speed = 2
    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()  # Remove the arrow when it goes off-screen

class ArrowManager:
    def __init__(self, screen):
        self.screen = screen
        self.arrows = pygame.sprite.Group()

    def spawn_arrow(self, direction):
       # Determine position based on direction
        if direction == "up":
            position = (100, 599)
        elif direction == "down":
            position = (200, 599)
        elif direction == "left":
            position = (300, 599)
        elif direction == "right":
            position = (400, 599)
        else:
            position = (0, 599)  # Default position for unknown direction
        arrow = Arrow('arrow.png', position, direction)
        self.arrows.add(arrow)

    def update(self):
        self.arrows.update()

    def draw(self):
        self.arrows.draw(self.screen)
