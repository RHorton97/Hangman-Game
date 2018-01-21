import Game as game

# Initialises gameplay class objects
runGame = game.Game()

###############################################################################
#                                   TESTS                                     #
###############################################################################
#print("Player Name: " + runGame.name)                                     #
#print("Player Guesses: " + str(runGame.guesses))                          #
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
        guessType = input("Press 1 to guess a letter or press 2 to guess the word. ")
        try:
            guessType = int(guessType)
        except ValueError:
            continue
        if guessType == 1 or 2:
            validType = True

    if guessType == 1:
        runGame.letterGuess()
    elif guessType == 2:
        runGame.wordGuess()
    else:
        raise ValueError("Invalid guess type selection")

    if runGame.guessWrong == True:
        runGame.guessDown()
        runGame.guessWrong = False
        if runGame.guesses <= 0:
            runGame.gameLost()
            playGame = False
    elif runGame.playerWins == True:
        runGame.gameWon()
        playGame = False
