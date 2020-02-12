
from board import Board

NO_WIN = 0
PLAYER_1_WIN = 1
PLAYER_2_WIN = 2
TIED = 3

class Game():
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2

    def turn(self, board, player):
        valid_move = False
        while not valid_move:
            col, row = current_player.get_move()
            valid_move = self.board.mark_square(col, row, player.mark)

        return get_win_state()

    def play_game(self):
        current_player = self.player1
        while self.turn(self.board, current_player) == NO_WIN:
            current_player self.player1 if current_player is self.player2 else self.player2

    def player_won(self, mark):
        if self.board[0][0] == mark and self.board[1][1] == mark and self.board[2][2] == mark:
            return True

        if self.board[0][2] == mark and self.board[1][1] == mark and self.board[2][0] == mark:
            return True

        for i in range(3):
            vertical = True
            for j in range(3):
                vertical = vertical and self.board[i][j] == mark
            if vertical:
                return True

        for i in range(3):
            horizontal = True
            for j in range(3):
                horizontal = horizontal and self.board[j][i] == mark
            if horizontal:
                return True

        return False

    def get_winner(self):
        """
        Checks to see if there is a current winner of the game

        :return: player1, player2, or None if no winner
        """

        if self.player_won(self.player1.mark):
            return self.player1

        if self.player_won(self.player2.mark):
            return self.player2

        return None

    def get_win_state(self):
        if not self.board_valid():
            raise ValueError("Board state is not valid!")

        player_won = self.get_win_state()
        if player_won is self.player1:
            return PLAYER_1_WIN
        if player_won is self.player2:
            return PLAYER_2_WIN

        if self.board.board_full():
            return TIED

        return NO_WIN


    def board_valid(self):
        """
        Checks if the board has the correct number of X and O values
        """
        x_count = 0
        o_count = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 'X':
                    x_count += 1
                elif self.board[i][j] == 'O':
                    o_count += 1
        return abs(x_count - o_count) <= 1