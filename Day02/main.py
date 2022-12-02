"""
Advent Of Code - 2022
Day 1

Part 1
------
The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.

Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).


"""
guide = []
with open("./input.txt", 'r') as f:
    guide = f.readlines()

