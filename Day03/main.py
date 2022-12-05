"""
Advent Of Code - 2022
Day 3
"""

import string


def enumerate() -> dict:
    chars = string.ascii_lowercase + string.ascii_uppercase
    cnt = 0
    priority_score = {}

    for char in chars:
        cnt += 1
        priority_score[char] = cnt

    return priority_score


def main(inventories: list):
    dbg_cnt = 0
    scoring = enumerate()
    sum = 0
    for inventory in inventories:
        dbg_cnt += 1
        x = int(len(inventory) / 2)
        first = set(inventory[:x])
        second = set(inventory[x:])
        for char in first:
            if char in second:
                sum += scoring[char]
    print(f"Total score sum is {sum}")


if __name__ == '__main__':
    inventories = []
    with open("./input.txt", 'r') as f:
        inventories = f.readlines()

    main(inventories)
