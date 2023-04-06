import pygame

BOARD_WIDTH = 400
SCREEN_WIDTH = 700
HEIGHT = 800
BLOCK = 40


class Buttons:

    def __init__(self, screen):
        self.screen = screen

    def resume(self):
        return self.template('Press space to resume!', BOARD_WIDTH//2, HEIGHT//2)

    def game_over(self):
        return self.template('Game over! Press space to restart!', BOARD_WIDTH//2, HEIGHT//2)

    def start(self):
        return self.template('Press space to start!', SCREEN_WIDTH//2,HEIGHT//2)
    
    def template(self, text, x, y):
        font = pygame.font.Font('freesansbold.ttf', 20)
        text_1 = font.render(text, True, (0, 0, 0), (255, 255, 255))
        rectangle = text_1.get_rect()
        rectangle.center = (x,y)
        self.screen.blit(text_1, rectangle)
