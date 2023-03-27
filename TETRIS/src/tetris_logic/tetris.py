from tetris_logic.piece import Piece

class Tetris:

    def __init__(self):
        self.piece = None
    
    def new_piece(self):
        self.piece = Piece(160,40)

    def move_side(self, x):
        self.piece.x += x
    
    def rotate(self):
        self.piece.rotate()
        
