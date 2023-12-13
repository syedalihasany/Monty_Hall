import random
import math


def restricted_doors(doors, stayer_choice):
    new_doors = []
    for item in [0,1,2]:
        if item != stayer_choice:
            new_doors.append(doors[item])
    return new_doors

def monty_peek(new_doors):
    if new_doors[0] == "G":
        return new_doors[1]
    elif new_doors[1] == "G":
        return new_doors[0] 

def sim(num_sim):

    # prize list represents the three doors
    # 'G' represents a goat and 'C' represents a car
    # we will shuffle this for each game
    doors = ["G", "G", "C"]

    # variables to count the switcher wins and stayers wins
    stayer_wins = 0
    switcher_wins = 0

    for i in range(1, num_sim + 1):
        random.shuffle(doors)                   # shuffling the list for each game
        stayer_choice = random.randint(0, 2)    # the first player (aka stayer) chooses the door number 
                                                # and they will stick to it for the rest of the game
        
        
        stayer_gets = doors[stayer_choice]      # this is the prize behind the door 
                                                # number selected by the stayer

        new_doors = restricted_doors(doors, stayer_choice)  # we remove their choice of door and subsequently the prize behind it

        switcher_gets = monty_peek(new_doors)       # switcher_gets is the prize behind the door that is left 
                                                    # after Monty opens one of the doors containing a goat
        if switcher_gets == "C":
            switcher_wins += 1
        elif stayer_gets == "C":
            stayer_wins += 1

    return stayer_wins, switcher_wins

# edit this to perform any number of simulations
num_sim = 1000

# calling the simulator function to do the simulations
stayer_wins, switcher_wins = sim(num_sim)

print(f'Number of games/simulations played: {num_sim}')
print(f'Stayer wins:{stayer_wins}')
print(f'Switcher wins:{switcher_wins}')
print(f'Stayer win ratio: {float(stayer_wins/num_sim)}')
print(f'Switcher win ratio: {float(switcher_wins/num_sim)}')
