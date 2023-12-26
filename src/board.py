class Board():
    def __init__(self, size: int) -> None:
        self._size = size
        self._board = [[" " for j in range(self._size)] for i in range(self._size)]

    def hasWinner(self) -> None:
        return False

    def printBoard(self) -> None:
        print("Board:")
        for i, row in enumerate(self._board):
            print("|".join([f" {col} " for col in row]))
            print("|".join(["---" for _ in row if i != len(self._board) - 1]))

    def getAvailableSpaces(self) -> list[int]:
        result = []
        for i in range(self._size):
            for j in range(self._size):
                if (self._board[i][j] == " "):
                    result.append((self._size * i) + j + 1)

        return result
    
    def playerMove(self, mark, place):
        col = (place - 1) % self._size
        row = (place - 1) // self._size
        self._board[row][col] = mark