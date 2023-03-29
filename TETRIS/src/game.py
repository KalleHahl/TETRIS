import pygame
from tetris_logic.tetris import Tetris

WIDTH = 400
HEIGHT = 800
BLOCK = WIDTH//10
BACKROUND = (99,99,99)
LINE = (128,128,128)

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Tetris')
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.end = False
        self.tetris = Tetris()
        self.clock = pygame.time.Clock()
        self.delay = pygame.USEREVENT + 1
        pygame.time.set_timer(self.delay, 500)

        
        
    def draw(self):
        self.screen.fill(BACKROUND)
        self.draw_grid()
        self.draw_previous()
        self.draw_piece()
        pygame.display.flip()

    def update(self):
        if self.tetris.end:
            self.end = True
        if self.tetris.piece.landed == True:
            self.tetris.new_piece()
        self.tetris.full_lines()

    def draw_piece(self):
        
        piece_coordinates = self.tetris.piece.piece_info()
        for coordinate in piece_coordinates:
            pygame.draw.rect(self.screen, self.tetris.piece.color, (self.tetris.piece.x+coordinate[0]*BLOCK, self.tetris.piece.y+coordinate[1]*BLOCK,BLOCK,BLOCK),0,4)
            pygame.draw.rect(self.screen, (0,0,0), (self.tetris.piece.x+coordinate[0]*BLOCK, self.tetris.piece.y+coordinate[1]*BLOCK,BLOCK,BLOCK),3,4)


    def events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.tetris.move_side(0-BLOCK)
                    if event.key == pygame.K_RIGHT:
                        self.tetris.move_side(BLOCK)
                    if event.key == pygame.K_UP:
                        self.tetris.rotate()
                    if event.key == pygame.K_DOWN:
                        self.tetris.move_down(BLOCK)

                if event.type == self.delay:
                        self.tetris.move_down(BLOCK)

    def draw_grid(self):
        for x in range(0,WIDTH,BLOCK):
            pygame.draw.line(self.screen, (LINE), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, BLOCK):
            pygame.draw.line(self.screen, (LINE), (0,y), (WIDTH, y))
    
    def draw_previous(self):
        for y in range(20):
            for x in range(10):
                color = self.tetris.map_pieces[y][x]
                if color == 0:
                    continue
                pygame.draw.rect(self.screen, color, (BLOCK*x,BLOCK*y,BLOCK,BLOCK),0,4)
                pygame.draw.rect(self.screen, (0,0,0), (BLOCK*x,BLOCK*y,BLOCK,BLOCK),3 ,4)

         
    def loop(self):
        while not self.end:
            self.clock.tick(60)
            if self.tetris.piece == None:
                self.tetris.new_piece()
            self.events()
            self.update()
            self.draw()
            
            


tetris = Game()
tetris.loop()