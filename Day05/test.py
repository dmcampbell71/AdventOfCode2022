stacks = [['A', 'B', 'C'], [], ['X', 'Y', 'Z']]

line = "move 1 from 3 to 2"

_, count, _, move_from, _, move_to = line.split()

for x in range(int(count)):
    move_from = int(move_from) - 1
    print(f"move_from => {move_from}")
    move_to = int(move_to) - 1
    print(f"move_to => {move_to}")

    temp = stacks[move_from].pop()
    stacks[move_to].append(temp)
    print(stacks)
