import pygame

class Arrow(pygame.sprite.Sprite):
    def __init__(self, direction, x, y):
        super().__init__()
        self.image = pygame.image.load(f"{direction}.png") 
        self.rect = self.image.get_rect(center=(x, y))
        self.direction = direction
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()  # Remove the arrow when it goes off-screen
        