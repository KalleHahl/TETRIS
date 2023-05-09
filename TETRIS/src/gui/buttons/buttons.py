import pygame
from src.settings import (HEIGHT, WIDTH, GAMEOVER_IMG, SCORE_IMG, START_IMG, NEXT_PIECE_IMG,
                          HIGHSCORES_IMG, SCORE_SAVED_IMG, RESUME_IMG, LEVEL_IMG, LINES_IMG)


class Buttons:
    """Class for rendering buttons

    Attributes:
        screen: pygame display
        _game_over_img: image for game over text
        _score_img: image for score text
        _start_img: image for start text
        _next_piece_img: image for next piece text
        _highscores_img: image for highscores
        _score_saved_img: image for score saved text
        _resume_img: image for resume text
    """

    def __init__(self, screen):
        """Class constructor

        Args:
            screen (pygame.display): Display to render on
        """
        self.screen = screen
        self._game_over_img = GAMEOVER_IMG
        self._score_img = SCORE_IMG
        self._start_img = START_IMG
        self._next_piece_img = NEXT_PIECE_IMG
        self._highscores_img = HIGHSCORES_IMG
        self._score_saved_img = SCORE_SAVED_IMG
        self._resume_img = RESUME_IMG
        self._level_img = LEVEL_IMG
        self._lines_img = LINES_IMG

    def resume(self):
        """Resume game button
        """
        image_width = self._resume_img.get_width()
        self.screen.blit(self._resume_img,
                         ((WIDTH//2)-(image_width//2), HEIGHT//2))

    def game_over(self):
        """Game over button
        """
        image_width = self._game_over_img.get_width()
        self.screen.blit(self._game_over_img,
                         ((WIDTH//2)-(image_width//2), 180))

    def start(self):
        """Start game button
        """
        image_width = self._start_img.get_width()
        self.screen.blit(self._start_img, ((WIDTH//2) -
                         (image_width//2), HEIGHT//3))

    def next_piece(self):
        """Next piece button
        """
        image_width = self._next_piece_img.get_width()
        self.screen.blit(self._next_piece_img,
                         ((WIDTH-150)-(image_width//2), 100))

    def score(self, score):
        """Button for current score

        Args:
            score (int): current score

        Returns:
            function: returns the template method with correct score
        """
        image_width = self._score_img.get_width()
        self.screen.blit(self._score_img, ((WIDTH-150)-(image_width//2), 400))
        return self._template(f'{score}', WIDTH-150, 480, 40)

    def level(self, level):
        """Button for current level

        Args:
            level (int): current level

        Returns:
            function: template with correct level
        """
        image_width = self._level_img.get_width()
        self.screen.blit(self._level_img, ((WIDTH-150)-(image_width//2), 530))
        return self._template(f'{level}', WIDTH-150, 610, 40)

    def lines(self, lines):
        """Button for lines cleared

        Args:
            lines (int): lines cleared

        Returns:
            function: template with correct lines cleared
        """
        image_width = self._lines_img.get_width()
        self.screen.blit(self._lines_img, ((WIDTH-150)-(image_width//2), 660))
        return self._template(f'{lines}', WIDTH-150, 740, 40)

    def score_saved(self):
        """Score saved button
        """
        image_width = self._score_saved_img.get_width()
        self.screen.blit(self._score_saved_img,
                         ((WIDTH//2)-(image_width//2), HEIGHT//2))

    def enter_name(self):
        """Enter name button

        Returns:
            function: returns the template method with correct text
        """
        return self._template('Enter name:', WIDTH//2, HEIGHT//2-20, 20)

    def highscores(self):
        """Highscore button
        """
        image_width = self._highscores_img.get_width()
        self.screen.blit(self._highscores_img,
                         ((WIDTH//2)-(image_width//2), HEIGHT//2))

    def top_3(self, top_3):
        """Method for rendering top 3 scores

        Args:
            top_3 (list): list of tuples with player name and score
        """
        y_coordinate = HEIGHT//2+80
        for tup in top_3:
            self._template(f'{tup[0]}: {tup[1]}', WIDTH//2, y_coordinate, 40)
            y_coordinate += 50

    def _template(self, text, x_coordinate, y_coordinate, size):
        """Template for buttons

        Args:
            text (string): text to be written on the button
            x_coordinate (int): x coordinate for button
            y_coordinate (int): y coordinate for button
            size (int): font size
        """
        font = pygame.font.Font('freesansbold.ttf', size)
        text_1 = font.render(text, True, (117, 204, 32), (0, 0, 0))
        rectangle = text_1.get_rect()
        rectangle.center = (x_coordinate, y_coordinate)
        self.screen.blit(text_1, rectangle)

    def user_input(self, player):
        """Box for user input which changes size with the text

        Args:
            player (string): player name
        """
        text = pygame.font.Font('freesansbold.ttf', 20)
        player_name = text.render(player, True, (117, 204, 32))
        rect_width = max(200, player_name.get_width() + 15)
        input_rect = pygame.Rect(WIDTH//2-rect_width //
                                 2, HEIGHT//2, rect_width, 32)
        pygame.draw.rect(self.screen, (117, 204, 32), input_rect, 2)
        self.screen.blit(player_name, (input_rect.x+5, input_rect.y+5))
