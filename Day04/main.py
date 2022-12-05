"""
Advent of Code - 2022
Day 4
"""

def explode(txt_range: str) -> str:
    """
    Takes a textual version of a range (e.g. 2-4) and returns it as
    an expanded string (e.g. "234")
    """
    a, b = txt_range.split('-')
    x = ""
    for i in range(int(a), int(b) + 1):
        x += " " + str(i) + " "
    return x


def part1(cleaning_pairs: list):
    dup_counts = 0
    for pair in cleaning_pairs:
        pair = pair.rstrip()
        elf_1, elf_2 = pair.split(',')
        elf_1 = explode(elf_1)
        elf_2 = explode(elf_2)
        if elf_1 in elf_2 or elf_2 in elf_1:
            dup_counts += 1
    print(f"There were {dup_counts} duplicates found.")


if __name__ == "__main__":
    with open('./input.txt', 'r') as f:
        cleaning_pairs = f.readlines()
    part1(cleaning_pairs)
