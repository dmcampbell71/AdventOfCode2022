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


def debug_stacks():
    print("\n\n----")
    for x in range(len(stacks)):
        print(stacks[x])


def load_input() -> tuple[list, list]:
    with open('./input.txt', 'r', encoding='utf-8') as f:
        containers, moves = [x for x in f.read().split("\n\n")]
    return containers, moves


def load_stacks(containers: list) -> list:
    num_stacks = int(containers.splitlines()[-1:][0].split()[-1])
    containers = containers.splitlines()[:-1]
    stacks = [[] for _ in range(num_stacks)]
    for line in containers:
        processed_line = []
        for i in range(len(line)):
            if i == 1 or (i - 1) % 4 == 0:
                processed_line.append(line[i].strip())
        for i in range(len(processed_line)):
            stacks[i].extend(processed_line[i])
    stacks = [elem[::-1] for elem in stacks]
    return stacks


def move_crates(moves: list, stacks: list) -> list:
    moves = moves.splitlines()
    for move in moves:
        move = move.rstrip().split()
        amount = int(move[1])
        from_stack = int(move[3]) - 1
        to_stack = int(move[5]) - 1
        stacks[to_stack].extend(list(reversed(stacks[from_stack][-amount:])))
        del stacks[from_stack][-amount::]
    return stacks


if __name__ == '__main__':
    containers, moves = load_input()
    stacks = load_stacks(containers)
    final_stacks = move_crates(moves, stacks)

    results = "".join([elem[-1] for elem in final_stacks])
    print(f"Results : {results}")