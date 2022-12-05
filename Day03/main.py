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


def part1(inventories: list):
    sum = 0
    for inventory in inventories:
        x = int(len(inventory) / 2)
        first = set(inventory[:x])
        second = set(inventory[x:])
        for char in first:
            if char in second:
                sum += scoring[char]
    print(f"Part 1 Total score sum is {sum}")


def part2(inventories: list):
    sum = 0
    dbg_cnt = 0
    while inventories:
        dbg_cnt += 1
        group = inventories[:3]
        del inventories[:3]
        first_elf = set(group[0].rstrip())
        second_elf = set(group[1].rstrip())
        third_elf = set(group[2].rstrip())
        char_cnt=0
        for char in first_elf:
            char_cnt += 1
            if char in second_elf and char in third_elf:
                sum += scoring[char]
                break
    print(f"Part 2 Total score sum in {sum}")


def main(inventories: list):
    global scoring
    scoring = enumerate()
    part1(inventories)
    part2(inventories)
    pass


if __name__ == '__main__':
    inventories = []
    with open("./input.txt", 'r') as f:
        inventories = f.readlines()

    main(inventories)
