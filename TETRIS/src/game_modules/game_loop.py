import pygame
from src.settings import BLOCK


class Game:

    def __init__(self, screen, tetris, renderer, event_queue, clock):
        self.state = 'menu'
        self.screen = screen
        self.quit = False
        self.end = False
        self.paused = False
        self.tetris = tetris
        self.renderer = renderer
        self.event = event_queue
        self.clock = clock
        self.move_down_fast = False
        self.player = ''

    def _update(self):
        if self.tetris.end:
            self.end = True
            return
        self.tetris.full_lines()
        if self.tetris.piece.landed is True:
            self.tetris.new_piece()
        if self.tetris.update_speed:
            self.event.set_speed(self.tetris.speed)
            self.tetris.update_speed = False

    def _game_events(self):
        for event in self.event.get():
            if event.type == pygame.constants.QUIT:
                self.quit = True

            if event.type == pygame.constants.KEYDOWN:
                if self.end:
                    self._handle_keydown_event_end(event)
                else:
                    self._handle_keydown_event(event)

            if event.type == pygame.constants.KEYUP:
                self._handle_keyup_event(event)

            if not self.paused and not self.end and self.tetris.piece:
                if event.type == self.event.delay:
                    self._handle_delay_event()

                if event.type == self.event.move_down_fast:
                    self._handle_move_down_fast()

    def _handle_keydown_event_end(self, event):

        if event.key == pygame.K_BACKSPACE:
            self.player = self.player[:-1]
        elif event.key == pygame.K_RETURN:
            print(self.player)
            self.player = ''
            self.state = 'menu'
            self.tetris.wipe()
            self.end = False
            self._score_saved()
        else:
            self.player += event.unicode

    def _handle_keydown_event(self, event):
        if not self.paused:
            if event.key == pygame.constants.K_LEFT:
                self.tetris.move_side(0-BLOCK)
            if event.key == pygame.constants.K_RIGHT:
                self.tetris.move_side(BLOCK)
            if event.key == pygame.constants.K_UP:
                self.tetris.rotate()
            if event.key == pygame.constants.K_DOWN:
                self.move_down_fast = True
            if event.key == pygame.constants.K_SPACE:
                self.tetris.jump_down()
        if event.key == pygame.constants.K_ESCAPE:
            self.paused = not self.paused

    def _handle_keyup_event(self, event):
        if event.key == pygame.constants.K_DOWN:
            self.move_down_fast = False

    def _handle_delay_event(self):
        if not self.move_down_fast:
            self.tetris.move_down()

    def _handle_move_down_fast(self):
        if self.move_down_fast:
            self.tetris.move_down()

    def _menu_events(self):
        for event in self.event.get():
            if event.type == pygame.constants.QUIT:
                self.quit = True
            elif event.type == pygame.constants.KEYDOWN:
                if event.key == pygame.constants.K_SPACE:
                    self.state = 'game'

    def _score_saved(self):
        self.renderer.render_score_saved()
        pygame.display.update()
        pygame.time.wait(3000)
        self.renderer.render_menu()
        pygame.display.update()


    def start(self):
        while not self.quit:
            self.clock.tick(60)
            if self.state == 'game':
                self._game_events()
                if not self.tetris.piece:
                    self.tetris.new_piece()
                if not self.end:
                    self._update()
                self.renderer.render_all(self.paused, self.end, self.player)
            elif self.state == 'menu':
                self._menu_events()
                self.renderer.render_menu()

            pygame.display.update()
