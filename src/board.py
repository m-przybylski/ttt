import copy

class Board():
    def __init__(self, size: int) -> None:
        self._size = size
        self._board = [[" " for j in range(self._size)] for i in range(self._size)]

    def hasWinner(self) -> None:
        return self.getWinner() != None
    
    def getWinner(self):
        left_top = self._board[0][0]
        right_top = self._board[0][self._size - 1]
        d1 = []
        d2 = []
        for i in range(self._size):
            char_r = self._board[i][0]
            char_c = self._board[0][i]

            if len([char_r for j in range(self._size) if self._board[i][j] == char_r and char_r != " "]) == self._size:
                return char_r
            if len([char_c for j in range(self._size) if self._board[j][i] == char_c and char_c != " "]) == self._size:
                return char_c
            
            d1.append(self._board[i][i])
            d2.append(self._board[i][self._size - 1 - i])
            
        if all([d == left_top and left_top != " " for d in d1]):
            return left_top

        if all([d == right_top and right_top != " " for d in d2]):
            return right_top

        return None

    def printBoard(self) -> None:
        print("Board:")
        for i, row in enumerate(self._board):
            print("|".join([f" {(self._size * i) + j + 1 if col == ' ' else col} " for j, col in enumerate(row)]))
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

    def copy(self):
        return copy.deepcopy(self)