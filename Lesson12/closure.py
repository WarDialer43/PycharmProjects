#Closure os a Function having access to the Scope of its parent Function after 
#  the parent Function has returned

def parent_function(person):
    coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) +  " coins left. " )
        elif coins == 1:
            print("\n" + person + " has " + str(coins) +  " coin left. " )
        else:
            print("\n" + person + " is out of coins ! " )

        
    return play_game

rupert = parent_function("Rupert")
jane =parent_function("Jane")

rupert()
rupert()
rupert()
jane()

