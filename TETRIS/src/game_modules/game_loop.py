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

    def update(self):
        if self.tetris.end:
            self.end = True
            return
        self.tetris.full_lines()
        if self.tetris.piece.landed is True:
            self.tetris.new_piece()
        if self.tetris.update_speed:
            self.event.set_speed(self.tetris.speed)
            self.tetris.update_speed = False

    def game_events(self):
        for event in self.event.get():
            if event.type == pygame.constants.QUIT:
                self.quit = True

            if event.type == pygame.constants.KEYDOWN:
                self.handle_keydown_event(event)

            if event.type == pygame.constants.KEYUP:
                self.handle_keyup_event(event)

            if not self.paused and not self.end and self.tetris.piece:
                if event.type == self.event.delay:
                    self.handle_delay_event()

                if event.type == self.event.move_down_fast:
                    self.handle_move_down_fast()

    def handle_keydown_event(self, event):
        if not self.paused and not self.end:
            if event.key == pygame.constants.K_LEFT:
                self.tetris.move_side(0-BLOCK)
            if event.key == pygame.constants.K_RIGHT:
                self.tetris.move_side(BLOCK)
            if event.key == pygame.constants.K_UP:
                self.tetris.rotate()
            if event.key == pygame.constants.K_DOWN:
                self.move_down_fast = True
        else:
            if event.key == pygame.K_BACKSPACE:
                self.renderer.player = self.renderer.player[:-1]
            else:
                self.renderer.player += event.unicode
            self.renderer.render_game_over()

        if event.key == pygame.constants.K_SPACE:
            if self.end:
                self.tetris.wipe()
                self.end = False
            else:
                self.paused = not self.paused

    def handle_keyup_event(self, event):
        if event.key == pygame.constants.K_DOWN:
            self.move_down_fast = False

    def handle_delay_event(self):
        if not self.move_down_fast:
            self.tetris.move_down()

    def handle_move_down_fast(self):
        if self.move_down_fast:
            self.tetris.move_down()

    def menu_events(self):
        for event in self.event.get():
            if event.type == pygame.constants.QUIT:
                self.quit = True
            elif event.type == pygame.constants.KEYDOWN:
                if event.key == pygame.constants.K_SPACE:
                    self.state = 'game'

    def start(self):
        while not self.quit:
            self.clock.tick(60)
            if self.state == 'game':
                self.game_events()
                if not self.tetris.piece:
                    self.tetris.new_piece()
                if not self.end:
                    self.update()
                self.renderer.render_all(self.paused, self.end)
            elif self.state == 'menu':
                self.menu_events()
                self.renderer.render_menu()


