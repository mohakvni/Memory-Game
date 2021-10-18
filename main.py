import random
import time
player=str(input("Enter Your name:"))
print("Hi",player)
x = "▫️️"
answerGrid = [['MANGO','APPLE','MANDARIN','BANANA','APPLE',"KIWI"],
             ['PAPAYA','PAPAYA','STRAWBERRY','JACKFRUIT','AVACADO','ORANGE'],
             ['CHERRY','CHERRY','TOMATO','KIWI', 'MANDARIN','STRAWBERRY'],
             ['POMEGRANATE','BANANA','LEMON','MANGO','ORANGE','JACKFRUIT'],
             ['COCONUT','AVACADO','APRICOT','WATERMELON','TOMATO','GRAPES'],
             ['COCONUT','LEMON','POMEGRANATE','GRAPES','APRICOT','WATERMELON']]

blankGrid = [[x,x,x,x,x,x],
             [x,x,x,x,x,x],
             [x,x,x,x,x,x],
             [x,x,x,x,x,x],
             [x,x,x,x,x,x],
             [x,x,x,x,x,x]]
guesses = 0
guess1 = "  "
guess2 = "  "
option = 0
emptySpaces = 0
correctGuesses = []
rowsAvailable = ["a", "b", "c", "d", "e", "f"]
colsAvailable = ["1", "2", "3", "4", "5", "6"]
cont = 0

while option not in [1, 2]: 
  option = 2
  answer = str(input("Would you like to play a memory game (y/n)?"))
  if answer in ["Y", "y", "Yes", "yes"]:
    print ("")
    print("Welcome to the Memory Game!")
    print ("The program will display a grid of cards flipped to the back and the user must choose the position (in the form of a letter followed by a number) of two cards that they wish to flip over. E.g:A1,B5,C6.The highest letter is f and the highest number is 6. The deck is composed of matching pairs of letters and the goal of the game is to find all the matching pairs. If the user guesses two cards that are not identical, the program will flip the cards back and the user will try again. The game runs until the user guesses all the matching pairs and wins the game.")
    print ("")
    answer = str(input("Would you still like to play (yes/no)?"))
    if answer in ["Y", "y", "Yes", "yes"]:
      option = 1

def printblankGrid():
  loops = 0
  while loops < 6:
    print (*blankGrid[loops])
    loops += 1

def startGame():
  while True:
    guess1 = str.lower(input("Enter the row and the column of your first guess:"))
    
    
    if len(guess1) == 2 and guess1[0] in rowsAvailable and guess1[1] in colsAvailable:
      row1 = ord(guess1[0]) - 97
      col1 = ord(guess1[1]) - 49
      if answerGrid[row1][col1] in correctGuesses:
        print ("That is not a valid guess. Try again")
      else:
        blankGrid[row1][col1] = answerGrid[row1][col1]
        break
    else:
      print ("That is not a valid guess. Try again")
  print ("")
  printblankGrid()
  print ("")

  while True:
    guess2 = str.lower(input("Enter the row and the column of your second guess :"))
    lengthguess2 = len(guess2)
    if guess1 == guess2:
      print("That is not a valid guess. Please try again")
    elif lengthguess2 == 2 and guess2[0] in rowsAvailable and guess2[1] in colsAvailable:
      row2 = ord(guess2[0]) - 97
      col2 = ord(guess2[1]) - 49
      if answerGrid[row2][col2] in correctGuesses:
        print ("That is not a valid guess. Please try again")
      else:
        blankGrid[row2][col2] = answerGrid[row2][col2]
        break
    else:
      print ("That is not a valid guess. Please try again")
  print ("")
  printblankGrid()
  print ("")

  if answerGrid[row1][col1] == answerGrid[row2][col2]:
    print ("You have found a match.")
    print ("")
    correctGuesses.append(answerGrid[row1][col1])
    time.sleep(1)
  else:
    print ("Sorry, that is not a match.")
    print ("")
    time.sleep(1)
    blankGrid[row1][col1] = x
    blankGrid[row2][col2] = x

while True:
  if answerGrid == blankGrid:
    print ("You have won the game. Congratulations!")
    print ("")
    print ("It took you", (guesses), "guesses!")
    option = 2
  elif cont == 1:
    while True:
      quit = str(input("Would you like to continue (yes/no)?"))
      if quit in ["Y", "y", "Yes", "yes"]:
        option = 1
        break
      elif quit in ["N", "n", "No", "no"]:
        option = 2
        break
      
  guesses = guesses + 1
  cont = 1
  if option == 1:
    printblankGrid()
    print ("")
    startGame()
  elif option == 2:
    print ("Thank you for playing!!!")
    break
