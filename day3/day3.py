def rucksack(line):
    left = set([])
    right = set([])
    middle = int(len(line)/2)
    for start in range(0, middle):
        left_char = line[start]
        if left_char in right:
            return left_char
        left.add(left_char)

        right_char = line[middle + start]
        if right_char in left:
            return right_char
        right.add(right_char)
    raise Exception('Did not find char')

def convert_to_point(char):
    ascii = ord(char)
    if ascii >= 97:
        return ascii - 97 + 1
    else:
        return 27 + ascii - 65

def open_rucksacks(filename):
    with open(filename) as f:
        chars = [rucksack(line.rstrip()) for line in f]
    points = [convert_to_point(char) for char in chars]
    return sum(points)

# PART TWO

def rucksack2(left_line, middle_line, right_line):
    left = set(left_line)
    middle = set(middle_line)
    right = set(right_line)
    output = left.intersection(middle, right)
    if len(output) != 1:
        raise Exception('Found incorrect size of intersection: ' + output)
    for elem in output:
        return elem

def badge(filename):
    chars = []
    with open(filename) as f:
        group = []
        for line in f:
            line = line.rstrip()
            group.append(line)
            if len(group) == 3:
                print(group)
                chars.append(rucksack2(group[0], group[1], group[2]))
                group = []
    points = [convert_to_point(char) for char in chars]
    return sum(points)

print(badge('day3/input1.txt'))