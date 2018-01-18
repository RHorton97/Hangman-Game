import tkinter as tk
import random as rand

class Player():
    '''Class to hold player information such as the player's name and number of lives
       as well as methods to manipulate the number of lives the player has'''
    def __init__(self):
        self.name = input("What is your name? ")
        self.lives = 5

    def lifeDown(self):
        self.lives = self.lives - 1

    def resetLives(self):
        self.lives = 5

    
class Game():
    '''Holds setup functions and key gameplay data such as the word being guessed'''
    def __init__(self):
        self.word = self.wordSelect()
    
    def wordSelect(self):
        '''Selects a word from the wordList file and stores it to be used in the game'''

        #wordNum range starts from 1 to ensuure that the source URL in the wordList file is never selected as the word
        wordNum = rand.randint(1, 1000)
        wordList = open("wordList.txt", "r")

        for i in range(wordNum+1):
            if i == wordNum:
                word = wordList.readline()
            else:
                wordList.readline()

        wordList.close()
        return word


