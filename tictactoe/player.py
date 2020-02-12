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
    def __init__(self, mark, actions):
        super(MockPlayer, self).__init__(mark)
        self.actions = actions


    def get_move(self, board):
        move = self.actions.pop(0)
        if move is None:
            raise ValueError("MockPlayer is out of actions!")

        col, row = move

        if not board.valid_move(col, row):
            raise ValueError("Action queued was invalid!")

        return col, row

class DummyPlayer(Player):
    def get_move(self, board):
        return 0, 0