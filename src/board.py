class Board():
    def __init__(self, size: int) -> None:
        self._size = size
        self._board = [[" " for j in range(self._size)] for i in range(self._size)]

    def hasWinner(self) -> None:
        pass

    def printBoard(self) -> None:
        print("Board:")
        for i, row in enumerate(self._board):
            print("|".join([f" {col} " for col in row]))
            print("|".join(["---" for _ in row if i != len(self._board) - 1]))
