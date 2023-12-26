from gameSate import GameState

print("Welcome to TTT.")

def getNumberOfPlayers() -> int:
    player_number = input("Please select number of players (2):")
    if player_number == "":
        return 2
    
    while True:
        try:
            player_number = int(player_number)
            if (0 < player_number <= 2):
                return player_number
            raise ValueError
        except ValueError:
            player_number = input("Invalid number, please select 0, 1 or 2 (2):")


player_number = getNumberOfPlayers()

game = GameState(player_count=player_number)

game.printState()

while game.canContinue():
    game.move()
    game.printState()
    game.printWinner()

