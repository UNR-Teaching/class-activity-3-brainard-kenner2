from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.board import HumanPlayer

def main():
    game = Game(HumanPlayer('X'), HumanPlayer('O'))
    game.play_game()

if __name__ == "__main__":
    main()