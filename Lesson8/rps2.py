import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
playagain = True

while playagain:
   
    playerchoice = input("\nEnter ... \n1 Rock,\n2 Paper, or \n3 Scissors\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("Please enter either 1, 2, or 3. !")

    computerchoice = (random.choice("123"))

    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")

    if player == 1 and computer == 3:
        print("㊗️Player wins !")
    elif player == 2 and computer == 1:
        print("㊗️Player wins !")
    elif player == 3 and computer == 2:
        print("㊗️Player wins !") 
    elif player == computer:
        print("🤨Draw !")
    else:
        print("🐍Python Wins !")

    playagain = input("\n Play again ? \nY for yes or \nQ for quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n👋👋👋")
        print("Thanks for stopping by!\n")
        
        playagain = False

    sys.exit("have a nice day 😁")


