"""
Advent of Code - 2022
Day 4
"""

def explode_to_string(txt_range: str) -> str:
    """
    Takes a textual version of a range (e.g. 2-4) and returns it as
    an expanded string (e.g. "234")
    """
    a, b = txt_range.split('-')
    x = ""
    for i in range(int(a), int(b) + 1):
        x += " " + str(i) + " "
    return x


def explode_to_list(txt_range: str) -> str:
    """
    Takes a textual version of a range (e.g. 2-4) and returns it as
    a list (e.g. [2, 3, 4])
    """
    a, b = txt_range.split('-')
    x = ""
    return [x for x in range(int(a), int(b) + 1)]


def part1(cleaning_pairs: list):
    dup_counts = 0
    for pair in cleaning_pairs:
        pair = pair.rstrip()
        elf_1, elf_2 = pair.split(',')
        elf_1 = explode_to_string(elf_1)
        elf_2 = explode_to_string(elf_2)
        if elf_1 in elf_2 or elf_2 in elf_1:
            dup_counts += 1
    print(f"There were {dup_counts} duplicates found.")


def part2(cleaning_pairs: list):
    dbg_cnt = 0
    overlap_counts = 0
    for pair in cleaning_pairs:
        dbg_cnt += 1
        pair = pair.rstrip()
        elf_1, elf_2 = pair.split(',')
        a, b = elf_1.split('-')
        x, y = elf_2.split('-')
        if int(a) in explode_to_list(elf_2) or int(b) in explode_to_list(elf_2):
            overlap_counts += 1
        elif int(x) in explode_to_list(elf_1) or int(y) in explode_to_list(elf_1):
            overlap_counts += 1

    print(f"There were {overlap_counts} overlaps.")


if __name__ == "__main__":
    with open('./input.txt', 'r') as f:
        cleaning_pairs = f.readlines()
    part1(cleaning_pairs)
    part2(cleaning_pairs)
