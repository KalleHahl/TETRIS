
from collections import deque
from src.tetris_logic.piece import Piece, Ghost
from src.settings import BLOCK, BOARD_WIDTH, HEIGHT

class Tetris:

    """Class, which takes care of the tetris logic.

    Attributes:
        next_piece: Piece class, which will be displayed next
        piece: Piece class, current piece on the board
        ghost: Ghost class, shows where the piece will drop
        board: Holds information on pieces on the board
        end: Boolean value, set to True when the game has ended
        score: Integer, keeps track of current score
        speed: Speed at which the pieces move
        update_speed: Boolean value, set to True every 10 points
    """

    def __init__(self):
        """Class constructor, takes no arguments
        """
        self.next_piece = Piece(160, 40)
        self.piece = None
        self.ghost = None
        self.board = deque([[0 for k in range(10)] for i in range(20)])
        self.end = False
        self.score = 0
        self.speed = 750
        self.update_speed = False

    def new_piece(self):
        """Creates a new piece and ghost. Checks if piece is out of bounds.
        Ends game if out_of_bounds return True
        """
        old_piece = self.piece
        self.piece = self.next_piece
        self.ghost = Ghost()
        coordinates = self.piece.piece_info()
        if self.out_of_bounds(coordinates, self.piece.x_coordinate, self.piece.y_coordinate):
            self.end = True
            self.piece = old_piece
        self.next_piece = Piece(160, 40)
        self.ghost_coordinates()

    def move_side(self, x_coordinate):
        """Moves piece by changint the x coordinate. If argument value is negative
        piece is moved left and right when positive. If the desired move is out of bounds
        movement is not allowed. Updates coordinates of the ghost piece.

        Args:
            x_coordinate (integer): Amount to be added to the piece objects x_coordinate
        """
        old_x = self.piece.x_coordinate
        self.piece.x_coordinate += x_coordinate
        coordinates = self.piece.piece_info()
        if self.out_of_bounds(coordinates, self.piece.x_coordinate, self.piece.y_coordinate):
            self.piece.x_coordinate = old_x
        self.ghost_coordinates()

    def move_down(self):
        """Method for moving piece down on the board. If out_of_bounds method returns
        True, then piece is added to the board.
        """
        old_y = self.piece.y_coordinate
        self.piece.y_coordinate += BLOCK
        coordinates = self.piece.piece_info()
        if self.out_of_bounds(coordinates, self.piece.x_coordinate, self.piece.y_coordinate):
            self.piece.y_coordinate = old_y
            self.piece.landed = True
            self.add_piece_to_board()
            return

    def jump_down(self):
        """Method for moving piece to the bottom by changing
        its y coordinate to that of the ghost piece
        """
        self.piece.y_coordinate = self.ghost.y_coordinate
        self.add_piece_to_board()
        self.piece.landed = True

    def rotate(self):
        """Method for rotating current piece. If rotation is out of bounds,
        wallkicks method is called. Updates ghosts coordinate in the end.
        """
        old_x = self.piece.x_coordinate
        old_y = self.piece.y_coordinate
        old_rotation = self.piece.rotation
        old_offsets = self.piece.get_wall_kicks()
        self.piece.rotate()
        coordinates = self.piece.piece_info()
        if self.out_of_bounds(coordinates, self.piece.x_coordinate, self.piece.y_coordinate):
            self.wallkicks(old_x, old_y, old_offsets, old_rotation)
        self.ghost_coordinates()

    def wallkicks(self, old_x, old_y, old_offsets, old_rotation):
        """Iterates through wallkick offsets, if wallkick is found loop is breaked
        if not, then the piece is set back to its old rotation and coordinates

        Args:
            old_x (integer): x coordinate of the piece before rotate was called
            old_y (integer): y_coordinate of the piece before rotate was called
            old_offsets (list): list of offset coordinates for current piece
            old_rotation (integer): number of current rotation

        """
        for index, offsets in enumerate(self.piece.get_wall_kicks()):
            new_x = old_offsets[index][0]-offsets[0]
            self.piece.x_coordinate = old_x + new_x
            new_y = old_offsets[index][1]-offsets[1]

            self.piece.y_coordinate = old_y + new_y
            coordinates = self.piece.piece_info()
            if not self.out_of_bounds(coordinates,
                                      self.piece.x_coordinate, self.piece.y_coordinate):
                break
        else:
            self.piece.rotation = old_rotation
            self.piece.x_coordinate = old_x
            self.piece.y_coordinate = old_y

    def out_of_bounds(self, coordinates, x_coordinate, y_coordinate):
        """Method for checking if piece is out of bounds or touching a piece
        on the board.

        Args:
            coordinates (list): list of tuples for x and y offsets for every block in current piece
            x_coordinate (integer): x coordinate of current piece
            y_coordinate (integer): y coordinate of current piece

        Returns:
            Boolean: True if out of bounds, False if not
        """

        for coordinate in coordinates:
            y_coordinate2 = BLOCK*coordinate[1]+y_coordinate
            x_coordinate2 = BLOCK*coordinate[0]+x_coordinate
            if y_coordinate2 < 0:
                continue

            if (x_coordinate2 > BOARD_WIDTH-BLOCK or x_coordinate2 < 0 or
                y_coordinate2 > HEIGHT-BLOCK or
                self.board[y_coordinate2//BLOCK][x_coordinate2//BLOCK] != 0):
                return True

        return False

    def full_lines(self):
        """Method which iterates self.board and checks if there are any full lines.
        If line is full, it's deleted from the deque and a new empty line is appended
        to the start of the deque. After this, score is increased and every 10 points
        speed is also increased.

        """
        for i in range(20):
            if 0 not in self.board[i]:
                self.score += 1
                del self.board[i]
                self.board.appendleft([0 for i in range(10)])
                if self.score % 10 == 0:
                    self.speed = self.speed // 2
                    self.update_speed = True

    def add_piece_to_board(self):
        """Method for adding piece to the board after landing.
        """
        coordinates = self.piece.piece_info()
        for coordinate in coordinates:
            x_coordinate = coordinate[0]+(self.piece.x_coordinate//BLOCK)
            y_coordinate = coordinate[1]+(self.piece.y_coordinate//BLOCK)
            if y_coordinate < 0:
                continue
            self.board[y_coordinate][x_coordinate] = self.piece.color

    def ghost_coordinates(self):
        """Updates the coordinates of the ghost piece
        """
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
        """Method for re-initializing the class
        """
        self.__init__()
        self.update_speed = True
