class Board(object):

    def __init__(self):
        """
        Initializes the Board of size 3x3
        """
        self.board = [['_' for _ in range(3)] for _ in range(3)]

    def mark_square(self, column, row, mark):
        """
        Marks a square at coordinate (column, row) for player

        :param column: (int) the 0-indexed column of the Board to mark
        :param row: (int) the 0-indexed row of the Board to mark
        :param mark: (str) the X or O representation of which player to mark in square

        :return: true on sucess, false on error
        """
        if self.out_of_bounds(column, row):
            return False
        if not self.square_empty(column, row):
            return False
        self.board[column][row] = mark
        return True

    def out_of_bounds(self, column, row):
        """
        Returns true if the space specified by the column and row is out of bounds
        """
        if column < 0 or column >= 3 or row < 0 or row >= 3:
            return True
        return False

    def square_empty(self, column, row):
        """
        Returns true if the space specified by the column and row is empty 
        """
        if self.out_of_bounds(column, row):
            return False
        return self.board[column][row] == '_'

    def board_full(self):
        """
        Returns true if the board is full
        """
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '_':
                    return False

        return True