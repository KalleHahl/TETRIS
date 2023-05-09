import pygame
from src.gui.buttons.buttons import Buttons
from src.settings import BOARD_WIDTH, BOARD_HEIGHT, LINE, BLOCK, WIDTH, BACKGROUND_IMG, TETRIS_LOGO_SCALED


class Renderer:
    """Renderer class for rendering pygame screen

    Attributes:
        screen: pygame display to draw on
        tetris: tetris class to get piece coordinates
        button: buttons class for button management
        _background: image for background
        _tetris_logo: image for tetris logo
    """

    def __init__(self, screen, tetris):
        """Class constructor

        Args:
            screen (pygame.surface): pygame display where stuff is rendered
            tetris (class): Tetris class
        """
        self.screen = screen
        self.tetris = tetris
        self.button = Buttons(self.screen)
        self._background = BACKGROUND_IMG
        self._tetris_logo = TETRIS_LOGO_SCALED

    def render_backround_game(self):
        """Method for rendering picture and grid in the 
        game background
        """
        self.screen.blit(self._background, (0, 0))
        for x_coordinate in range(0, BOARD_WIDTH, BLOCK):
            pygame.draw.line(self.screen, (LINE),
                             (x_coordinate, 0), (x_coordinate, BOARD_HEIGHT))
        for y_coordinate in range(0, BOARD_HEIGHT, BLOCK):
            pygame.draw.line(self.screen, (LINE),
                             (0, y_coordinate), (BOARD_WIDTH, y_coordinate))
        pygame.draw.line(self.screen, (LINE),
                         (BOARD_WIDTH, 0), (BOARD_WIDTH, BOARD_HEIGHT), 2)

    def render_piece(self):
        """Method for rendering current piece on the screen
        """
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
        """Method for rendering the 'ghost' for the current piece
        """
        piece_coordinates = self.tetris.ghost.piece_info()
        for coordinate in piece_coordinates:

            pygame.draw.rect(self.screen, (220, 220, 220),
                             (self.tetris.ghost.x_coordinate + coordinate[0]*BLOCK,
                             self.tetris.ghost.y_coordinate +
                                 coordinate[1]*BLOCK,
                             BLOCK, BLOCK), 2, 4)

    def render_next_piece(self):
        """Method for rendering the next piece
        """
        next_coordinates = self.tetris.next_piece.piece_info()
        for coordinate in next_coordinates:
            pygame.draw.rect(self.screen, self.tetris.next_piece.color,
                             (525 + coordinate[0]*BLOCK, 200 + coordinate[1]*BLOCK,
                              BLOCK, BLOCK), 0, 4)
            pygame.draw.rect(self.screen, (0, 0, 0),
                             (525 + coordinate[0]*BLOCK, 200 + coordinate[1]*BLOCK,
                             BLOCK, BLOCK), 3, 4)

    def render_previous_pieces(self):
        """Method for rendering all previous pieces on the board
        """
        for y_coordinate in range(20):
            for x_coordinate in range(10):
                color = self.tetris.board[y_coordinate][x_coordinate]
                if color == 0:
                    continue
                pygame.draw.rect(self.screen, color,
                                 (BLOCK*x_coordinate, BLOCK*y_coordinate, BLOCK, BLOCK), 0, 4)
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 (BLOCK*x_coordinate, BLOCK*y_coordinate, BLOCK, BLOCK), 3, 4)

    def render_all(self, pause, end, player):
        """Method for rendering all of the necessary things during game

        Args:
            pause (boolean): Tells if the game should render pause state
            end (boolean): Tells if game should render game over screen
            player (string): Player name
        """
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
            self.render_game_over(player)

    def render_menu(self, top_3):
        """Method for rendering menu state
        """
        self.screen.blit(self._background, (0, 0))
        image_width = self._tetris_logo.get_width()
        self.screen.blit(self._tetris_logo,((WIDTH//2)-(image_width//2), 60))
        self.button.start()
        self.button.highscores()
        self.button.top_3(top_3)

    def render_score_saved(self):
        """Method for rendering score saved on display
        """
        self.screen.blit(self._background, (0, 0))
        self.button.score_saved()

    def render_game_over(self, player):
        """Method for rendering game over screen

        Args:
            player (string): Player name
        """
        self.blur()
        self.button.user_input(player)
        self.button.game_over()
        self.button.enter_name()

    def blur(self):
        """Method for blurring the screen
        """
        blur = pygame.Surface((WIDTH, BOARD_HEIGHT))
        blur.set_alpha(200)
        blur.fill((0, 0, 0))
        self.screen.blit(blur, (0, 0))
