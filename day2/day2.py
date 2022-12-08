# rock a, x
# paper b, y
# scissors c, z
DRAW = 3
WIN = 6
LOSE = 0
points = {
    'A X': DRAW,
    'A Y': WIN,
    'A Z': LOSE,
    
    'B Y': DRAW,
    'B Z': WIN,
    'B X': LOSE,

    'C Z': DRAW,
    'C X': WIN,
    'C Y': LOSE,
}

move = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

ROCK = 'X'
PAPER = 'Y'
SCISSORS = 'Z'

part2 = {
    'A X': SCISSORS,
    'A Y': ROCK,
    'A Z': PAPER,
    
    'B X': ROCK,
    'B Y': PAPER,
    'B Z': SCISSORS,

    'C X': PAPER,
    'C Y': SCISSORS,
    'C Z': ROCK,
}

part2_points = {
    'X': LOSE,
    'Y': DRAW,
    'Z': WIN,
}

def get_score(code):
    return move[part2[code]] + part2_points[code[-1]]

def play_game(filename):
    with open(filename) as f:
        points = [get_score(line.rstrip()) for line in f]
    return sum(points)

print(play_game('day2/input2.txt'))