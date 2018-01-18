import tkinter as tk
import random as rand

class Player():
    '''Class to hold player information such as the player's name and number of lives
       as well as methods to manipulate the number of lives the player has'''
    def __init__(self):
        self.name = input("What is your name? ")
        self.guesses = 5

    def guessDown(self):
        '''Remove one guess from total remaining guesses'''
        self.guesses = self.guesses - 1

    def resetGuesses(self):
        '''Resets guesses to five guesses'''
        self.guesses = 5

    
class Game():
    '''Holds setup functions and key gameplay data such as the word being guessed'''
    def __init__(self):
        self.word = self.wordSelect()
        self.wordLength = len(self.word)
    
    def wordSelect(self):
        '''Selects a word from the wordList file and stores it to be used in the game'''

        #wordNum range starts from 1 to ensuure that the source URL in the wordList file is never selected as the word
        wordNum = rand.randint(1, 1000)
        wordList = open("wordList.txt", "r")

        for i in range(wordNum+1):
            if i == wordNum:
                word = wordList.readline()
                word = word[:-1]
            else:
                wordList.readline()

        wordList.close()
        return word

mainPlayer = Player()
runGame = Game()

print("Player Name: " + mainPlayer.name)
print("Player Guesses: " + str(mainPlayer.guesses))
print("Chosen Word: " + runGame.word)
print("Word Length: " + str(runGame.wordLength))
