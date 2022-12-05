instructions = []

with open ("data.txt") as f:
    for line in f.readlines():
        tokens = []
        for token in line.strip().split(' '):
            tokens.append(token)
            # print(tokens)
        instructions.append(tokens)
    # print(instructions)

stacks = [
    ['J','H','G','M','Z','N','T','F'], 
    ['V','W','J'], 
    ['G','V','L','J','B','T','H'], 
    ['B','P','J','N','C','D','V','L'], 
    ['F','W','S','M','P','R','G'], 
    ['G','H','C','F','B','N','V','M'],
    ['D','H','G','M','R'], 
    ['H','N','M','V','Z','D'], 
    ['G','N','F','H']
]

for x in instructions:
    num_crates = int(x[1])
    start = int(x[3])
    end = int(x[5])

    # align indices
    start -= 1
    end -= 1
    queue = []

    for element in range(num_crates):
        pop = stacks[start].pop()
        # insert at 0 to maintain priority
        queue.insert(0, pop)
        # print("Queue:", queue)
    for item in queue:
        stacks[end].append(item)
        # print(stacks[end])

result_stack = ""
for top_element in stacks:
    result_stack += top_element[-1]

print("Part 2 Elements:", result_stack)