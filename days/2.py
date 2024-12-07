testInput = [
    '7 6 4 2 1',
    '1 2 7 8 9',
    '9 7 6 2 1',
    '1 3 2 4 5',
    '8 6 4 4 1',
    '1 3 6 7 9'
]

def difDirection(diff):
    if diff > 0:
        return -1
    elif diff < 0:
        return 1
    else:
        return 0
        

def isSafe(line):
    lastDirection = -99
    for x in range(len(line)-1):
        dif = line[x] - line[x+1]

        if abs(dif) > 3:
            return False

        direction = difDirection(dif)
        if lastDirection != -99 and (lastDirection != direction and (direction != 0 or lastDirection != 0)):
            return False

        lastDirection = direction

    return True 


def sanitizeInput(input):
    return list(map(lambda x: list(map(int, x.split(' '))), input))


def partOne(input):
    input = sanitizeInput(input)
    safeCount = 0
    for line in input:
        if isSafe(line):
            safeCount += 1

    print(safeCount)


def partTwo(input):
    input = sanitizeInput(input)
    safeCount = 0
    for line in input:
        if isSafe(line):
            safeCount += 1
        else:
            for x in range(len(line)):
                

    print(safeCount)


def main(input):
    partOne(input)
    # partTwo(input)    