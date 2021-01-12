import numpy as np
import pandas as pd
import time

baseballTable = pd.read_csv("baseballSimulation.csv", usecols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
baseballDF    = pd.DataFrame(baseballTable)

arrayOfDiceRolls          = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
probabilitiesOfDiceRolls  = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
eventArray                = pd.DataFrame(0, index = np.arange(24) + 1, # https://stackoverflow.com/a/22964673
                            columns = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])# https://stackoverflow.com/a/19483025

def collectEvents(stateReached, diceRoll):
    stateReachedIndex = stateReached - 1
    diceRollIndex     = diceRoll
    eventArray.iloc[int(stateReachedIndex)][diceRollIndex] += 1 # Increment cell by 1 each time it's reached

def playOneGame(verboseBoolean, extraDetailsBoolean):
    startingConfiguration = baseballDF.iloc[0]
    startingState         = startingConfiguration["Game State"] # Always start at State 1
    currentConfiguration  = startingConfiguration
    currentState          = startingState
    killState             = 25 # State 25 corresponds to 3 outs = inning over
    
    if extraDetailsBoolean:
        print(f'The starting configuration is {startingConfiguration}')
        print(f'The starting state is therefore {int(startingState)}.')
        
    while int(currentState) <= killState:
        diceRoll             = np.random.choice(                   # Roll the dice:
                             arrayOfDiceRolls,                     # Dice roll outcomes with weighted probabilities
                             1,                                    # Only want one item
                             p = probabilitiesOfDiceRolls)[0]      # Array of probs., want 1 item = [0]
        newStateIndex        = diceRoll - 1                        # Get correct index by shifting by 1
        newState             = currentConfiguration[newStateIndex] # Find the new game state
        stateDifference      = newState - currentState             # State diff. for logic purposes
        index                = int(newState) - 1                   # state float -> int. & find index for next config.
        newConfiguration     = baseballDF.iloc[index]              # Find the new state configuration
        currentConfiguration = newConfiguration                    # Set new config. as current config
        if currentState == 1:                                   # if first state, dice roll needs to be recorded
            collectEvents(currentState, diceRoll)               # write to the output table
        if currentState != 1 and currentState < 25:             # if not in the first state, do regular stuff
            collectEvents(currentState, diceRoll)               # write to the output table
        currentState         = newState                            # Set new state as current state
        
        # Debugging purposes only:
        if verboseBoolean:
            print(f'The dice rolled a {diceRoll}')
            print(f'This roll pulls out state #{int(newState)}.')
        if extraDetailsBoolean:
            print(f'That state corresponds to a new configuration of {newConfiguration}.')
        if currentState >= 25:
            if verboseBoolean:
                print("State 25 reached... Game over.")
            break

def simulateInnings(numberOfInnings, verboseBoolean, extraVerboseBoolean):
    startTime = time.time()
    if verboseBoolean:
        inningDetailsBoolean = True
    else:
        inningDetailsBoolean = False
    if extraVerboseBoolean:
        inningProgramDetailsBoolean = True
    else:
        inningProgramDetailsBoolean = False        
    iterator = 0 # Prime the iterator
    while iterator < numberOfInnings:
            
        playOneGame(inningDetailsBoolean, inningProgramDetailsBoolean)
        iterator += 1
        if iterator % 50000 == 0:
            print('Ran inning #{} in {} minutes'.format(iterator + 1, round(((time.time() - startTime) / 60), 2)))

number = int(input("How many innings do we want to run:"))
simulateInnings(number, False, False) if isinstance(number, int) else print("ERROR: Number of innings must be of integer type.")

# some extra stuff if you want it - display(eventArray)
# some extra stuff if you want it - eventArray.to_csv("So_CSV.csv")
# some extra stuff if you want it - eventArray.to_excel("So_Simulation.xlsx", sheet_name = "Much-Wow!")
