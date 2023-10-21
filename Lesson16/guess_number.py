# Creat a new game called Guess my number.

# Take what was learned in the RPS with the argpass module and apply it by creating a new game.

# Will accept a name and on passing the name you apply.

# then launch with the question name, guess what number I amthinking of .... 1, 2, 3, or 4

# the mechanics much like that of RPS feel free to be creative in my judgement !

import sys
import random
from enum import Enum
import numbers


def gn(name='PlayerOne'):
    game_count  = 0
    player_wins =0
    python_wins = 0

    def play_gn():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class GN(Enum):
            One = 1
            Two = 2
            Three = 3
        
        playerchoice = input(f"\n{name}, please enter... \n1 One,\n2 Two, or \n3 Three\n\n")
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter either 1, 2, or 3. !")
            return play_gn()

        player = int(playerchoice)


        computerchoice = (random.choice("123"))

        computer = int(computerchoice)

        print(f"\n{name }, you chose {str(GN(player)).replace('GN.', '').title()}.")
        print(f"Python chose {str(GN(computer)).replace('GN.', '').title()}.\n")

        def decide_winner(play, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"㊗️ {name}, you wins !"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"㊗️ {name}, you wins !"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"㊗️ {name}, you wins !" 
            elif player == computer:
                return"🤨Draw !"
            else:
                python_wins += 1
                return"🐍Python Wins !\nSorry, {name}..😞 "

        game_result = decide_winner("player", computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        
# attempt tpcalculate percentages ############################################################################
# def percentage(part, whole):
#   return 100 * float(part)/float(whole)

# def percentage(part, whole):
#   Percentage = 100 * float(part)/float(whole)
#   return str(Percentage) + “%”

#   def percentage(percent, whole):
#   return (percent * whole) / 100.0



def percent(player, computer):
        return 100 * float(player_wins) / float(python_wins)
 
        return 0



########################################################################################################

        print(f"\nGame Count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

        print(f"\n play again,{name}?")

        while True:
            playagain = input("\n Play again ? \nY for yes or \nQ for quit \n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_gn()
        else:
            print("\n👋👋👋")
            print("Thanks for stopping by!\n")
            sys.exit(f"have a nice day {name} !😁")

    return play_gn  

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experiemce."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    One_Two_Three = gn(args.name)

    One_Two_Three()

