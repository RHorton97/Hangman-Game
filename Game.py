import random as rand


class Game():
    '''Holds setup functions and key gameplay data such as the word being
       guessed'''

    def __init__(self):
        self.word = self.wordSelect()
        self.wordLength = len(self.word)
        self.unguessedLetters = self.wordLength
        self.wordWithGuesses = self.wordForGuesses(self.word)
        self.playerWins = False
        self.guessWrong = False

    def wordSelect(self):
        '''Selects a word from the wordList file and stores it to be used in
           the game'''

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
        wordListed = []
        for letter in word:
            wordListed.append("_")

        return wordListed

    def beginGame(self):
        print("The word is " + str(self.wordLength) + " letters long")
        print(self.unguessedLetters * "_ ")

    def letterGuess(self):
        letterGuessed = input("What is your guess? ")
        if letterGuessed in self.word:
            i = 0
            for letter in self.word:
                if letter == letterGuessed:
                    self.wordWithGuesses[i] = letterGuessed

                i = i + 1
        else:
            self.guessWrong = True

        self.allLettersCheck()

    def allLettersCheck(self):
        if "_" not in self.wordWithGuesses:
            self.playerWins = True

    def wordGuess(self):
        wordGuessed = input("What is your guess? ")
        if wordGuessed == self.word:
            self.playerWins = True
        else:
            self.guessWrong = True

    def gameWon():
        pass
