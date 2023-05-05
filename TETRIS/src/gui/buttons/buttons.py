import pygame
from src.settings import HEIGHT, WIDTH


class Buttons:

    def __init__(self, screen):
        self.screen = screen

    def resume(self):
        return self._template('Press escape to resume!', WIDTH//2, HEIGHT//2,40)

    def game_over(self):
        return self._template('Game over',WIDTH//2, HEIGHT//4,100)

    def start(self):
        return self._template('Press space to start!', WIDTH//2, HEIGHT//2,40)

    def next_piece(self):
        return self._template('Next piece', WIDTH-150, 100,40)

    def score(self, score):
        return self._template(f'Score: {score}', WIDTH-150, 400,40)

    def score_saved(self):
        return self._template('Score saved!', WIDTH//2, HEIGHT//2,40)

    def enter_name(self):
        return self._template('Enter name:', WIDTH//2, HEIGHT//2-20, 30)

    def _template(self, text, x_coordinate, y_coordinate, size):
        font = pygame.font.Font('freesansbold.ttf', size)
        text_1 = font.render(text, True, (220, 220, 220), (0, 0,0))
        rectangle = text_1.get_rect()
        rectangle.center = (x_coordinate, y_coordinate)
        self.screen.blit(text_1, rectangle)

    def user_input(self, player):
        text = pygame.font.Font('freesansbold.ttf', 20)
        player_name = text.render(player, True, (255, 255, 255))
        rect_width = max(200, player_name.get_width() + 15)
        input_rect = pygame.Rect(WIDTH//2-rect_width //
                                 2, HEIGHT//2, rect_width, 32)
        pygame.draw.rect(self.screen, (255, 255, 255), input_rect, 2)
        self.screen.blit(player_name, (input_rect.x+5, input_rect.y+5))
