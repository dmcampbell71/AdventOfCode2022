"""
Advent of Code - 2022
Day 5

Initial stacks:
[F]         [L]     [M]
[T]     [H] [V] [G] [V]
[N]     [T] [D] [R] [N]     [D]
[Z]     [B] [C] [P] [B] [R] [Z]
[M]     [J] [N] [M] [F] [M] [V] [H]
[G] [J] [L] [J] [S] [C] [G] [M] [F]
[H] [W] [V] [P] [W] [H] [H] [N] [N]
[J] [V] [G] [B] [F] [G] [D] [H] [G]
 1   2   3   4   5   6   7   8   9
"""

stacks = [['J', 'H', 'G', 'M', 'Z', 'N', 'T', 'F'],
          ['V', 'W', 'J'],
          ['G', 'V', 'L', 'J', 'B', 'T', 'H'],
          ['B', 'P', 'J', 'N', 'C', 'D', 'V', 'L'],
          ['F', 'W', 'S', 'M', 'P', 'R', 'G'],
          ['G', 'G', 'C', 'F', 'B', 'N', 'V', 'M'],
          ['D', 'H', 'G', 'M', 'R'],
          ['H', 'N', 'M', 'V', 'Z', 'D'],
          ['G', 'N', 'F', 'H']
          ]


def debug_stacks():
    print("\n\n----")
    for x in range(len(stacks)):
        print(stacks[x])


def load_input():
    with open('./Day05/input.txt', 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
    return lines


def part1(lines: list):
    pass


if __name__ == '__main__':
    lines = load_input()
    part1(lines)
