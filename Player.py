class Player():
    '''Class to hold player information such as the player's name and number of
       lives as well as methods to manipulate the number of lives the player
       has'''

    def __init__(self):
        self.name = input("What is your name? ")
        self.guesses = 5

    def guessDown(self):
        '''Remove one guess from total remaining guesses'''
        self.guesses = self.guesses - 1

    def resetGuesses(self):
        '''Resets guesses to five guesses'''
        self.guesses = 5
