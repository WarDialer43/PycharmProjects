#challenge 3
import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
    game_count  = 0
    player_wins =0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
        
        playerchoice = input(f"\n{name}, please enter... \n1 Rock,\n2 Paper, or \n3 Scissors\n\n")
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter either 1, 2, or 3. !")
            return play_rps()

        player = int(playerchoice)


        computerchoice = (random.choice("123"))

        computer = int(computerchoice)

        print(f"\n{name }, you chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

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
            return play_rps()
        else:
            print("\n👋👋👋")
            print("Thanks for stopping by!\n")
            sys.exit(f"have a nice day {name} !😁")

    return play_rps  

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

    rock_paper_scissors = rps(args.name)

    rock_paper_scissors()

