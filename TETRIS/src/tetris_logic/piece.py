import random
from src.settings import pieces, colors, wall_kick_offsets


class Piece:

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.piece = random.choice(list(pieces))
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


class Ghost(Piece):

    def __init__(self):
        pass
