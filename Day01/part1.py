"""
Advent Of Code - 2022
Day 1

Part 1
------
Given a file listing groups of items carried by individual elves, separated
by blank lines, find the max # of calories (sum) carried by an individual elf.
    Answer 71502

Part 2
------
Find the sum of calories carried by the top three elves.
    Answer: 208191
"""

with open("./input.txt", 'r') as f:
    total = 0
    elves_total = []

    lines = f.readlines()
    # for x in range(len(lines)):
    #     lines[x] = lines[x].rstrip()
    #     if lines[x] != '':
    #         total = total + int(lines[x])
    #     else:
    #         elves_total.append(total)
    #         total = 0
    #
    # or
    for line in lines:
        if line == '\n':
            elves_total.append(total)
            total = 0
        else:
            total += int(line.rstrip())
    print("The elf carrying the maximum count of calories carried "
          f"{max(elves_total)} calories.")

    # part 2
    total = 0
    # for x in range(3):
    #     total += max(elves_total)
    #     elves_total.pop(elves_total.index(max(elves_total)))
    # or
    elves_total.sort(reverse=True)
    total += sum([elves_total[x] for x in range(3)])
    print(f"Total calories for top 3 elves is {total}.")
