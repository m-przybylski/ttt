from gameSate import GameState

game = GameState()

game.printState()

while game.canContinue():
    game.move()
    game.printState()
    game.printWinner()