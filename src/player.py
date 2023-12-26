import random
import time

class Player():
    def __init__(self, mark: str) -> None:
        self.mark = mark

class HumanPlayer(Player):
    def __init__(self, mark: str) -> None:
        super().__init__(mark)
        self._isAI = False

    def makeMove(self, available_spaces):
        user_move = input("select field:")
        while True:
            try:
                user_move = int(user_move)
                if user_move not in available_spaces:
                    raise ValueError
                return user_move
            except ValueError:
                user_move = input("invalid input:")

class AIPlayer(Player):
    def __init__(self, mark: str, level = 0) -> None:
        super().__init__(mark)
        self._isAI = True
        self._level = level

    def makeMove(self, available_spaces):
        if len(available_spaces) == 1:
            return available_spaces[0]
        random.seed(time.time())
        return available_spaces[random.randrange(0, len(available_spaces) -1, 1)]