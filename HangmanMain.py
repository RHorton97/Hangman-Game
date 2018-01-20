import tkinter as tk
import Player as play
import Game as game

mainPlayer = play.Player()
runGame = game.Game()

print("Player Name: " + mainPlayer.name)
print("Player Guesses: " + str(mainPlayer.guesses))
print("Chosen Word: " + runGame.word)
print("Word Length: " + str(runGame.wordLength))
runGame.beginGame()
