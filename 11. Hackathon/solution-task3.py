input = "A Y \nB X \nC Z"

convert = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

beats = {
    #rock
    "A": "C",
    #paper
    "B": "A",
    #scissors
    "C": "A",
}

score = {
    "A": 1,
    "B": 2,
    "C": 3,
}

for round in input.split("\n"):
    opp = round[0]
    me = round[2]
    me = convert[me]
    
    count = 0
    count += score[me]

    if (opp in beats[me]): count += 6
    elif (opp == me): count += 3