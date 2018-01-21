import Game as game

# Initialises gameplay class objects
runGame = game.Game()

###############################################################################
#                                   TESTS                                     #
###############################################################################
#print("Player Name: " + runGame.name)                                        #
#print("Player Guesses: " + str(runGame.guesses))                             #
print("Chosen Word: " + runGame.word)                                        #
#print("Word Length: " + str(runGame.wordLength))                             #
                                                                              #
#runGame.beginGame()                                                          #
###############################################################################

playAgain = True
while playAgain == True:
    runGame.beginGame()
    playGame = True
    while playGame == True:
        validChoice = False
        while validChoice == False:
            guessType = input("Press 1 to guess a letter or press 2 to guess the word. ")
            try:
                guessType = int(guessType)
            except ValueError:
                continue
            if guessType == 1 or 2:
                validChoice = True

        if guessType == 1:
            runGame.letterGuess()
        elif guessType == 2:
            runGame.wordGuess()
        else:
            raise ValueError("Invalid guess type selection")

        if runGame.gameOver == True:
            validChoice = False
            while validChoice == False:
                playAgain = input("\nDo you want to play again? y/n  ")
                if playAgain.lower() == "n":
                    validChoice = True
                    playGame = False
                    playAgain = False
                elif playAgain.lower() == "y":
                    validChoice = True
                    playGame = False
                    playAgain = True
                    runGame.resetGame()
