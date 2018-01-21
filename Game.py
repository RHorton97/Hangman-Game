import random as rand


class Game():
    """Holds setup functions and key gameplay data such as the word being
       guessed"""

    def __init__(self):
        self.name = input("What is your name? ")
        self.guesses = 5
        self.word = self.wordSelect()
        self.wordLength = len(self.word)
        self.unguessedLetters = self.wordLength
        self.wordWithGuesses = self.wordForGuesses(self.word)
        self.playerWins = False
        self.guessWrong = False
        self.gameOver = False

    def beginGame(self):
        """Begins the game by stating the length of the word and showing a blank space with underscores to represent
           each letter of the word"""
        print("You have " + str(self.guesses) + " wrong guesses")
        print("\nThe word is " + str(self.wordLength) + " letters long")
        print(self.unguessedLetters * "_ " + "\n")

    def resetGame(self):
        self.gameOver = False
        self.guesses = 5
        self.word = self.wordSelect()
        self.wordLength = len(self.word)
        self.unguessedLetters = self.wordLength
        self.wordWithGuesses = self.wordForGuesses(self.word)

    def guessDown(self):
        """Remove one guess from total remaining guesses"""
        self.guesses = self.guesses - 1

    def wordSelect(self):
        """Selects a word from the wordList file and stores it to be used in
           the game"""

        # wordNum range starts from 1 to ensuure that the source URL in the
        # wordList file is never selected as the word
        wordNum = rand.randint(1, 1000)
        wordList = open("wordList.txt", "r")

        for i in range(wordNum + 1):
            if i == wordNum:
                word = wordList.readline()
                word = word[:-1]
            else:
                wordList.readline()

        wordList.close()
        return word

    def wordForGuesses(self, word):
        """Creates a list containing one underscore as an element for each letter of the chosen word which is taken as
           input to the function"""
        wordListed = []
        for letter in word:
            wordListed.append("_")

        return wordListed

    def wordGuess(self):
        """Allows the user to input a word as a guess, if the word is correct then the player wins the game, if the
           word is not correct then the player is told and the list of guessed and unguessed letters is printed so that
           it is visible to the player"""
        wordGuessed = input("What is your guess? ")
        if wordGuessed == self.word:
            self.playerWins = True
            print("Congratulations! You guessed correctly, the word was " + self.word + "!")
            self.gameWon()
        else:
            print("Sorry, that isn't the word")
            self.guessDown()
            self.lifeCheck()

    def letterGuess(self):
        """Allows the user to input a letter as a guess, if the letter is in the word then it replaces the appropriate
           characters in the list created by wordForGuesses, if the letter is not in the word then the player is told
           that they were wrong. The list containing underscores and letters is displayed at the end of the function
           each time in order to ensure it is visible to the player at all times"""
        letterGuessed = input("What is your guess? ")
        if letterGuessed in self.word:
            i = 0
            for letter in self.word:
                if letter == letterGuessed:
                    self.wordWithGuesses[i] = letterGuessed

                i = i + 1
        else:
            print("Sorry, that letter isn't in the word")
            self.guessDown()
            self.lifeCheck()

        self.allLettersCheck()

        if self.playerWins == False:
            if self.unguessedLetters == 1:
                print("There is " + str(self.unguessedLetters) + " letter left to guess\n")
            else:
                print("There are " + str(self.unguessedLetters) + " letters left to guess\n")

            showWordGuesses = ""
            for letter in self.wordWithGuesses:
                showWordGuesses = showWordGuesses + letter + " "

            print(showWordGuesses + "\n")

    def allLettersCheck(self):
        """Checks if the player has guessed all the letters in the word correctly, if they have then the player wins
           the game, if not the function determines how many letters are left to be guessed and updates the unguessed
           letters value"""
        if "_" not in self.wordWithGuesses:
            self.playerWins = True
            self.gameWon()
        else:
            i = 0
            for letter in self.wordWithGuesses:
                if letter == "_":
                    i = i + 1
                else:
                    continue
            self.unguessedLetters = i

    def lifeCheck(self):
        if self.guesses <= 0:
            print("You have no wrong guesses remaining")
            self.gameLost()
        else:
            print("You have " + str(self.guesses) + " wrong guesses left")

    def gameWon(self):
        """This function tells the player they have won"""
        self.gameOver = True
        print("\nCongratulations " + self.name + "! You Win!")

    def gameLost(self):
        """This function tells the player they have lost"""
        self.gameOver = True
        print("\nThe word was " + self.word)
        print("\nSorry " + self.name + ". You Lose!")
