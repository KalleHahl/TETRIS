import pygame
from src.settings import BLOCK


class Game:
    """Class for game loop

    Attributes:
        state: game _state
        screen: pygame display for rendering
        quit: quits program
        end: indicates if the game has ended
        paused: indicates if the game is paused
        tetris: tetris class for game logic
        renderer: renderer class for rendering
        events: events class for handling pygame events
        clock: clock class for pygame clock
        move_down_fast: indicates if arrowkey down is held down
        player: player name
    """

    def __init__(self, screen, tetris, renderer, event_queue, clock, score_repo):
        """Class constructor

        Args:
            screen (pygame.display): display
            tetris (class): tetris class 
            renderer (class): renderer class
            event_queue (class): event queue class
            clock (class): clock class
        """
        self._state = 'menu'
        self._screen = screen
        self._quit = False
        self._end = False
        self._paused = False
        self._tetris = tetris
        self._renderer = renderer
        self._events = event_queue
        self._clock = clock
        self._move_down_fast = False
        self._player = ''
        self._score_repo = score_repo
        self._top_3 = self._top_scores()

    def _update(self):
        """Method for keeping game updated when playing.
        Checks full lines, if piece has landed etc
        """
        if self._tetris.end:
            self._end = True
            return
        self._tetris.full_lines()
        if self._tetris.piece.landed is True:
            self._tetris.new_piece()
        if self._tetris.update_speed:
            self._events.set_speed(self._tetris.level)
            self._tetris.update_speed = False

    def _game_events(self):
        """Method for handling events when game is being played
        """
        for event in self._events.get():
            if event.type == pygame.constants.QUIT:
                self._quit = True

            if event.type == pygame.constants.KEYDOWN:
                if self._end:
                    self._handle_keydown_event__end(event)
                else:
                    self._handle_keydown_event(event)

            if event.type == pygame.constants.KEYUP:
                self._handle_keyup_event(event)

            if not self._paused and not self._end and self._tetris.piece:
                if event.type == self._events.delay:
                    self._handle_delay_event()

                if event.type == self._events.move_down_fast:
                    self._handle_move_down_fast()

    def _handle_keydown_event__end(self, event):
        """Method for handling keydown events when game is over
        Wipes game, creates new score and updates top 3

        Args:
            event (pygame.event): event type
        """

        if event.key == pygame.K_BACKSPACE:
            self._player = self._player[:-1]
        elif event.key == pygame.K_RETURN:
            if self._player == '':
                self._player = "unknown"
            self._score_repo.create_score(self._player, self._tetris.score)
            self._top_3 = self._top_scores()
            self._player = ''
            self._state = 'menu'
            self._tetris.wipe()
            self._end = False
            self._score_saved()
        else:
            self._player += event.unicode

    def _handle_keydown_event(self, event):
        """Method for handling keydown events during game

        Args:
            event (pygame.event): event type
        """
        if not self._paused:
            if event.key == pygame.constants.K_LEFT:
                self._tetris.move_side(0-BLOCK)
            if event.key == pygame.constants.K_RIGHT:
                self._tetris.move_side(BLOCK)
            if event.key == pygame.constants.K_UP:
                self._tetris.rotate()
            if event.key == pygame.constants.K_DOWN:
                self._move_down_fast = True
            if event.key == pygame.constants.K_SPACE:
                self._tetris.jump_down()
        if event.key == pygame.constants.K_ESCAPE:
            self._paused = not self._paused

    def _handle_keyup_event(self, event):
        """Method for handling keyup events

        Args:
            event (pygame.event): event type
        """
        if event.key == pygame.constants.K_DOWN:
            self._move_down_fast = False

    def _handle_delay_event(self):
        """Method for handling delay event for moving piece
        down periodically
        """
        if not self._move_down_fast:
            self._tetris.move_down()

    def _handle_move_down_fast(self):
        """Method for moving piece down faster when arrowkey down
        is pressed
        """
        if self._move_down_fast:
            self._tetris.move_down()

    def _menu_events(self):
        """Method for handling events when game is in menu state
        """
        for event in self._events.get():
            if event.type == pygame.constants.QUIT:
                self._quit = True
            elif event.type == pygame.constants.KEYDOWN:
                if event.key == pygame.constants.K_SPACE:
                    self._state = 'game'

    def _score_saved(self):
        """Method for rendering score saved screen for 3 seconds
        """
        self._renderer.render_score_saved()
        pygame.display.update()
        pygame.time.wait(3000)
        self._renderer.render_menu(self._top_3)
        pygame.display.update()

    def _top_scores(self):
        """Method for updating top 3 scores

        Returns:
            funciton call: function which fetches top 3 scores from db
        """
        return self._score_repo.find_top_scores()

    def start(self):
        """Main method to start the game loop and updating screen.
        Calls methods according to game state
        """
        while not self._quit:
            self._clock.tick(60)
            if self._state == 'game':
                self._game_events()
                if not self._tetris.piece:
                    self._tetris.new_piece()
                if not self._end:
                    self._update()
                self._renderer.render_all(
                    self._paused, self._end, self._player)
            elif self._state == 'menu':
                self._menu_events()
                self._renderer.render_menu(self._top_3)

            pygame.display.update()
