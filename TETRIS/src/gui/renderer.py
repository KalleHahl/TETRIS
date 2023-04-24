import pygame
from src.gui.buttons.buttons import Buttons

BOARD_WIDTH = 400
BOARD_HEIGHT = 800
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
        for x_coordinate in range(0, BOARD_WIDTH, BLOCK):
            pygame.draw.line(self.screen, (LINE), (x_coordinate, 0), (x_coordinate, BOARD_HEIGHT))
        for y_coordinate in range(0, BOARD_HEIGHT, BLOCK):
            pygame.draw.line(self.screen, (LINE), (0, y_coordinate), (BOARD_WIDTH, y_coordinate))
        pygame.draw.line(self.screen, (0, 0, 0),
                         (BOARD_WIDTH, 0), (BOARD_WIDTH, BOARD_HEIGHT), 2)

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

    def render_next_piece(self):
        next_coordinates = self.tetris.next_piece.piece_info()
        for coordinate in next_coordinates:
            pygame.draw.rect(self.screen, self.tetris.next_piece.color,
                             (525 + coordinate[0]*BLOCK, 200 + coordinate[1]*BLOCK,
                              BLOCK, BLOCK), 0, 4)
            pygame.draw.rect(self.screen, (0, 0, 0),
                             (525 + coordinate[0]*BLOCK, 200 + coordinate[1]*BLOCK,
                             BLOCK, BLOCK), 3, 4)

    def render_previous_pieces(self):
        for y_coordinate in range(20):
            for x_coordinate in range(10):
                color = self.tetris.board[y_coordinate][x_coordinate]
                if color == 0:
                    continue
                pygame.draw.rect(self.screen, color,
                                 (BLOCK*x_coordinate, BLOCK*y_coordinate, BLOCK, BLOCK), 0, 4)
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 (BLOCK*x_coordinate, BLOCK*y_coordinate, BLOCK, BLOCK), 3, 4)

    def render_all(self, pause, end):
        self.render_backround_game()
        self.render_piece()
        self.render_next_piece()
        self.render_previous_pieces()
        self.button.next_piece()
        self.button.score(self.tetris.score)

        if pause:
            self.button.resume()
        if end:
            self.button.game_over()

        pygame.display.update()

    def render_menu(self):
        self.screen.fill(BACKROUND)
        self.button.start()
        pygame.display.update()
