import pygame

WIDTH = 400
HEIGHT = 800
BLOCK = 40


class Buttons:

    def __init__(self, screen):
        self.screen = screen

    def resume(self):
        return self.template('Press space to resume!')

    def game_over(self):
        return self.template('Game over! Press space for new game!')

    def template(self, text):
        font = pygame.font.Font('freesansbold.ttf', 16)
        text_1 = font.render(text, True, (0, 0, 0), (255, 255, 255))
        rectangle = text_1.get_rect()
        rectangle.center = (WIDTH//2, HEIGHT//2)
        self.screen.blit(text_1, rectangle)
