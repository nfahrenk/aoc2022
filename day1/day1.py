def day1(filename):
    f = open(filename,"r")
    lines = f.readlines()
    
    total = 0
    sums = [10, 11, 12]
    for line in lines:
        line = line.rstrip()
        if line:
            total += int(line)
        else:
            sums.append(total)
            total = 0
    sums.append(total)
    top3 = sorted(sums)[-3:]
    return sum(top3)

print(day1('input1.txt'))