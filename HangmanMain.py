import Player as play
import Game as game

# Initialises gameplay class objects
mainPlayer = play.Player()
runGame = game.Game()

###############################################################################
#                                   TESTS                                     #
###############################################################################
#print("Player Name: " + mainPlayer.name)                                     #
#print("Player Guesses: " + str(mainPlayer.guesses))                          #
print("Chosen Word: " + runGame.word)                                        #
#print("Word Length: " + str(runGame.wordLength))                             #
                                                                              #
#runGame.beginGame()                                                          #
###############################################################################

runGame.beginGame()
playGame = True
while playGame == True:
    validType = False
    while validType == False:
        guessType = int(input("Press 1 to guess a letter or press 2 to guess the word. "))
        if guessType == 1 or 2:
            validType = True

    if guessType == 1:
        runGame.letterGuess()
    elif guessType == 2:
        runGame.wordGuess()
    else:
        raise ValueError("Invalid guess type selection")

    if runGame.guessWrong == True:
        mainPlayer.guessDown()
        runGame.guessWrong = False
        if mainPlayer.guesses <= 0:
            runGame.gameLost()
            playGame = False
    elif runGame.playerWins == True:
        runGame.gameWon()
        playGame = False
