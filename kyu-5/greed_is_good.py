# https://www.codewars.com/kata/5270d0d18625160ada0000e4
# Greed is Good

# First Implementation 01/10/2021
def score(dice):
    # initialize the six dice's faces as 0
    valDice={
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
    }
    
    # set the amount of time a face has been rolled
    for number in dice:
        valDice[str(number)]+=1

    # initialize the total as 0
    total=0
    
    # for every face of the dice
    for face in valDice:
        # while the amount of times a face has been rolled is more than 0
        # and the value of the face is either 1 or 5
        while valDice[face] > 0 and (face == "1" or face == "5"):
            # if said face has been rolled 3 or more times
            if valDice[face] >= 3:
                # add 1000 to the total if the face is 1
                # or add 500 if the face is 5
                total += 1000 if face == "1" else 500
                # remove 3 from the amount of times that the face has been rolled 
                valDice[face]-=3
            # if the face has been rolled less than 3 times
            else:
                # add 100 to the total if the face is 100
                # or add 50 if the face is 5
                total += 100 if face == "1" else 50
                # remove 1 from the amount of times that the face has been rolled 
                valDice[face]-=1
                
        # if the face is not 1 or 5 and the amount of times it has been rolled is greater than 3
        if valDice[face] >= 3:
            # add the value of the face multiplied by 100 to the total
            total+=int(face)*100
    
    return total

# --------------------

# Second Implementation 25/10/2021
def score(dice):
    # join lines 6 to 18 in a single statement
    valDice={str(index+1): dice.count(index+1) for index in range(6)}
    total=0
    
    for value in valDice:
        while valDice[value] > 0 and (value == "1" or value == "5"):
            if valDice[value] >= 3:
                total += 1000 if value == "1" else 500
                valDice[value]-=3
            else:
                total += 100 if value == "1" else 50
                valDice[value]-=1
                
        if valDice[value] >= 3:
            total+=int(value)*100
    
    return total
