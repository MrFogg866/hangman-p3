import random 

print                        ("Welcome to Sports Car Hangman")
print  ("_____________________________________________________________________________")
print  ("      .----------.              .----------.              .----------.       ")
print  ("     /            \            /            \            /            \      ") 
print  ("   _(.-. _...._ .-.)_        _(.-. _...._ .-.)_        _(.-. _...._ .-.)_    ")
print  ("  (_)`-' __)(__ `-'(_)      (_)`-' __()__ `-'(_)      (_)`-' __()__ `-'(_)   ") 
print  (" (....__|MR_FOGG|__....)   (....__|MR_FOGG|__....)   (....__|MR_FOGG|__....) ") 
print  ("  | |    ~~~~~~    | |      | |    ~~~~~~    | |      | |    ~~~~~~    | |   ") 
print  ("  `-'              `-'      `-'              `-'      `-'              `-'   ") 
print  ("_____________________________________________________________________________")

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
    print("    ")
    print("    ")
    print("      __________________  __________________  __________________  _________________   __________________    ")
  elif(wrong == 1): 
    print("      .------------------.  ")
    print("      | .--------------. |  ")
    print("      | |     ______   | |  ")
    print("      | |   .' ___  |  | |  ")
    print("      | |  / .'   \_|  | |  ")
    print("      | |  | |         | |  ")
    print("      | |  \ `.___.'\  | |  ")
    print("      | |   `._____.'  | |  ")
    print("      | |              | |  ")
    print("      '----------------' '  ")
    print("      __________________  __________________  __________________  _________________   __________________    ")

  elif(wrong == 2): 
     print("       .--------------.    .--------------.      ")
    print("        |     ______   |    |  _______     |      ")
    print("        |   .' ___  |  |    | |_   __ \    |      ")
    print("        |  / .'   \_|  |    |   | |__) |   |      ")
    print("        |  | |         |    |   |  __ /    |      ")
    print("        |  \ `.___.'\  |    |  _| |  \ \_  |      ")
    print("        |   `._____.'  |    | |____| |___| |      ")
    print("        |              |    |              |      ")
    print("        '--------------'    '--------------'      ")
    print("        ________________    ________________    ________________    ________________    ________________  ")

  elif(wrong == 3): 
    print("        .--------------.    .--------------.    .--------------.     ")
    print("        |     ______   |    |  _______     |    |      __      |     ")
    print("        |   .' ___  |  |    | |_   __ \    |    |     /  \     |     ")
    print("        |  / .'   \_|  |    |   | |__) |   |    |    / /\ \    |     ")
    print("        |  | |         |    |   |  __ /    |    |   / ____ \   |     ")
    print("        |  \ `.___.'\  |    |  _| |  \ \_  |    | _/ /    \ \_ |     ")
    print("        |   `._____.'  |    | |____| |___| |    ||____|  |____||     ")
    print("        |              |    |              |    |              |     ")
    print("        '--------------'    '--------------'    '--------------'     ")
    print("        ________________    ________________    ________________    ________________    ________________  ")

  elif(wrong == 4): 
    print("        .--------------.    .--------------.    .--------------.    .--------------.      ")
    print("        |     ______   |    |  _______     |    |      __      |    |    _______   |      ")
    print("        |   .' ___  |  |    | |_   __ \    |    |     /  \     |    |   /  ___  |  |      ")
    print("        |  / .'   \_|  |    |   | |__) |   |    |    / /\ \    |    |  |  (__ \_|  |      ")
    print("        |  | |         |    |   |  __ /    |    |   / ____ \   |    |   '.___`-.   |      ")
    print("        |  \ `.___.'\  |    |  _| |  \ \_  |    | _/ /    \ \_ |    |  |`\____) |  |      ")
    print("        |   `._____.'  |    | |____| |___| |    ||____|  |____||    |  |_______.'  |      ")
    print("        |              |    |              |    |              |    |              |      ")
    print("        '--------------'    '--------------'    '--------------'    '--------------'      ")
    print("        ________________    ________________    ________________    ________________    ________________ ")
  elif(wrong == 5): 
    
    print("        .--------------.    .--------------.    .--------------.    .--------------.    .--------------.    ")
    print("        |     ______   |    |  _______     |    |      __      |    |    _______   |    |  ____  ____  |    ")
    print("        |   .' ___  |  |    | |_   __ \    |    |     /  \     |    |   /  ___  |  |    | |_   ||   _| |    ")
    print("        |  / .'   \_|  |    |   | |__) |   |    |    / /\ \    |    |  |  (__ \_|  |    |   | |__| |   |    ")
    print("        |  | |         |    |   |  __ /    |    |   / ____ \   |    |   '.___`-.   |    |   |  __  |   |    ")
    print("        |  \ `.___.'\  |    |  _| |  \ \_  |    | _/ /    \ \_ |    |  |`\____) |  |    |  _| |  | |_  |    ")
    print("        |   `._____.'  |    | |____| |___| |    ||____|  |____||    |  |_______.'  |    | |____||____| |    ")
    print("        |              |    |              |    |              |    |              |    |              |    ")
    print("        '--------------'    '--------------'    '--------------'    '--------------'    '--------------'    ")
    print("        ________________    ________________    ________________    ________________    ________________    ")

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


length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
latest_guess_index = 0
latest_letters_guessed = []
latest_letters_right = 0

while(amount_of_times_wrong != 6 and latest_letters_right != length_of_word_to_guess):
  print("\nLetters guessed so far: ")
  for letter in latest_letters_guessed:
    print(letter, end=" ")
  ### Prompt user for input
  letterGuessed = input("\nGuess a letter: ")
  ### User is right
  if(randomWord[latest_guess_index] == letterGuessed):
    print_hangman(amount_of_times_wrong)
    ### Print word
    latest_guess_index+=1
    latest_letters_guessed.append(letterGuessed)
    latest_letters_right = printWord(latest_letters_guessed)
    printLines()






 