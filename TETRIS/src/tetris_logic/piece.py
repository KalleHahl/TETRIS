import random

colors = {
    'I': (0, 205, 205),
    'T': (178, 58, 238),
    'O': (238, 238, 0),
    'L': (255, 165, 0),
    'J': (28, 134, 238),
    'S': (0, 201, 87),
    'Z': (255, 48, 48)
}

wall_kick_offsets = {
    **dict.fromkeys(['T', 'L', 'J', 'S', 'Z'],
                    [[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                     [(0, 0), (40, 0), (40, -40), (0, 40), (40, 80)],
                     [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
                     [(0, 0), (-40, 0), (-40, -40), (0, 40), (-40, 80)]]),
    'I': [[(0, 0), (-40, 0), (80, 0), (0, 0), (80, 0)],
          [(-40, 0), (0, 0), (0, 0), (0, 80), (0, -80)],
          [(-40, 40), (40, 0), (-80, 0), (40, 0), (0, 0)],
          [(0, 40), (0, 0), (0, 0), (0, -40), (0, 40)]],
    'O': [[(0,0)]]
}

pieces = {
    'T': [[(0, 0), (-1, 0), (1, 0), (0, -1)],
          [(0, 0), (0, -1), (0, 1), (1, 0)],
          [(0, 0), (-1, 0), (1, 0), (0, 1)],
          [(0, 0), (-1, 0), (0, -1), (0, 1)]],
    'I': [[(0, 0), (1, 0), (-1, 0), (2, 0)],
          [(0, 0), (0, 1), (0, -1), (0, 2)],
          [(0, 0), (-2, 0), (-1, 0), (1, 0)],
          [(0, 0), (0, 1), (0, -2), (0, -1)]],
    'O': [[(0, 0), (0, -1), (1, 0), (1, -1)]],
    'L': [[(1, -1), (1, 0), (0, 0), (-1, 0)],
          [(1, 1), (0, 1), (0, 0), (0, -1)],
          [(-1, 1), (-1, 0), (0, 0), (1, 0)],
          [(-1, -1), (0, -1), (0, 0), (0, 1)]],
    'J': [[(-1, -1), (-1, 0), (0, 0), (1, 0)],
          [(0, -1), (0, 0), (0, 1), (1, -1)],
          [(-1, 0), (0, 0), (1, 0), (1, 1)],
          [(-1, 1), (0, 1), (0, 0), (0, -1)]],
    'S': [[(0, 0), (0, -1), (1, -1), (-1, 0)],
          [(0, 0), (0, -1), (1, 0), (1, 1)],
          [(0, 0), (1, 0), (0, 1), (-1, 1)],
          [(0, 0), (0, 1), (-1, 0), (-1, -1)]],
    'Z': [[(0, 0), (0, -1), (-1, -1), (1, 0)],
          [(0, 0), (1, 0), (1, -1), (0, 1)],
          [(0, 0), (-1, 0), (0, 1), (1, 1)],
          [(0, 0), (-1, 0), (-1, 1), (0, -1)]]
}


class Piece:

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.piece = 'I'#random.choice(list(pieces))
        self.rotation = 0
        self.color = colors[self.piece]
        self.landed = False

    def piece_info(self):
        return pieces[self.piece][self.rotation]

    def rotate(self):
        if len(pieces[self.piece])-1 == self.rotation:
            self.rotation = 0
        else:
            self.rotation += 1

    def get_wall_kicks(self):
        return wall_kick_offsets[self.piece][self.rotation]
