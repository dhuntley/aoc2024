from util.io import readTokens
from functools import reduce

def isPossiblyTrue(testValue: int, currentValue: int, index: int, operands: list[int]) -> bool:
    if index == len(operands):
        return testValue == currentValue

    # Check addition and multiplication
    return isPossiblyTrue(testValue, currentValue + operands[index], index + 1, operands) \
        or isPossiblyTrue(testValue, currentValue * operands[index], index + 1, operands)

def getTruthScore(equation: list[int]) -> int:
    return equation[0] if isPossiblyTrue(equation[0], equation[1], 2, equation) else 0

def main() -> None:
    input = readTokens("./day07/data/input1.txt")
    equations: list[list[int]] = [[int(token.strip(":")) for token in line] for line in input]
    print(reduce(lambda score, equation: score + getTruthScore(equation), equations, 0))


if __name__ == "__main__":
    main()
