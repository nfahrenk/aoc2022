class Bound(object):
    def __init__(self, left, right):
        self.Right = right
        self.Left = left

    def contains(self, other):
        return (
            other.Left <= self.Right and other.Left >= self.Left
        ) or (
            other.Left <= self.Left and other.Right >= self.Left
        )

def create_bound(line):
    parts = line.split('-')
    return Bound(int(parts[0]), int(parts[1]))  

def assignments(filename):
    counter = 0
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            
            parts = line.split(',')
            left = parts[0]
            right = parts[1]
            
            bound1 = create_bound(left)
            bound2 = create_bound(right)

            counter += 1 if bound1.contains(bound2) else 0
    return counter

print(assignments('day4/input1.txt'))