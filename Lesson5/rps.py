import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")

playerchoice = input("Enter ... \n1 Rock,\n2 Paper, or \n3 Scissors\n\n")


player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("Please enter either 1, 2, or 3. !")


computerchoice = (random.choice("123"))

computer = int(computerchoice)

print("")

print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")

print("")


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

