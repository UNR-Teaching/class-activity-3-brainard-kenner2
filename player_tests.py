import unittest
from tictactoe.board import Board
from tictactoe.player import MockPlayer

class PlayerTester(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(PlayerTester, self).__init__(*args, **kwargs)
        self.board = None

    def setUp(self):
        self.board = Board()

    def test_mock_player(self):
        mockPlayer = MockPlayer('O', [(0, 0)])
        self.assertEqual(mockPlayer.get_move(self.board), (0, 0))    

if __name__ == "__main__":
    unittest.main()