def update_stack(stacks, line):
    stack_ndx = 0
    for pos in range(0, len(line), 4):
        if line[pos] == '[':
            stacks[stack_ndx].insert(0, line[pos + 1])
        stack_ndx += 1

def initialize_stacks(stacks, line):
    for i in range(0, int(len(line) / 4)):
        stacks.append([])

def move_stacks(stacks, start, end, count):
    for _ in range(0, count):
        stacks[end].append(stacks[start].pop())

# implementation of move_stacks for part 2
def move_stacks2(stacks, start, end, count):
    tmp_stack = []
    for _ in range(0, count):
        tmp_stack.append(stacks[start].pop())
    while tmp_stack:
        stacks[end].append(tmp_stack.pop())

def boxes(filename):
    stacks = []
    with open(filename) as f:
        # Build the stacks
        for line in f:
            if len(stacks) == 0:
                initialize_stacks(stacks, line)
            line = line.rstrip()
            if not line:
                break
            update_stack(stacks, line)
        print(stacks)
        # Move section
        for line in f:
            parts = line.split(' ')
            count, start, end = int(parts[1]), int(parts[3]) - 1, int(parts[5]) - 1
            move_stacks2(stacks, start, end, count)
        # Get the top of each stack
        output = ''
        print(stacks)
        for stack in stacks:
            output += stack[-1]
    return output

print(boxes('day5/input1.txt'))