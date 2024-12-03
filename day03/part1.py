import re
from functools import reduce
from util.io import readLines

def eval(statement) -> int:
    factors = re.findall(r"\d+", statement)
    return int(factors[0]) * int(factors[1])

def main():
    input = readLines("./day03/data/input1.txt")[0]
    print(reduce(lambda sum, statement: sum + eval(statement), re.findall(r"mul\(\d+,\d+\)", input), 0))


if __name__ == "__main__":
    main()
