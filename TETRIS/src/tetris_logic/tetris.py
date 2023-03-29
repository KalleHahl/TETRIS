from tetris_logic.piece import Piece

WIDTH = 400
HEIGHT = 800

BLOCK = 40

class Tetris:

    def __init__(self):
        self.piece = None
        self.map_pieces = [[0 for x in range(10)] for i in range(20)]
    
    def new_piece(self):
        self.piece = Piece(160,40)

    def move_side(self, x):
        old_x = self.piece.x
        self.piece.x += x
        if self.out_of_bounds():
            self.piece.x = old_x
    
    def move_down(self, y):
        old_y = self.piece.y
        self.piece.y += y
        if self.out_of_bounds():
            self.piece.y = old_y
            self.piece.landed = True
            self.map_piece()
            return
             

    def rotate(self):
        old = self.piece.rotation
        self.piece.rotate()
        if self.out_of_bounds():
            self.piece.rotation = old
    
    def out_of_bounds(self):
        coordinates = self.piece.piece_info()
        for coordinate in coordinates:
            y = BLOCK*coordinate[1]+self.piece.y
            x = BLOCK*coordinate[0]+self.piece.x

            if x > WIDTH-BLOCK or x < 0 or y > HEIGHT-BLOCK \
                or self.map_pieces[y//BLOCK][x//BLOCK] != 0:
                return True
            
        return False
    
    def map_piece(self):
        coordinates = self.piece.piece_info()
        for coordinate in coordinates:
            x = coordinate[0]+(self.piece.x//40)
            y = coordinate[1]+(self.piece.y//40)
            self.map_pieces[y][x] = self.piece.color
        print(self.map_pieces)
