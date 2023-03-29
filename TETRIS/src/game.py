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
        self.clock = pygame.time.Clock()
        self.end = False
        self.tetris = Tetris()
        self.left = False
        self.right = False
        
    def draw(self):
        self.screen.fill(BACKROUND)
        self.draw_grid()
        self.draw_previous()
        self.draw_piece()
        pygame.display.flip()

    def update(self):
        self.tetris.move_down(BLOCK)
        if self.tetris.piece.landed == True:
            self.tetris.new_piece()
        pygame.time.wait(200)

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
                pygame.draw.rect(self.screen, (0,0,0), (BLOCK*x,BLOCK*y,BLOCK,BLOCK),3,4)

         
    def loop(self):
        while not self.end:
            if self.tetris.piece == None:
                self.tetris.new_piece()
            self.events()
            self.update()
            self.draw()
            
            


tetris = Game()
tetris.loop()