import unittest
from tictactoe.board import Board

class BoardTester(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BoardTester, self).__init__(*args, **kwargs)
        self.board = None

    def setUp(self):
        self.board = Board()

    def test_mark_square_normal_use_X(self):
        self.assertTrue(self.board.mark_square(1, 2, 'X'))
        self.assertEqual(self.board.board[1][2], 'X')
    
    def test_row_out_of_bounds(self):
        self.assertTrue(self.board.out_of_bounds(0, 3))
    
    def test_col_out_of_bounds(self):
        self.assertTrue(self.board.out_of_bounds(3, 0))

    def test_row_col_in_bounds(self):
        self.assertFalse(self.board.out_of_bounds(0, 0))

    def test_empty_square(self):
        self.assertTrue(self.board.square_empty(0, 0))

    def test_non_empty_square(self):
        self.board.mark_square(0, 0, 'O')
        self.assertFalse(self.board.square_empty(0, 0))

    def test_board_full(self):
        for i in range(3):
            for j in range(3):
                self.board.mark_square(i, j, 'O')
        self.assertTrue(self.board.board_full())

    def test_board_not_full(self):
        for i in range(3):
            self.board.mark_square(i, i, 'O')
        self.assertFalse(self.board.board_full())

    def test_mark_square_normal_use_O(self):
        self.assertTrue(self.board.mark_square(1, 2, 'O'))
        self.assertEqual(self.board.board[1][2], 'O')

    def test_mark_square_out_of_bounds_X(self):
        self.assertFalse(self.board.mark_square(1, 4, 'X'))

    def test_mark_square_out_of_bounds_O(self):
        self.assertFalse(self.board.mark_square(1, 4, 'O'))

    def test_mark_square_out_of_bounds_row_and_col(self):
        self.assertFalse(self.board.mark_square(5, 4, 'X'))

if __name__ == "__main__":
    unittest.main()