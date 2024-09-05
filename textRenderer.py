import pygame
import time

class TextRenderer:
    def __init__(self, pyg):
        self.pygame = pyg
        self.pygame.font.init()
        self.font = self.pygame.font.SysFont('Alagard', 36)
        self.display_text = ""
        self.position = (0, 0)
        self.end_time = 0
        self.color = (255, 255, 255)

    def show_text(self, text, position, duration=0.75, color=(255, 255, 255)):
        self.display_text = text
        self.position = position
        self.color = color
        self.end_time = time.time() + duration

    def render(self, screen):
        if time.time() < self.end_time:
            text_surface = self.font.render(self.display_text, True, self.color)
            screen.blit(text_surface, self.position)
