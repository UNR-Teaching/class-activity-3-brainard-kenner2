from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import HumanPlayer, MockPlayer

def main():
    game = Game(HumanPlayer('X'), MockPlayer('O'))
    # game = Game(HumanPlayer('X'), MockPlayer('O', [(0,0), (1,1), (2,2)]))
    game.play_game()

if __name__ == "__main__":
    main()