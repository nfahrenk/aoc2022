# Change size to 4 for part 1
size = 14
message = ['' for i in range(0, size)]

def check_starter():
    return len(set(message)) == len(message)

def solution(filename):
    with open(filename) as f:
        for line in f:
            comm = line.rstrip()
    return transmission(comm)

def transmission(comm):
    counter = 0
    for char in comm:
        message.pop(0)
        message.append(char)
        counter += 1
        
        if counter >= (size - 1) and check_starter():
            print(message)
            return counter
    return -1

print(transmission('bvwbjplbgvbhsrlpgdmjqwftvncz'))
print(transmission('nppdvjthqldpwncqszvftbrmjlhg'))
print(transmission('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'))

print(transmission('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'))
print(solution('day6/input1.txt'))
