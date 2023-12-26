from board import Board
from player import HumanPlayer, AIPlayer

class GameState():
    def __init__(self, board_size = 3, player_count = 2) -> None:
        assert 0 < player_count <= 2
        self._board = Board(board_size)
        self._players = [HumanPlayer(mark) for mark in "XO"[:player_count]] + [AIPlayer(mark) for mark in "XO"[player_count:]]
        self.current_player = self._players[0]

    def canContinue(self):
        return len(self._board.getAvailableSpaces()) > 0 or not self._board.hasWinner()
    
    def move(self):
        move = self.current_player.makeMove()
        self._board.playerMove(self.current_player.mark, move)
        self._nextPlayer()


    def _nextPlayer(self):
        playerIndex = self._players.index(self.current_player) - 1
        self.current_player = self._players[playerIndex]

    def printState(self):
        print(f"Current player: {self.current_player.mark}")
        print(f"Available spots: {self._board.getAvailableSpaces()}")

        self._board.printBoard()