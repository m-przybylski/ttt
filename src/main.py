from gameSate import GameState

print("Welcome to TTT.")

def getAiLevel() -> int:
    user_choice = input("Select AI level (b)eginer (e)xpert: (b)")
    if user_choice == "":
        return 0
    
    while user_choice == "" or user_choice not in "beBE":
        user_choice = input("Select AI level (b)eginer (e)xpert: (b)")
        if user_choice.lower() == "b":
            return 0

        if user_choice.lower() == "e":
            return 1


def getNumberOfPlayers() -> int:
    player_number = input("Please select number of players (2):")
    if player_number == "":
        return 2
    
    while True:
        try:
            ai = None
            player_number = int(player_number)
            if (0 <= player_number <= 2):
                if (player_number < 2):
                    ai = getAiLevel()
                return (player_number, ai)
            raise ValueError
        except ValueError:
            player_number = input("Invalid number, please select 0, 1 or 2 (2):")



def gameLoop():
    user_choice = ""

    while True:
    
        while user_choice == "" or user_choice not in "qnQN":
            user_choice = input("(n)ew game, (q)uit: (n)")
            if user_choice == "":
                user_choice = "n"

        if user_choice.lower() == "n":
            user_choice = ""
            player_number, ai_level = getNumberOfPlayers()
            game = GameState(player_count=player_number, ai_level=ai_level)

            while game.canContinue():
                game.move()
                game.printState()
                game.printWinner()

        if user_choice.lower() == 'q':
            exit()

gameLoop()
