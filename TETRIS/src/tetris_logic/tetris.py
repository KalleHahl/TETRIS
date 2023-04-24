
from collections import deque
from src.tetris_logic.piece import Piece

WIDTH = 400
HEIGHT = 800

BLOCK = 40


class Tetris:

    def __init__(self):
        self.next_piece = Piece(160, 40)
        self.piece = None
        self.board = deque([[0 for k in range(10)] for i in range(20)])
        self.end = False
        self.score = 0

    def new_piece(self):
        old_piece = self.piece
        self.piece = self.next_piece
        if self.out_of_bounds():
            self.end = True
            self.piece = old_piece
        self.next_piece = Piece(160, 40)

    def move_side(self, x_coordinate):
        old_x = self.piece.x_coordinate
        self.piece.x_coordinate += x_coordinate
        if self.out_of_bounds():
            self.piece.x_coordinate = old_x

    def move_down(self):
        old_y = self.piece.y_coordinate
        self.piece.y_coordinate += BLOCK
        if self.out_of_bounds():
            self.piece.y_coordinate = old_y
            self.piece.landed = True
            self.add_piece_to_board()
            return

    def rotate(self):
        old_x = self.piece.x_coordinate
        old_y = self.piece.y_coordinate
        old = self.piece.rotation
        old_offsets = self.piece.get_wall_kicks()
        self.piece.rotate()
        if self.out_of_bounds():
            for index, offsets in enumerate(self.piece.get_wall_kicks()):
                new_x = old_offsets[index][0]-offsets[0]
                self.piece.x_coordinate = old_x + new_x
                new_y = old_offsets[index][1]-offsets[1]

                self.piece.y_coordinate = old_y + new_y

                if not self.out_of_bounds():
                    break
            else:
                self.piece.rotation = old
                self.piece.x_coordinate = old_x
                self.piece.y_coordinate = old_y

    def out_of_bounds(self):
        coordinates = self.piece.piece_info()
        for coordinate in coordinates:
            y_coordinate = BLOCK*coordinate[1]+self.piece.y_coordinate
            x_coordinate = BLOCK*coordinate[0]+self.piece.x_coordinate

            if y_coordinate < 0:
                continue

            if x_coordinate > WIDTH-BLOCK or x_coordinate < 0 or y_coordinate > HEIGHT-BLOCK \
                    or self.board[y_coordinate//BLOCK][x_coordinate//BLOCK] != 0:
                return True

        return False

    def full_lines(self):
        for i in range(20):
            if 0 not in self.board[i]:
                self.score += 1
                del self.board[i]
                self.board.appendleft([0 for i in range(10)])

    def add_piece_to_board(self):
        coordinates = self.piece.piece_info()
        for coordinate in coordinates:
            x_coordinate = coordinate[0]+(self.piece.x_coordinate//BLOCK)
            y_coordinate = coordinate[1]+(self.piece.y_coordinate//BLOCK)
            if y_coordinate < 0:
                continue
            self.board[y_coordinate][x_coordinate] = self.piece.color

    def wipe(self):
        self.__init__()
