lives = 6

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

while lives !=0:
    drawHangman(lives)
    input("Welcome to hangman! Please select a letter.")
    break