import colorama

colorama.init()


class StateManager:
    HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========''']

    letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]

    def __init__(self, player_1, game_mode, word, player_2=None):
        self.player_1 = player_1

        if game_mode == "2 player":
            self.player_2 = player_2
            self.game_mode = game_mode

            self.word = word

            #allows upper and lower case
            self.word_letters = word.lower() + word.upper()
            self.tries_left = 7
            self.won = False

            #which phase hangman pic is in
            self.state = 0
            self.tries = 0
            self.guessed_string = ""
            self.guessed_letters = ["_" for i in range(len(word))]

            s = ""
            
            if len(word) > 1:
                s = "s"

            print(player_1.title() + " chose a word " + str(len(word)) + " letter " + s + " long.")
        else:
            self.game_mode = game_mode

            self.word = word

            #allows upper and lower case
            self.word_letters = word.lower() + word.upper()
            self.tries_left = 7
            self.won = False

            #which phase hangman pic is in
            self.state = 0
            self.tries = 0
            self.guessed_string = ""
            self.guessed_letters = ["_" for i in range(len(word))]

            s = ""
            
            if len(word) > 1:
                s = "s"

            print("The word length is " + str(len(self.word)) + " letters long.")

    #main game sequence
    def two_player(self):
        letter = ""

        self.guessed_string = " ".join(self.guessed_letters)

        #main game loop
        while self.tries_left > 0:
            #set won to be true
            if "".join(self.guessed_letters) == self.word:
                self.won = True
                break

            print("\033[2J\033[1;1f")
            print(self.HANGMANPICS[self.state])
            print()
            print(self.guessed_string)
            print()
            print(" ".join(self.letters[:10]))
            print(" ".join(self.letters[10:19]))
            print(" ".join(self.letters[19:]))
            

            #first try?
            if self.tries == 0:
                letter = input("What letter do you choose, " + self.player_2 + "? ")

                if self.check_letter(letter) == "finished":
                    print("done!")
                    return

            #not first try
            else:
                letter = input("What next, " + self.player_2 + "? ")

                if self.check_letter(letter) == "finished":
                    print("done!")
                    return
                
            #update tries amount
            self.tries += 1
                
        self.finished()

    def one_player(self):
        letter = ""

        self.guessed_string = " ".join(self.guessed_letters)

        #main game loop
        while self.tries_left > 0:
            #set won to be true
            if "".join(self.guessed_letters) == self.word:
                self.won = True
                break

            print("\033[2J\033[1;1f")
            print(self.HANGMANPICS[self.state])
            print()
            print(self.guessed_string)
            print()
            print(" ".join(self.letters[:10]))
            print(" ".join(self.letters[10:19]))
            print(" ".join(self.letters[19:]))
            

            #first try?
            if self.tries == 0:
                letter = input("What letter do you choose, " + self.player_1 + "? ")

                if self.check_letter(letter) == "finished":
                    print("done!")
                    return

            #not first try
            else:
                letter = input("What next, " + self.player_1 + "? ")

                if self.check_letter(letter) == "finished":
                    print("done!")
                    return
                
            #update tries amount
            self.tries += 1
                
        self.finished()


    def check_letter(self, letter):
        if len(letter) == 1 and letter in self.word_letters:
            if not list(self.word).count(letter) > 1:
                #replace all instances in word_letters
                self.word_letters = self.word_letters.replace(letter.lower(), "")
                self.word_letters = self.word_letters.replace(letter.upper(), "")

                self.guessed_letters[self.word.index(letter.lower())] = letter

                self.guessed_string = " ".join(self.guessed_letters)

                self.remove_letter(letter)

                print(self.guessed_string)
            else:
                #replace all instances in word_letters, but also makes sure to check for two of same letters in word
                self.word_letters = self.word_letters.replace(letter.lower(), "")
                self.word_letters = self.word_letters.replace(letter.upper(), "")

                word = self.word

                for index in self.find_all_indices(word, letter):
                    self.guessed_letters[index] = letter

                print(self.guessed_letters)

                self.guessed_string = " ".join(self.guessed_letters)

                self.remove_letter(letter)

                print(self.guessed_string)
        elif letter == "end":
            return "finished"
        elif not len(letter) == 1:
            letter = input("Uh oh! Invalid character, try again! ")

            self.check_letter(letter)
        #checks if letter not in word_letters
        elif not letter in self.word_letters:
            self.state += 1
            self.tries_left -= 1

            self.remove_letter(letter)

    def find_all_indices(self, string, substring):
        indices = []
        start = 0

        while True:
            start = string.find(substring, start)
            if start == -1:
                break
            indices.append(start)
            start += 1

        return indices

    def remove_letter(self, letter):
        try:
            self.letters[self.letters.index(letter)] = "/"
        except ValueError:
            pass

    def finished(self):
        if self.game_mode == "2 player":
            if self.won == True:
                print("\033[2J\033[1;1f")
                print("Great Job, " + self.player_2 + "! YOU WON! The word was, drumroll please . . . " + self.word.upper() + "!!!")
            else:
                print("\033[2J\033[1;1f")
                print("Aww, Nice try, " + self.player_2 + ", you almost had it. The word was " + self.word.upper() + "! \nGood job, " + self.player_1 + "!")
        else:
            if self.won == True:
                print("\033[2J\033[1;1f")
                print("Great Job, " + self.player_1 + "! YOU WON! The word was, drumroll please . . . " + self.word.upper() + "!!!")
            else:
                print("\033[2J\033[1;1f")
                print("Aww, Nice try, " + self.player_1 + ", you almost had it. The word was " + self.word.upper() + "!")