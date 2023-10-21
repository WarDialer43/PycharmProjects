import sys
import random
from enum import Enum


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
    
    
    playerchoice = input("\nEnter ... \n1 Rock,\n2 Paper, or \n3 Scissors\n\n")
    if playerchoice not in ["1", "2", "3"]:
        print("Please enter either 1, 2, or 3. !")
        return play_rps()

    player = int(playerchoice)


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
    
    print("\n play again ?")

    while True:
        playagain = input("\n Play again ? \nY for yes or \nQ for quit \n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n👋👋👋")
        print("Thanks for stopping by!\n")
        sys.exit("have a nice day 😁")  

play_rps()
