#Imports the random module.
import random

#Sets up the lives to 6.
lives = 6

#Sets up the lettersGuessed to print out the guessed word.
lettersGuessed = ""

#Sets up the word list.
wordList = ("acid", "coal", "come", "head", "shelf", "shine", "earth", "dodge", "damage", "export")

#Picks a word randomly from the word list.
randomWord = random.choice(wordList)

#Function that draws the stages of the hangman based on the life.
def drawHangman(life):
    if life == 6:
        print("  +-----+  \n"
        "  |     |\n"
        "  |\n"
        "  |\n"
        "  |\n"
        "  |\n"
        "---------")
    if life == 5:
        print("  +-----+  \n"
        "  |     |\n"
        "  |     O\n"
        "  |\n"
        "  |\n"
        "  |\n"
        "---------")
    if life == 4:
        print("  +-----+  \n"
        "  |     |\n"
        "  |     O\n"
        "  |     |\n"
        "  |\n"
        "  |\n"
        "---------")
    if life == 3:
        print("  +-----+  \n"
        "  |     |\n"
        "  |     O\n"
        "  |    /|\n"
        "  |\n"
        "  |\n"
        "---------")
    if life == 2:
        print("  +-----+  \n"
        "  |     |\n"
        "  |     O\n"
        "  |    /|\ \n"
        "  |\n"
        "  |\n"
        "---------")
    if life == 1:
        print("  +-----+  \n"
        "  |     |\n"
        "  |     O\n"
        "  |    /|\ \n"
        "  |    / \n"
        "  |\n"
        "---------")
    if life == 0:
        print("  +-----+  \n"
        "  |     |\n"
        "  |     O\n"
        "  |    /|\ \n"
        "  |    / \ \n"
        "  |\n"
        "---------")
        print("Game Over")

#Prints the welcome statement.
print("Welcome to hangman!")

#Draws the hangman before the while loop.
drawHangman(lives)

#Draws the guessed word before the while loop.
for letter in randomWord:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")

#Prints a break in the line.
print("\n")

#While loop runs while lives is not equal to 0.
while lives !=0:

    #Sets the lives to lives.
    lives = lives

    #Asks the user for a letter.
    userInput = input("Please select a letter: ")

    #If the user's letter is in the word, then this statement is printed.
    if userInput in randomWord:
        print(f"The letter {userInput} is in the more one or more times!")
    #If the user's letter is not in the word, one life is subtracted and the statement is printed.
    else:
        lives -= 1
        print(f"The letter {userInput} is not in the word. {lives} more guesses remain.")

    #The user's letter is put into the lettersGuessed.
    lettersGuessed += userInput

    #Sets hasWon to 0.
    hasWon = 0

    #Draws the hangman state.
    drawHangman(lives)

    #If the letter is in lettersGuessed, it is printed onto the screen.
    for letter in randomWord:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            #If any "_" are in lettersGuessed, hasWon is set to 1.
            hasWon += 1

    #Prints a break in the line.
    print("\n")

    #If there are no more "_" in lettersGuessed, the game ends.
    if hasWon == 0:
        print("Congratulations! You guessed the right word!")
        break

    #If the lives equal 0, the game ends and the game breaks out of the loop.
    if lives == 0:
        print(f"You have run out of guesses! The word was {randomWord}.")
        break