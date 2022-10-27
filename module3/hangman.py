import random

lives = 6
wordList = ("acid", "coal", "come", "head", "shelf", "shine", "earth", "dodge", "damage", "export")
randomWord = random.choice(wordList)

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

print("Welcome to hangman!")

drawHangman(lives)

while lives !=0:
    lives = lives
    lettersGuessed = ""

    print(randomWord)

    userInput = input("Please select a letter: ")

    if userInput in randomWord:
        print(f"The letter {userInput} is in the more one or more times!")
    else:
        lives -= 1
        print(f"The letter {userInput} is not in the word. {lives} more guesses remain.")

    lettersGuessed += userInput
    hasWon = 0

    for letter in randomWord:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            hasWon += 1

    print("\n")

    drawHangman(lives)

    if hasWon == 0:
        print("Congradulations! You guessed the right word!")
        break

    if lives == 0:
        print(f"You have run out of guesses! The word was {randomWord}.")
        break