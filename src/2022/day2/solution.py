"""
A(X) - Rock
B(Y) - Paper
C(Z) - Scissors
"""

import aocd

mapping = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}
shape_points = {
    "A": 1,
    "B": 2,
    "C": 3,
}
defeats = {
    "A": "C",
    "B": "A",
    "C": "B",
}

input = [line.split(" ") for line in aocd.get_data(year=2022, day=2).splitlines()]

points = 0

for opponent_shape, player_shape in input:
    points += shape_points[mapping[player_shape]]
    if defeats[mapping[player_shape]] == opponent_shape:
        points += 6
    if mapping[player_shape] == opponent_shape:
        points += 3

print(points)  # part 1


"""
X - lose
Y - draw
Z - win
"""

loses = {
    "C": "A",
    "A": "B",
    "B": "C",
}

points = 0

for opponent_shape, expected_result in input:
    if expected_result == "X":
        points += shape_points[defeats[opponent_shape]]
    if expected_result == "Y":
        points += shape_points[opponent_shape] + 3
    if expected_result == "Z":
        points += shape_points[loses[opponent_shape]] + 6

print(points)  # part 2
