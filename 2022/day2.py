dependencies = {"A": "C", "B": "A", "C": "B"} # key beats value
shape_scores = {"A": 1, "B": 2, "C": 3} 
assigment = {"X": "A", "Y": "B", "Z":"C"} 

score_total = 0
for line in open("day2.input"):
    opponent, player = line.strip().split()
    player = assigment[player]
    score_round = shape_scores[player]
    if dependencies[player] == opponent: # player wins
        score_round += 6
    elif player == opponent:
        score_round += 3
    score_total += score_round

print(f"part 1: {score_total}")
        
score_total = 0
for line in open("day2.input"):
    opponent, outcome = line.strip().split()
    if outcome == "X": # player should lose
        player = dependencies[opponent]
        score_total += shape_scores[player]
    elif outcome == "Y": # player should draw
        score_total += 3 + shape_scores[opponent]
    else: # player should win
        player = [k for k in dependencies.keys() if dependencies[k] == opponent][0]
        score_total += 6 + shape_scores[player]

print(f"part 2: {score_total}")
