import pygame

WIDTH = 400
HEIGHT = 800
BLOCK = 40

class Buttons:

    def __init__(self, screen):
        self.screen = screen
    
    def resume(self):
        return self.template('Resume')
    
    def template(self, text):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text_1 = font.render(text, True, (0,0,0), (255,255,255))
        textRect = text_1.get_rect()
        textRect.center = (WIDTH//2, HEIGHT//2)
        self.screen.blit(text_1, textRect)
