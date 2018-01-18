import tkinter as tk
import random as rand

class player():
    def __init__(self, name):
        self.name = name
        self.lives = 5

    def lifeDown(self):
        self.lives = self.lives - 1

    def resetLives(self):
        self.lives = 5

    
