from util.io import readTokens

def main():
    tokens = readTokens("./day01/data/input1.txt")
    leftList = list(map(lambda t: int(t[0]), tokens))
    rightList = list(map(lambda t: int(t[1]), tokens))
    
    rightCounts = dict.fromkeys(rightList, 0)
    for item in rightList:
        rightCounts[item] = rightCounts[item] + 1

    similarityScore = 0
    for item in leftList:
        similarityScore += item * rightCounts.get(item, 0)

    print(similarityScore)


if __name__ == "__main__":
    main()
