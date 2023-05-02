import random
from src.settings import pieces, colors, wall_kick_offsets


class Piece:
    """Class for TETRIS piece

    Attributes:
        x_coordinate: x coordinate of the piece
        y_coordinate: y coordinate of the piece
        piece: shape of the piece
        rotation: current rotation of the piece
        color: color of the piece
        landed: set to True when piece has landed
    """

    def __init__(self, x_coordinate, y_coordinate):
        """Constructor, which creates new piece

        Args:
            x_coordinate (integer): starting x coordinate of the piece
            y_coordinate (integer): starting y coordinate of the piece
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.piece = random.choice(list(pieces))
        self.rotation = 0
        self.color = colors[self.piece]
        self.landed = False

    def piece_info(self):
        """Method for fetching coordinate offsets for blocks in piece

        Returns:
            list: list of tuples which store x and y offsets for blocks in piece
        """
        return pieces[self.piece][self.rotation]

    def rotate(self):
        """Method for changing rotation
        """
        if len(pieces[self.piece])-1 == self.rotation:
            self.rotation = 0
        else:
            self.rotation += 1

    def get_wall_kicks(self):
        """Method for fetching wallkick offsets of piece

        Returns:
            list: list of tuples with wallkick offsets
        """
        return wall_kick_offsets[self.piece][self.rotation]


class Ghost(Piece):
    """Class for ghost piece with all methods from Piece-class

    Args:
        Piece (object): inherits attributes of piece-object
    """
    def __init__(self):
        pass
