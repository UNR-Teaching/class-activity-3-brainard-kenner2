import unittest
from tictactoe.board import Board
from tictactoe.player import MockPlayer, DummyPlayer
from tictactoe.game import Game, NO_WIN, PLAYER_1_WIN, TIED

class IntegrationTester(unittest.TestCase):
    def test_no_win(self):
        board = Board()
        player = MockPlayer('X', [(0, 0)])
        game = Game(player, DummyPlayer('O'))
        self.assertEqual(game.turn(board, player), NO_WIN)

    def test_win(self):
        board = Board()
        board.board[0][0] = 'X'
        board.board[0][1] = 'O'
        board.board[1][1] = 'X'
        board.board[1][0] = 'O'
        player = MockPlayer('X', [(2, 2)])
        game = Game(player, DummyPlayer('O'))

        self.assertEqual(game.turn(board, player), PLAYER_1_WIN)

    def test_tie(self):
        board = Board()
        board.board[0][0] = 'O'
        board.board[0][1] = 'X'
        board.board[0][2] = 'X'
        board.board[1][0] = 'X'
        board.board[1][1] = 'X'
        board.board[1][2] = 'O'
        board.board[2][0] = 'O'
        board.board[2][1] = 'O'
        player = MockPlayer('X', [(2, 2)])
        game = Game(player, DummyPlayer('O'))

        self.assertEqual(game.turn(board, player), TIED)

if __name__ == "__main__":
    unittest.main()