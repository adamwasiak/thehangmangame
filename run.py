import random

# Welcome message to the player and player name input
print("Hangman game by Adam Wasiak, welcome!")
name = input("Enter your name please:")
print("Hello " + name + "," + " enjoy the game!")
print("Are you ready?, let's start")

# Add dictonary for words selection
dictionary = ["year", "dog", "name", "twenty", "car", "february",
              "window", "computer", "coffee", "hawk", "shopping", "bat",
              "lane", "tower", "crystal", "gold", "silver", "cat",
              "impossible", "nice", "game", "sharp", "books", "radio",
              "speed", "slow", "nothing", "history", "mountain", "lake"]


def hangman():
    """
    Hangman logic function
    """
    global count
    global display
    global word
    global guessed
    global play_game
    limit = 5
    guess = input("This is the selected word:" + display + "Take a guess:\n")
    guess = guess.strip()
    print(word)
    if len(guess.strip()) == 0 and len(guess) != 1:
        print("Incorrect Input, please ensure that you use a letter. \n")
        hangman()
    elif guess in guessed:
        print("You have already selected this letter.\n")
        hangman()
    elif guess in word:
        guessed.append(guess)
        display = ""
        for i in range(len(word)):
            if (word[i] in guessed):
                display += word[i]
            else:
                display += "_"
            display += " "

        if display.replace(" ", "") == word:
            print("Nice one, you guessed the word")
            replay()

        hangman()
         
    else:
        count += 1

        if count == 1:
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Incorrect guess." + str(limit - count) + " guesses left\n")

        elif count == 2:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Incorrect guess." + str(limit - count) + " guesses left\n")
        elif count == 3:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Incorrect guess." + str(limit - count) + " guesses left\n")
        elif count == 4:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Incorrect guess." + str(limit - count) + " guess left\n")
        elif count == 5:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("You got it wrong. You lost\n")
            print("The word is:", guessed, word)
            replay()

        if count != limit:
            hangman()


def replay():
    """
    Function to replay the game again
    """
    global play_game
    play_game = input("Would you like to play again?Yes=y, No=n\n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game = input("Would you like to play again?Yes=y, No=n\n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("See you soon!")
        exit()


def main():
    """
    main function of the game including all parameters
    """
    global count
    global display
    global word
    global guessed
    global length
    global play_game
    word = random.choice(dictionary)
    length = len(word)
    count = 0
    display = '_ ' * length
    guessed = []
    play_game = ""

main()

hangman()
