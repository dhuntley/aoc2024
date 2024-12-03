from functools import reduce
from util.io import readTokens

def isMonotonic(report: list[int]) -> bool:
    increasing: bool = report[1] > report[0]
    for index in range(1, len(report)):
        if (report[index] > report[index - 1]) != increasing:
            return False
    return True

def validRanges(report: list[int]) -> bool:
    for index in range(1, len(report)):
        diff = abs(report[index] - report[index - 1])
        if diff > 3 or diff < 1:
            return False
    return True

def isSafe(tokens: list[str]) -> bool:
    report = list(map(lambda x: int(x), tokens))

    for index in range(len(report)):
        testReport = report.copy()
        testReport.pop(index)
        if isMonotonic(testReport) and validRanges(testReport):
            return True

    return False

def main():
    reports = readTokens("./day02/data/input1.txt")
    
    safeCount = reduce(lambda prevSafe, report: prevSafe + (1 if isSafe(report) else 0), reports, 0)

    print(safeCount)


if __name__ == "__main__":
    main()
