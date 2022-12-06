with open('./input.txt', 'r', encoding="utf-8") as fh:
    stacks, moves = fh.read().split("\n\n")


max_stacks = stacks.splitlines()[-1:][0].split()[-1]

x = [[] for _ in range(int(max_stacks))]
stacks = stacks.splitlines()[:-1]
for line in stacks:
    processed_line = []
    for i in range(len(line)):
        if i == 1 or (i - 1) % 4 == 0:
            processed_line.append(line[i].strip())
    # print(processed_line)
    for i in range(len(processed_line)):
        x[i].extend(processed_line[i])
    print(x)
    x = [elem[::-1] for elem in x]
