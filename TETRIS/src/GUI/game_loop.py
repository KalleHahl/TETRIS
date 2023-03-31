import pygame
from tetris_logic.tetris import Tetris
from GUI.renderer import Renderer
from GUI.event_queue import EventQueue


BLOCK = 40


class Game:

    def __init__(self, screen):

        self.screen = screen
        self.end = False
        self.paused = False
        self.tetris = Tetris()
        self.renderer = Renderer(self.screen, self.tetris)
        self.event = EventQueue()
        self.clock = pygame.time.Clock()

    def update(self):
        if self.tetris.end:
            self.end = True
        if self.tetris.piece.landed is True:
            self.tetris.new_piece()
        self.tetris.full_lines()

    def events(self):
        for event in self.event.get():
            if event.type == pygame.QUIT:
                self.end = True
            if event.type == pygame.KEYDOWN:
                if not self.paused:
                    if event.key == pygame.K_LEFT:
                        self.tetris.move_side(0-BLOCK)
                    if event.key == pygame.K_RIGHT:
                        self.tetris.move_side(BLOCK)
                    if event.key == pygame.K_UP:
                        self.tetris.rotate()
                    if event.key == pygame.K_DOWN:
                        self.tetris.move_down(BLOCK)
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused

            if not self.paused:
                if event.type == self.event.delay:
                    self.tetris.move_down(BLOCK)

    def start(self):
        while not self.end:
            self.clock.tick(60)
            self.events()
            if not self.tetris.piece:
                self.tetris.new_piece()
            self.update()
            self.renderer.render_all(self.paused)
