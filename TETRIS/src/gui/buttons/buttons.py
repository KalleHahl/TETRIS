import pygame
from src.settings import BOARD_WIDTH, HEIGHT, WIDTH


class Buttons:

    def __init__(self, screen):
        self.screen = screen

    def resume(self):
        return self.template('Press space to resume!', BOARD_WIDTH//2, HEIGHT//2)

    def game_over(self):
        return self.template('Game over! Press space to restart!', BOARD_WIDTH//2, HEIGHT//2)

    def start(self):
        return self.template('Press space to start!', WIDTH//2, HEIGHT//2)

    def next_piece(self):
        return self.template('Next piece', WIDTH-150, 100)

    def score(self, score):
        return self.template(f'Score: {score}', WIDTH-150, 400)

    def template(self, text, x_coordinate, y_coordinate):
        font = pygame.font.Font('freesansbold.ttf', 20)
        text_1 = font.render(text, True, (0, 0, 0), (255, 255, 255))
        rectangle = text_1.get_rect()
        rectangle.center = (x_coordinate, y_coordinate)
        self.screen.blit(text_1, rectangle)
