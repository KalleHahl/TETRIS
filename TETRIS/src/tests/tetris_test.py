import unittest
from collections import deque
from src.tetris_logic.tetris import Tetris
from src.tetris_logic.piece import Piece

WIDTH = 400
HEIGHT = 800
BLOCK = 40


class TetrisTest(unittest.TestCase):

    def setUp(self):
        self.game = Tetris()
        self.game.new_piece()

    def test_new_piece_coordinates(self):
        tup = (self.game.piece.x_coordinate, self.game.piece.y_coordinate)
        self.assertEqual(tup, (160, 0))

    def test_move_left(self):
        self.game.move_side(-BLOCK)
        tup = (self.game.piece.x_coordinate, self.game.piece.y_coordinate)
        self.assertEqual(tup, (120, 0))

    def test_move_right(self):
        self.game.move_side(BLOCK)
        tup = (self.game.piece.x_coordinate, self.game.piece.y_coordinate)
        self.assertEqual(tup, (200, 0))

    def test_move_side_not_allowed(self):
        self.game.piece.x_coordinate = 0
        self.game.move_side(-BLOCK)
        self.assertEqual(self.game.piece.x_coordinate, 0)

    def test_move_down(self):
        self.game.move_down()
        tup = (self.game.piece.x_coordinate, self.game.piece.y_coordinate)
        self.assertEqual(tup, (160, 40))

    def test_landed(self):
        # test with T
        self.game.piece.piece = 'T'
        self.game.piece.y_coordinate = HEIGHT-BLOCK
        self.game.move_down()
        self.assertEqual(self.game.piece.landed, True)
        self.assertEqual(self.game.piece.y_coordinate, HEIGHT-BLOCK)

    def test_rotate(self):
        # test with t
        self.game.piece.piece = 'T'
        self.game.rotate()
        new_rotation = self.game.piece.rotation
        new_coordinates = self.game.piece.piece_info()

        self.assertEqual(new_rotation, 1)
        self.assertEqual(new_coordinates, self.game.piece.pieces['T'][1])
    """
    def test_cannot_rotate(self):
        # test with I 
        self.game.piece.piece = 'I'
        self.game.piece.x_coordinate 
        old_coordinates = self.game.piece.piece_info()
        self.game.piece.rotate()
        new_coordinates = self.game.piece.piece_info()
        self.assertEqual(self.game.piece.rotation, 0)
        self.assertEqual(new_coordinates, old_coordinates)
    """

    def test_out_of_bounds(self):
        self.game.new_piece()
        self.game.piece.x_coordinate = -40
        self.assertTrue(self.game.out_of_bounds())

        self.game.new_piece()
        self.game.piece.x_coordinate = 400
        self.assertTrue(self.game.out_of_bounds())

        self.game.new_piece()
        self.game.piece.y_coordinate = 800
        self.assertTrue(self.game.out_of_bounds())

    def test_full_lines(self):
        initial = self.game.board[19]
        self.game.board[19] = [(0, 0, 0) for i in range(10)]
        self.game.full_lines()
        new = self.game.board[19]
        self.assertEqual(self.game.score, 1)
        self.assertEqual(new, initial)
