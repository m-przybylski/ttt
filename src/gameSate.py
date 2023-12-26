from board import Board
from player import HumanPlayer, AIPlayer

class GameState():
    def __init__(self, board_size = 3, player_count = 2, ai_level = 0) -> None:
        assert 0 <= player_count <= 2
        self._board = Board(board_size)
        self._players = [HumanPlayer(mark) for mark in "XO"[:player_count]] + [AIPlayer(mark, ai_level) for mark in "XO"[player_count:]]
        self.current_player = self._players[0]

    def canContinue(self):
        return not len(self._board.getAvailableSpaces()) == 0 and not self._board.hasWinner()
    
    def move(self):
        self._board.printBoard()
        move = self.current_player.makeMove(self._board.getAvailableSpaces())
        self._board.playerMove(self.current_player.mark, move)
        self._nextPlayer()

    def printWinner(self):
        winner = self._board.getWinner()
        if len(self._board.getAvailableSpaces()) == 0:
            print("Tie")
        elif winner != None:
            print(f"{winner} wins!")

    def _nextPlayer(self):
        playerIndex = self._players.index(self.current_player) - 1
        self.current_player = self._players[playerIndex]

    def printState(self):
        print(f"Current player: {self.current_player.mark}")
        print(f"Available spots: {self._board.getAvailableSpaces()}")

        self._board.printBoard()