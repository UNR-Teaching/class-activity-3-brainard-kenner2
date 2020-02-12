import abc

class Player(object):
    def __init__(self, mark):
        self.mark = mark
    
    @abc.abstractmethod
    def get_move(self, board):
        pass

class HumanPlayer(Player):
    def get_move(self, board):
        print("Please enter column then row:")
        input_col = int(input())
        input_row = int(input())
        return input_col, input_row

class MockPlayer(Player):
    def get_move(self, board):
        raise NotImplementedError("smile")