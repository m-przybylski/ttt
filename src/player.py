class Player():
    def __init__(self, mark: str) -> None:
        self.mark = mark

class HumanPlayer(Player):
    def __init__(self, mark: str) -> None:
        super().__init__(mark)
        self._isAI = False

    def makeMove(self):
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

    def makeMove(self):
        user_move = input("select field:")
        print(user_move)
