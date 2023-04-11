import pygame

BLOCK = 40


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

    def update(self):
        if self.tetris.end:
            self.end = True
            return
        if self.tetris.piece.landed is True:
            self.tetris.new_piece()
        self.tetris.full_lines()

    def game_events(self):
        for event in self.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            if event.type == pygame.KEYDOWN:
                if not self.paused:
                    if event.key == pygame.K_LEFT:
                        self.tetris.move_side(0-BLOCK)
                    if event.key == pygame.K_RIGHT:
                        self.tetris.move_side(BLOCK)
                    if event.key == pygame.K_UP:
                        self.tetris.rotate()
                    if event.key == pygame.K_DOWN:
                        self.tetris.move_down()
                if event.key == pygame.K_SPACE:
                    if self.end:
                        self.tetris.wipe()
                        self.end = False
                    else:
                        self.paused = not self.paused

            if not self.paused and not self.end:
                if event.type == self.event.delay:
                    self.tetris.move_down()
    
    def menu_events(self):
        for event in self.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
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
    
