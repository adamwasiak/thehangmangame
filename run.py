import random

# Welcome message to the player and player name input
print("Hangman game by Adam Wasiak, welcome!")
name = input("Enter your name please:")
print("Hello " + name + "," + " enjoy the game!")
print("Are you ready?, let's start")

#Add dictonary for words selection
dictonary= ["year","dog","name","twenty","car","february",
    "window","computer","coffee","hawk","shopping","bat",
    "lane","tower","crystal","gold","silver","cat",
    "impossible","nice","game","sharp","books","radio",
    "speed","slow","nothing","history","mountain","lake"]


def hangman():
    """ 
    Hangman logic function
    """ 
    
    limit = 5
    guess = input("This is the selected word:" + display + "Take a guess:\n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) == "2" or guess == "9":
        print("Incorrect Input, please use letter instead\n")
        

def replay():    

def main():




