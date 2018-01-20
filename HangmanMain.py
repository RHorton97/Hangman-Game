import Player as play
import Game as game

# Initialises gameplay class objects
mainPlayer = play.Player()
runGame = game.Game()

###############################################################################
#                                    TESTS                                    #
###############################################################################
print("Player Name: " + mainPlayer.name)
print("Player Guesses: " + str(mainPlayer.guesses))
print("Chosen Word: " + runGame.word)
print("Word Length: " + str(runGame.wordLength))

runGame.beginGame()
###############################################################################

# if game.guessWrong == True:
#    mainPlayer.guessDown()
#    game.guessWrong = False
#    if mainPlayer.guesses <= 0:
#        game.gameLost()
