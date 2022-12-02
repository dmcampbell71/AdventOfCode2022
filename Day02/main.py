"""
Advent Of Code - 2022
Day 2
"""


def score(opponent: str, me: str) -> int:
    """Figures score based upon part 1"""
    points = {'X': 1, 'Y': 2, 'Z': 3}
    matrix = {'X': {'C': 6, 'A': 3, 'B': 0},
              'Y': {'A': 6, 'B': 3, 'C': 0},
              'Z': {'B': 6, 'C': 3, 'A': 0}
              }
    sum = matrix[me][opponent] + points[me]
    return sum


def score2(opponent: str, state: str) -> int:
    """Figures score based upon part 2"""
    points = {'X': 0, 'Y': 3, 'Z': 6}
    matrix = {'A': {'X': 3, 'Y': 1, 'Z': 2},
              'B': {'X': 1, 'Y': 2, 'Z': 3},
              'C': {'X': 2, 'Y': 3, 'Z': 1}
              }
    sum = matrix[opponent][state] + points[state]
    return sum


guide = []
with open("./input.txt", 'r') as f:
    guide = f.readlines()

total1 = 0
total2 = 0
for line in guide:
    line = line.rsplit()
    (col1, col2) = line
    points = score(col1, col2)
    total1 += points
    points = score2(col1, col2)
    total2 += points
print(f"You originally scored a total of {total1} points.")
print(f"Your updated score total was {total2} points.")
