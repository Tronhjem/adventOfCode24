import re

testPartOne = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]
testPartTwo = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

def findMulInstances(input):
    pattern = re.compile(r'mul\((\d+),(\d+)\)')
    matches = pattern.findall(input)
    return matches


def partOne(input):
    sum = 0
    for line in input:
        matches = findMulInstances(line)
        for match in matches:
            num1, num2 = match
            sum += int(num1) * int(num2)

    print(sum)


def partTwo(input):
    sum = 0
    # input = testPartTwo

    oneLine = f''
    for line in input:
        oneLine += line
    
    dos = re.sub(r"don't\(\).*?(?=do\(\)|$)", "", oneLine, flags=re.DOTALL)
    matches = findMulInstances(dos)
    for match in matches:
        print(match)
        num1, num2 = match
        sum += int(num1) * int(num2)

    print(sum)


def main(input):
    # partOne(input)
    partTwo(input)
