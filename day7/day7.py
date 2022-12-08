from collections import defaultdict

class Dir(object):
    def __init__(self, name, parent):
        self.name = name
        self.children = {}
        self.parent = parent
    
    def add_child(self, child):
        if child.name in self.children:
            return
        self.children[child.name] = child
    
    def child(self, name):
        if name not in self.children:
            raise Exception('Invalid directory name ' + name)
        return self.children[name]
    
    def __str__(self) -> str:
        return self.name + '\n' + '\n'.join([str(val) for val in self.children.values()])

class File(object):
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
    
    def __str__(self) -> str:
        return str(self.size) + ' ' + self.name

def create_key(node):
    return node.name + '--' + str(id(node))

def dfs(root):
    nodes = [root]
    sizes = defaultdict(lambda: 0)
    while nodes:
        node = nodes.pop(0)
        if isinstance(node, Dir):
            for child in node.children.values():
                nodes.append(child)
        else:
            size = node.size
            while node.name != '/':
                sizes[create_key(node.parent)] += size
                node = node.parent
    return sizes
        

def filesystem(filename):
    root = Dir('/', None)
    node = root
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            if line == '$ cd /':
                node = root
            elif line == '$ ls':
                pass
            elif not line.startswith('$ '):
                if line.startswith('dir'):
                    node.add_child(Dir(line.split('dir ')[1], node))
                else:
                    parts = line.split(' ')
                    node.add_child(File(parts[1], int(parts[0]), node))
            elif line.startswith('$ cd '):
                directory = line[len('$ cd '):]
                if directory == '..':
                    node = node.parent
                else:
                    node = node.child(directory)
    sizes = dfs(root)
    print(sizes)
    # part one
    # threshold = 100000
    # return sum([val for val in sizes.values() if val <= threshold])

    # part two
    SPACE_NEEDED = 30000000
    TOTAL_SPACE = 70000000
    unused_space = TOTAL_SPACE - sizes[create_key(root)]
    threshold = SPACE_NEEDED - unused_space
    return min([val for val in sizes.values() if val >= threshold])

print(filesystem('day7/input1.txt'))
