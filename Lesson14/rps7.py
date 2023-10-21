import sys
import random
from enum import Enum

def rps():
    game_count  = 0
    player_wins =0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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

        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(play, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return"㊗️Player wins !"
            elif player == 2 and computer == 1:
                player_wins += 1
                return"㊗️Player wins !"
            elif player == 3 and computer == 2:
                player_wins += 1
                return"㊗️Player wins !" 
            elif player == computer:
                return"🤨Draw !"
            else:
                python_wins += 1
                return"🐍Python Wins !"

        game_result = decide_winner("player", computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame Count: {str(game_count)}")
        print(f"\nPlayer wins: {str(player_wins)}")
        print(f"\nPython wins: {str(python_wins)}")

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

    return play_rps  

rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()

