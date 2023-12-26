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
                return int(user_move)
            except ValueError:
                user_move = input("invalid input:")

class AIPlayer(Player):
    def __init__(self, mark: str) -> None:
        super().__init__(mark)
        self._isAI = True

    def makeMove(self, available_spaces):
        random.seed(time.time())
        return available_spaces[random.randrange(0, len(available_spaces) -1, 1)]