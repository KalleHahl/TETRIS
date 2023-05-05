import pygame
from src.gui.buttons.buttons import Buttons
from src.settings import BACKROUND, BOARD_WIDTH, BOARD_HEIGHT, LINE, BLOCK, WIDTH


class Renderer:

    def __init__(self, screen, tetris):
        self.screen = screen
        self.tetris = tetris
        self.button = Buttons(self.screen)
        self.player = ''

    def render_backround_game(self):
        self.screen.fill(BACKROUND)
        self.screen.fill((220,220,220), (BOARD_WIDTH, 0, BOARD_WIDTH, BOARD_HEIGHT))
        for x_coordinate in range(0, BOARD_WIDTH, BLOCK):
            pygame.draw.line(self.screen, (LINE),
                             (x_coordinate, 0), (x_coordinate, BOARD_HEIGHT))
        for y_coordinate in range(0, BOARD_HEIGHT, BLOCK):
            pygame.draw.line(self.screen, (LINE),
                             (0, y_coordinate), (BOARD_WIDTH, y_coordinate))
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

    def render_ghost(self):
        piece_coordinates = self.tetris.ghost.piece_info()
        for coordinate in piece_coordinates:

            pygame.draw.rect(self.screen, (0, 0, 0),
                             (self.tetris.ghost.x_coordinate + coordinate[0]*BLOCK,
                             self.tetris.ghost.y_coordinate +
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
        self.render_ghost()
        self.render_next_piece()
        self.render_previous_pieces()
        self.button.next_piece()
        self.button.score(self.tetris.score)

        if pause:
            self.blur()
            self.button.resume()
        if end:
            self.render_game_over()

        pygame.display.update()

    def render_menu(self):
        self.screen.fill(BACKROUND)
        self.button.start()
        pygame.display.update()

    def render_game_over(self):
        self.blur()
        self.render_user_input()
        #self.button.game_over()
    
    def blur(self):
        blur = pygame.Surface((WIDTH, BOARD_HEIGHT))
        blur.set_alpha(150)
        blur.fill((0,0,0))
        self.screen.blit(blur, (0,0))

    def render_user_input(self):
        text = pygame.font.Font('freesansbold.ttf', 20)
        player_name = text.render(self.player, True, (255,255,255))
        rect_width = max(100, player_name.get_width() + 15)
        input_rect = pygame.Rect(WIDTH//2-rect_width//2,BOARD_HEIGHT//2,rect_width,32)
        pygame.draw.rect(self.screen,(255,255,255),input_rect,2)
        self.screen.blit(player_name,(input_rect.x+5,input_rect.y+5))
