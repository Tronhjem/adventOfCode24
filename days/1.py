testInput = ['3   4','4   3', '2   5', '1   3', '3   9', '3   3'] 

def sortInput(input ):
    # input = testInput
    leftColumn = []
    rightColumn = []

    for pair in input:
        split = pair.split(' ')
        leftColumn.append(int(split[0]))
        rightColumn.append(int(split[3]))
    
    leftColumn.sort()
    rightColumn.sort()
    return leftColumn, rightColumn


def partOne(input):
    leftColumn, rightColumn = sortInput(input)

    sum = 0
    for x in range(len(leftColumn)):
        sum += abs(leftColumn[x] - rightColumn[x])
        
    print(sum)


def partTwo(input):
    # input = testInput
    leftColumn, rightColumn = sortInput(input)

    score = 0
    for x in leftColumn:
        occurances = 0
        for y in rightColumn:
            if x == y:
                occurances += 1
        score += occurances * x
        
    print(score)


def main(input):
    # partOne(input)
    partTwo(input)