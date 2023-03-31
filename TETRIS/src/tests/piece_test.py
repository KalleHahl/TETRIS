import unittest
from src.tetris_logic.piece import Piece

class TestPiece(unittest.TestCase):

    def setUp(self):
        self.piece = Piece(0, 0)
        self.piece.piece = 'T'


    def test_initial_position(self):
        self.assertEqual(self.piece.x_coordinate, 0)
        self.assertEqual(self.piece.y_coordinate, 0)

    def test_piece_info(self):
        expected_piece_info = [(0, 0), (-1, 0), (1, 0), (0, -1)]
        self.assertEqual(self.piece.piece_info(), expected_piece_info)


    def test_rotate(self):
        expected_piece_info = [(0, 0), (0, -1), (0, 1), (1, 0)]
        self.piece.rotate()
        self.assertEqual(self.piece.piece_info(), expected_piece_info)
    
    def test_back_to_first_rotation(self):
        self.piece.rotation = 3
        excpected_piece_info = [(0, 0), (-1, 0), (1, 0), (0, -1)]
        self.piece.rotate()
        self.assertEqual(self.piece.piece_info(), excpected_piece_info)