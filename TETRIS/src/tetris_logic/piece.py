import random

colors = {
    'I': (0,205,205),
    'T': (178,58,238),
    'O': (238,238,0),
    'L': (255,165,0),
    'J': (28,134,238),
    'S': (0,201,87),
    'Z': (255,48,48)
}
class Piece:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.pieces = {
            'T': [[(0,0), (-1,0), (1,0), (0,-1)],
                  [(0,0),(-1,0),(1,0),(0,1)],
                  [(0,0), (-1,0), (0,-1), (0,1)],
                  [(0,0), (0,-1),(0,1),(1,0)]], 
            'I': [[(0,0), (0,1),(0,-1),(0,-2)],
                  [(0,0), (1,0),(-1,0),(-2,0)]],
            'O': [[(0,0), (0,-1), (1,0), (1,-1)]],
            'L': [[(0,0), (1,0),(0,-1),(0,-2)],
                  [(0,0), (0,1), (1,0), (2,0)],
                  [(0,0), (-1,0), (0,1), (0,2)],
                  [(0,0), (0,-1), (-1,0), (-2,0)]],
            'J': [[(0,0), (-1,0), (0,-1), (0,-2)],
                  [(0,0), (0,-1), (1,0), (2,0)],
                  [(0,0), (1,0), (0,1), (0,2)],
                  [(0,0), (0,1), (-1, 0), (-2,0)]],
            'S': [[(0,0), (0,-1), (1, -1), (-1,0)],
                  [(0,0), (0,-1), (1,0), (1,1)],
                  [(0,0), (1,0), (0,1), (-1,1)],
                  [(0,0), (0,1), (-1,0), (-1,-1)]],
            'Z': [[(0,0), (0,-1), (-1,-1), (1,0)],
                  [(0,0), (1,0), (1,-1), (0,1)],
                  [(0,0), (-1,0), (0,1), (1,1)],
                  [(0,0), (-1,0),(-1,1), (0,-1)]]
        }
        self.piece = random.choice(list(self.pieces))
        self.rotation = 0
        self.color = colors[self.piece]
        self.landed = False
    
    def piece_info(self):
        return self.pieces[self.piece][self.rotation]

    def rotate(self):
        if len(self.pieces[self.piece])-1 == self.rotation:
            print('liikaa')
            self.rotation = 0
        else:
            self.rotation += 1
