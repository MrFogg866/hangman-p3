import random

print("\033[1;32;48m Welcome to Sports Car Hangman")
print("There are 6 Car Manufacturers to guess\
enter one letter at a time\
you have 5 attempts before you will crash\
guess the letters correctly and win a car")
print("___________________________________________________________________________")
print("     .----------.              .----------.              .----------.      ")
print("    /            \            /            \            /            \     ")
print("  _(.-. _...._ .-.)_        _(.-. _...._ .-.)_        _(.-. _...._ .-.)_   ")
print(" (_)`-' __)(__ `-'(_)      (_)`-' __( )__ `-'(_)      (_)`-' __()__ `-'(_) ")
print("(....__|MR_FOGG|__....)   (....__|MR_FOGG|__....)   (....__|MR_FOGG|__....)")
print(" | |    ~~~~~~    | |      | |    ~~~~~~    | |      | |    ~~~~~~    | |  ")
print(" `-'              `-'      `-'               `-'      `-'              `-' ")
print("___________________________________________________________________________")

wordLibrary = ["ferrari", "lamborghini", "mclaren",
               "maserati", "bentley", "porsche", ]

# Choose a random word
randomWord = random.choice(wordLibrary)

for x in randomWord:
    print("_", end=" ")  

def print_hangman(wrong):
  if(wrong == 0):
    print("    ")
    print("    ")
    print("    ")
    print("    ")
    print("    ")
    print("    ")
    print("    ")
    print("    ")
    print("    ")
    print(" __________    ____________  ______________   __________  ____________ ")
  elif(wrong == 1):
    print("    ______ ")
    print("  .' ___  | ")
    print(" / .'   \_|")
    print(" | |       ")
    print(" \ `.___.'\ ")
    print("  `._____.'")
    print(" __________    ____________  ______________   __________  ____________ ")

  elif(wrong == 2):
    print("    ______      _______   ")
    print("  .' ___  |    |_   __ \  ")
    print(" / .'   \_|      | |__) | ")
    print(" | |             |  __ /  ")
    print(" \ `.___.'\     _| |  \ \_")
    print("  `._____.'    |____| |___|")
    print(" __________    ____________  ______________   __________  ____________ ")
  elif(wrong == 3):
    print("    ______      _______            __     ")
    print("  .' ___  |    |_   __ \          /  \    ")
    print(" / .'   \_|      | |__) |        / /\ \   ")
    print(" | |             |  __ /        / ____ \  ")
    print(" \ `.___.'\     _| |  \ \_    _/ /    \ \_ ")
    print("  `._____.'    |____| |___|  |____|  |____|")
    print(" __________    ____________  ______________   __________  ____________ ")
  elif(wrong == 4):
    print("    ______      _______            __           _______  ")
    print("  .' ___  |    |_   __ \          /  \         /  ___  | ")
    print(" / .'   \_|      | |__) |        / /\ \       |  (__ \_| ")
    print(" | |             |  __ /        / ____ \       '.___`-.  ")
    print(" \ `.___.'\     _| |  \ \_    _/ /    \ \_    |`\____) | ")
    print("  `._____.'    |____| |___|  |____|  |____|   |_______.' ")
    print(" __________    ____________  ______________   __________  ____________ ")
  elif(wrong == 5): 
    print("    ______      _______            __           _______    ____  ____  ")
    print("  .' ___  |    |_   __ \          /  \         /  ___  |  |_   ||   _| ")
    print(" / .'   \_|      | |__) |        / /\ \       |  (__ \_|    | |__| |   ")
    print(" | |             |  __ /        / ____ \       '.___`-.     |  __  |   ")
    print(" \ `.___.'\     _| |  \ \_    _/ /    \ \_    |`\____) |   _| |  | |_  ")
    print("  `._____.'    |____| |___|  |____|  |____|   |_______.'  |____||____| ")
    print(" __________    ____________  ______________   __________  ____________ ")

def printWord(guessedLetters):
    tmp_guessedLetters = []
    counter = 0
    rightLetters = 0
    for char in randomWord:
        if (char in guessedLetters):
            print(randomWord[counter], end=" ")
            tmp_guessedLetters.append(char)
            rightLetters += 1
        else:
            print(" ", end=" ")
        counter += 1
    return rightLetters, tmp_guessedLetters


def printLines():
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")


word_length_to_guess = len(randomWord)
times_wrong = 0
latest_guess_index = 0
latest_letters_guessed = []
latest_letters_right = 0

is_win = False
tmp_letter_guess = ''
while (times_wrong != 5 and latest_letters_right != word_length_to_guess):
    print()
    print("gusess Number: ", randomWord)
    print("\nLetters guessed so far: ")

    for letter in latest_letters_guessed:
        print(letter, end=" ")

    ### Prompt user for input
    letterGuessed = input("\nGuess a letter: ")
    letterGuessed = letterGuessed.lower()

    ### User is right
    if (letterGuessed in randomWord):
        tmp_letter_guess += letterGuessed
        print_hangman(times_wrong)
        print("correct, keep guessing until the word is complete")

        ### Print word
        latest_guess_index += 1
        latest_letters_guessed.append(letterGuessed)
        latest_letters_right, latest_letters_guessed = printWord(latest_letters_guessed)
        printLines()

        ### User was wrong
    else:
        times_wrong += 1
        latest_letters_guessed.append(letterGuessed)

        ### Update the drawing
        print_hangman(times_wrong)
        print("incorrect, keep guessing")

        ### Print Car Make
        latest_letters_right, latest_letters_guessed = printWord(latest_letters_guessed)
        printLines()

print("Game is over! Thank you for playing)")

if len(randomWord) == len(latest_letters_guessed):
    is_win = True

if is_win:

    print("You have won =(%s)" % randomWord)
    print("Disclaimer The above statement is not true")

else:
    print("Sorry that was a complete car crash, better luck next time")











