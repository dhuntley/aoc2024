import re
from functools import reduce
from util.io import readLines

def eval(statement) -> int:
    factors = re.findall(r"\d+", statement)
    return int(factors[0]) * int(factors[1])

def main():
    input = readLines("./day03/data/input1.txt")[0]
    statements = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input)

    sum = 0
    enabled = True
    for statement in statements:
        if statement == "do()":
            enabled = True
        elif statement == "don't()":
            enabled = False
        elif enabled:
            sum += eval(statement)

    print(sum)


if __name__ == "__main__":
    main()
