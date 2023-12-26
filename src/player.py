from board import Board
import random
import time

class Player():
    def __init__(self, mark: str, opponent_mark: str) -> None:
        self.mark = mark
        self.opponent_mark = opponent_mark

class HumanPlayer(Player):
    def __init__(self, mark: str, opponent_mark: str) -> None:
        super().__init__(mark, opponent_mark)
        self._isAI = False

    def makeMove(self, board: Board):
        available_spaces = board.getAvailableSpaces()
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
    def __init__(self, mark: str, opponent_mark: str, level = 0) -> None:
        super().__init__(mark, opponent_mark)
        self._isAI = True
        self._level = level

    def _getRandomValue(self, available_spaces):
        if len(available_spaces) == 1:
            return available_spaces[0]
        random.seed(time.time())
        return available_spaces[random.randrange(0, len(available_spaces) -1, 1)]
    

    def _evaluate(self, board: Board):
        winner = board.getWinner()
        if winner == self.mark:
            return 10
        if winner == self.opponent_mark:
            return -10
        
        return 0

    def _minimax(self, board: Board, depth: int, isMaximizingPlayer: bool):
        score = self._evaluate(board)
        available_spaces = board.getAvailableSpaces()
        if score in [10, -10]:
            return score
        
        if len(available_spaces) == 0:
            return 0
        
        if isMaximizingPlayer:
            best = -100
            for available_space in available_spaces:
                next_board = board.copy()
                next_board.playerMove(self.mark, available_space)
                best = max(best, self._minimax(next_board, depth + 1, not isMaximizingPlayer))

            return best - depth
        else:
            best = 100
            for available_space in available_spaces:
                next_board = board.copy()
                next_board.playerMove(self.opponent_mark, available_space)
                best = min(best, self._minimax(next_board, depth + 1, not isMaximizingPlayer))

            return best + depth

    def makeMove(self, board: Board):
        if self._level == 0:
            available_spaces = board.getAvailableSpaces()
            return self._getRandomValue(available_spaces)
        if self._level == 1:
            available_spaces = board.getAvailableSpaces()
            for available_space in available_spaces:
                next_board = board.copy()
                next_board.playerMove(self.mark, available_space)
                if (next_board.getWinner() == self.mark):
                    return available_space
                

        if self._level == 2:
            available_spaces = board.getAvailableSpaces()
    
            best_score = -100
            best_move = None
            for available_space in available_spaces:
                next_board = board.copy()
                next_board.playerMove(self.mark, available_space)
                current_score = self._minimax(next_board, 0, False)
                if (current_score > best_score):
                    best_score = current_score
                    best_move = available_space

            return best_move

        return self._getRandomValue(available_spaces)