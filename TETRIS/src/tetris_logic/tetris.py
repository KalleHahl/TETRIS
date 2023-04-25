
from collections import deque
from src.tetris_logic.piece import Piece, Ghost
from src.settings import *



class Tetris:

    def __init__(self):
        self.next_piece = Piece(160, 40)
        self.piece = None
        self.ghost = None
        self.board = deque([[0 for k in range(10)] for i in range(20)])
        self.end = False
        self.score = 0
        self.speed = 750
        self.update_speed = False


    def new_piece(self):
        old_piece = self.piece
        self.piece = self.next_piece
        self.ghost = Ghost(self.piece.x_coordinate, self.piece.y_coordinate)
        coordinates = self.piece.piece_info()
        if self.out_of_bounds(coordinates, self.piece.x_coordinate, self.piece.y_coordinate):
            self.end = True
            self.piece = old_piece
        self.next_piece = Piece(160, 40)
        self.ghost_coordinates()

    def move_side(self, x_coordinate):
        old_x = self.piece.x_coordinate
        self.piece.x_coordinate += x_coordinate
        coordinates = self.piece.piece_info()
        if self.out_of_bounds(coordinates, self.piece.x_coordinate, self.piece.y_coordinate):
            self.piece.x_coordinate = old_x
        self.ghost_coordinates()

    def move_down(self):
        old_y = self.piece.y_coordinate
        self.piece.y_coordinate += BLOCK
        coordinates = self.piece.piece_info()
        if self.out_of_bounds(coordinates, self.piece.x_coordinate, self.piece.y_coordinate):
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
        coordinates = self.piece.piece_info()
        if self.out_of_bounds(coordinates, self.piece.x_coordinate, self.piece.y_coordinate):
            for index, offsets in enumerate(self.piece.get_wall_kicks()):
                new_x = old_offsets[index][0]-offsets[0]
                self.piece.x_coordinate = old_x + new_x
                new_y = old_offsets[index][1]-offsets[1]

                self.piece.y_coordinate = old_y + new_y
                coordinates = self.piece.piece_info()
                if not self.out_of_bounds(coordinates, self.piece.x_coordinate, self.piece.y_coordinate):
                    break
            else:
                self.piece.rotation = old
                self.piece.x_coordinate = old_x
                self.piece.y_coordinate = old_y
        self.ghost_coordinates()

    def out_of_bounds(self, coordinates, x_coordinate, y_coordinate):

        for coordinate in coordinates:
            y_coordinate2 = BLOCK*coordinate[1]+y_coordinate
            x_coordinate2 = BLOCK*coordinate[0]+x_coordinate
            if y_coordinate2 < 0:
                continue

            if x_coordinate2 > BOARD_WIDTH-BLOCK or x_coordinate2 < 0 or y_coordinate2 > HEIGHT-BLOCK \
                    or self.board[y_coordinate2//BLOCK][x_coordinate2//BLOCK] != 0:
                return True

        return False

    def full_lines(self):
        for i in range(20):
            if 0 not in self.board[i]:
                self.score += 1
                del self.board[i]
                self.board.appendleft([0 for i in range(10)])
                if self.score % 10 == 0:
                    self.speed = self.speed // 2
                    self.update_speed = True

    def add_piece_to_board(self):
        coordinates = self.piece.piece_info()
        for coordinate in coordinates:
            x_coordinate = coordinate[0]+(self.piece.x_coordinate//BLOCK)
            y_coordinate = coordinate[1]+(self.piece.y_coordinate//BLOCK)
            if y_coordinate < 0:
                continue
            self.board[y_coordinate][x_coordinate] = self.piece.color

    def ghost_coordinates(self):

        self.ghost.piece = self.piece.piece
        self.ghost.rotation = self.piece.rotation
        self.ghost.x_coordinate = self.piece.x_coordinate
        self.ghost.y_coordinate = self.piece.y_coordinate
        coordinates = self.ghost.piece_info()

        while True:
            self.ghost.y_coordinate += BLOCK
            if self.out_of_bounds(coordinates, self.ghost.x_coordinate, self.ghost.y_coordinate):
                self.ghost.y_coordinate -= BLOCK
                break
    
    def wipe(self):
        self.__init__()
        self.update_speed = True
