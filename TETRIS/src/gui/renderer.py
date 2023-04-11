import pygame
from src.gui.buttons.buttons import Buttons

WIDTH = 400
HEIGHT = 800
BLOCK = 40

BACKROUND = (99, 99, 99)
LINE = (128, 128, 128)


class Renderer:

    def __init__(self, screen, tetris):
        self.screen = screen
        self.tetris = tetris
        self.button = Buttons(self.screen)

    def render_backround_game(self):
        self.screen.fill(BACKROUND)
        for x in range(0, WIDTH, BLOCK):
            pygame.draw.line(self.screen, (LINE), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, BLOCK):
            pygame.draw.line(self.screen, (LINE), (0, y), (WIDTH, y))
        pygame.draw.line(self.screen, (0, 0, 0),
                         (WIDTH, 0), (WIDTH, HEIGHT), 2)

    def render_piece(self):
        piece_coordinates = self.tetris.piece.piece_info()
        for coordinate in piece_coordinates:
            pygame.draw.rect(self.screen, self.tetris.piece.color,
                             (self.tetris.piece.x_coordinate + coordinate[0]*BLOCK,
                              self.tetris.piece.y_coordinate +
                              coordinate[1]*BLOCK,
                              BLOCK, BLOCK), 0, 4)
            pygame.draw.rect(self.screen, (0, 0, 0),
                             (self.tetris.piece.x_coordinate + coordinate[0]*BLOCK,
                             self.tetris.piece.y_coordinate +
                                 coordinate[1]*BLOCK,
                             BLOCK, BLOCK), 3, 4)

    def render_previous_pieces(self):
        for y in range(20):
            for x in range(10):
                color = self.tetris.board[y][x]
                if color == 0:
                    continue
                pygame.draw.rect(self.screen, color,
                                 (BLOCK*x, BLOCK*y, BLOCK, BLOCK), 0, 4)
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 (BLOCK*x, BLOCK*y, BLOCK, BLOCK), 3, 4)

    def render_all(self, pause, end):
        self.render_backround_game()
        self.render_piece()
        self.render_previous_pieces()
        if pause:
            self.button.resume()
        if end:
            self.button.game_over()

        pygame.display.update()

    def render_menu(self):
        self.screen.fill(BACKROUND)
        self.button.start()
        pygame.display.update()
