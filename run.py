import random 

from termcolor import colored

import sys

print                        ("\033[2;31;43m Welcome to Sports Car Hangman \n")
print  ("\033[1;32;40m _____________________________________________________________________________ \n")
print  ("\033[1;32;40m       .----------.              .----------.              .----------.        \n")
print  ("\033[1;32;40m      /            \            /            \            /            \       \n") 
print  ("\033[1;32;40m    _(.-. _...._ .-.)_        _(.-. _...._ .-.)_        _(.-. _...._ .-.)_     \n")
print  ("\033[1;32;40m   (_)`-' __)(__ `-'(_)      (_)`-' __()__ `-'(_)      (_)`-' __()__ `-'(_)    \n") 
print  ("\033[1;32;40m  (....__|MR_FOGG|__....)   (....__|MR_FOGG|__....)   (....__|MR_FOGG|__....)  \n") 
print  ("\033[1;32;40m   | |    ~~~~~~    | |      | |    ~~~~~~    | |      | |    ~~~~~~    | |    \n") 
print  ("\033[1;32;40m   `-'              `-'      `-'              `-'      `-'              `-'    \n") 
print  ("\033[1;32;40m _____________________________________________________________________________ \n")

wordLibrary = ["ferrari", "lamborghini", "mclaren", "maserati", "bentley", "porsche",]

### Choose a random word
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
    print("\033[1;32;40m        ___________     ___________     ______________    __________    ____________   /n")
  elif(wrong == 1): 
    print("\033[1;32;40m           ______    /n")      
    print("\033[1;32;40m         .' ___  |   /n")
    print("\033[1;32;40m        / .'   \_|   /n")
    print("\033[1;32;40m        | |          /n")
    print("\033[1;32;40m        \ `.___.'\   /n")
    print("\033[1;32;40m         `._____.'   /n")
    print("\033[1;32;40m        ___________  /n")
  elif(wrong == 2): 
    print("\033[1;32;40m           ______         _______     /n")      
    print("\033[1;32;40m         .' ___  |       |_   __ \    /n")
    print("\033[1;32;40m        / .'   \_|        | |__) |    /n")
    print("\033[1;32;40m        | |               |  __ /     /n")
    print("\033[1;32;40m        \ `.___.'\       _| |  \ \_   /n")
    print("\033[1;32;40m         `._____.'      |____| |___|  /n")
    print("\033[1;32;40m        ___________     ___________   /n")
  elif(wrong == 3): 
    print("\033[1;32;40m           ______         _______             __         /n")  
    print("\033[1;32;40m         .' ___  |       |_   __ \           /  \        /n")
    print("\033[1;32;40m        / .'   \_|        | |__) |          / /\ \       /n")
    print("\033[1;32;40m        | |               |  __ /          / ____ \      /n")
    print("\033[1;32;40m        \ `.___.'\       _| |  \ \_      _/ /    \ \_    /n")
    print("\033[1;32;40m         `._____.'      |____| |___|    |____|  |____|   /n")
    print("\033[1;32;40m        ___________     ___________     ______________   /n")
  elif(wrong == 4): 
    print("\033[1;32;40m           ______         _______             __            _______    /n")
    print("\033[1;32;40m         .' ___  |       |_   __ \           /  \          /  ___  |   /n")
    print("\033[1;32;40m        / .'   \_|        | |__) |          / /\ \        |  (__ \_|   /n")
    print("\033[1;32;40m        | |               |  __ /          / ____ \        '.___`-.    /n")
    print("\033[1;32;40m        \ `.___.'\       _| |  \ \_      _/ /    \ \_     |`\____) |   /n")
    print("\033[1;32;40m         `._____.'      |____| |___|    |____|  |____|    |_______.'   /n")
    print("\033[1;32;40m        ___________     ___________     ______________    __________   /n")
  elif(wrong == 5): 
    print("\033[1;32;40m           ______        _______              __            _______      ____  ____    /n")
    print("\033[1;32;40m         .' ___  |      |_   __ \            /  \          /  ___  |    |_   ||   _|   /n")
    print("\033[1;32;40m        / .'   \_|        | |__) |          / /\ \        |  (__ \_|      | |__| |     /n")
    print("\033[1;32;40m        | |               |  __ /          / ____ \        '.___`-.       |  __  |     /n")
    print("\033[1;32;40m        \ `.___.'\       _| |  \ \_      _/ /    \ \_     |`\____) |     _| |  | |_    /n")
    print("\033[1;32;40m         `._____.'      |____| |___|    |____|  |____|    |_______.'    |____||____|   /n")
    print("\033[1;32;40m        ___________     ___________     ______________    __________    ____________   /n")

def printWord(guessedLetters):
  counter=0
  rightLetters=0   
  for char in randomWord:
    if(char in guessedLetters):
      print(randomWord[counter], end=" ")
      rightLetters+=1
    else:
      print(" ", end=" ")
    counter+=1
  return rightLetters 
     
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
while(times_wrong != 5 and latest_letters_right != word_length_to_guess):
  print("\nLetters guessed so far: ")
  for letter in latest_letters_guessed:
    print(letter, end=" ")
  ### Prompt user for input
  letterGuessed = input("\nGuess a letter: ")
  letterGuessed = letterGuessed.lower()

  ### User is right
  if(letterGuessed in randomWord):
    tmp_letter_guess += letterGuessed
    print_hangman(times_wrong)
    print("correct,keep guessing until the word is complete")

    ### Print word
    latest_guess_index+=1
    latest_letters_guessed.append(letterGuessed)
    latest_letters_right = printWord(latest_letters_guessed)
    printLines()

    ### User was wrong 
  else:
    times_wrong+=1
    latest_letters_guessed.append(letterGuessed)
    ### Update the drawing
    print_hangman(times_wrong)
    print("incorrect, keep guessing")
    ### Print Car Make
    latest_letters_right = printWord(latest_letters_guessed)
    printLines()

print("Game is over! Thank you for playing)") 

if len(randomWord) == len(tmp_letter_guess):
  is_win = True

if is_win:

  print("You have won =(%s)" % randomWord)
  print("Disclaimer The above statement is not true")

else:
  print("Sorry that was a complete car crash, better luck next time")







