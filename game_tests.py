import unittest
from tictactoe.board import Board
from tictactoe.player import HumanPlayer
from tictactoe.game import Game, NO_WIN, PLAYER_1_WIN, PLAYER_2_WIN, TIED

class GameTester(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(GameTester, self).__init__(*args, **kwargs)
        self.game = None

    def setUp(self):
        self.game = Game(HumanPlayer('X'), HumanPlayer('O'))

    def test_has_winner_diagonal(self):
        for i in range(3):
            self.game.board.mark_square(i, i, 'X')
        self.game.board.mark_square(0, 1, 'O')
        self.game.board.mark_square(0, 2, 'O')
        self.assertEqual(self.game.get_win_state(), PLAYER_1_WIN)

    def test_has_winner_horizontal(self):
        for i in range(3):
            self.game.board.mark_square(i, 0, 'O')
        self.game.board.mark_square(0, 1, 'X')
        self.game.board.mark_square(0, 2, 'X')
        self.assertEqual(self.game.get_win_state(), PLAYER_2_WIN)

    def test_has_winner_vertical(self):
        for i in range(3):
            self.game.board.mark_square(0, i, 'X')
        self.game.board.mark_square(1, 1, 'O')
        self.game.board.mark_square(1, 2, 'O')
        self.assertEqual(self.game.get_win_state(), PLAYER_1_WIN)

    def test_has_no_winner(self):
        self.game.board.mark_square(0, 0, 'X')
        self.game.board.mark_square(1, 1, 'O')
        self.game.board.mark_square(2, 2, 'X')
        self.assertEqual(self.game.get_win_state(), NO_WIN)

    def test_has_no_winner_empty_board(self):
        self.assertEqual(self.game.get_win_state(), NO_WIN)
    
    def test_has_no_winner_tie(self):
        self.game.board.mark_square(0, 0, 'O')
        self.game.board.mark_square(0, 1, 'X')
        self.game.board.mark_square(0, 2, 'X')
        self.game.board.mark_square(1, 0, 'X')
        self.game.board.mark_square(1, 1, 'X')
        self.game.board.mark_square(1, 2, 'O')
        self.game.board.mark_square(2, 0, 'O')
        self.game.board.mark_square(2, 1, 'O')
        self.game.board.mark_square(2, 2, 'X')
        self.assertEqual(self.game.get_win_state(), TIED)

    def test_board_tied_not_full(self):
        self.game.board.mark_square(1, 1, 'X')
        self.game.board.mark_square(1, 2, 'O')
        self.game.board.mark_square(2, 0, 'O')
        self.game.board.mark_square(2, 1, 'X')
        self.game.board.mark_square(2, 2, 'O')
        self.assertEqual(self.game.get_win_state(), NO_WIN)

    def test_board_valid_correct(self):
        self.game.board.mark_square(1, 1, 'X')
        self.game.board.mark_square(1, 2, 'O')
        self.game.board.mark_square(2, 0, 'O')
        self.assertTrue(self.game.board_valid())

    def test_board_valid_empty(self):
        self.assertTrue(self.game.board_valid())

    def test_board_valid_too_many_X(self):
        self.game.board.mark_square(1, 1, 'X')
        self.game.board.mark_square(1, 2, 'X')
        self.game.board.mark_square(2, 0, 'X')
        self.assertFalse(self.game.board_valid())

if __name__ == "__main__":
    unittest.main()