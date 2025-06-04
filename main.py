from state_manager import *
import random

class Main:
    words = ["hangman", "ham", "armistice", "apple", "train", "chair", "house", "dance", "giraffe", "puzzle", "jungle", "mountain", "travel", "elephant", "thunderstorm", "chocolate", "revolution", "quarantine", "bread", "water", "light", "orange", "jacket", "planet", "algorithm", "enthusiasm", "hypothesis", "kaleidoscope", "candy", "bird", "beach", "library", "galaxy", "tranquility", "renaissance", "paradox", "unbelievable", "serendipity", "flower", "skate", "pizza", "ball", "discover", "butterfly", "triangle", "satellite", "incomprehensible", "metamorphasis", "circumference", "hypothetical", "Oxymoron"]

    def __init__(self):
        self.start_screen()
        self.start()

    def start_screen(self):
        print("\033[2J\033[1;1f")

        print(StateManager.HANGMANPICS[-1])
        print()
        print("""
        |    |    ^    |\   |   ===  |\    /|    ^   |\  |
        |====|   /=\   |  \ |  |  _  | \  / |   /=\  | \ |
        |    |  /   \  |   \|  \___| |  \/  |  /   \ |  \|
        """)

        print()
        input("The Game of Puzzling Fun! (Press Enter to Continue) ")

    def start(self):
        print("\033[2J\033[1;1f")

        state = ""

        self.game_mode = input("How many players . . . (1 or 2)? ")

        if self.game_mode == "2":
            player_1 = input("Who here wants to be Player 1? : ")
            player_2 = input("And Player 2... : ")

            word = input("Okay! " + player_2 + " look away! Okay, " + player_1 + ", whats the word? : ")

            state = StateManager(player_1, "2 player", word, player_2=player_2)
            state = state.two_player()

            input("Press Enter to close the game . . . ")
        elif self.game_mode == "1":
            player_1 = input("Who's player 1? ")

            word = random.choice(self.words)

            state = StateManager(player_1, "1 player", word)
            state.one_player()

            input("Press Enter to close the game . . . ")
    
main = Main()
