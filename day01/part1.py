from util.io import readTokens

def main():
    tokens = readTokens("./day01/data/input1.txt")
    listA = sorted(map(lambda t: int(t[0]), tokens))
    listB = sorted(map(lambda t: int(t[1]), tokens))

    totalDistance = 0
    for index in range(len(listA)):
        totalDistance += abs(listA[index] - listB[index])

    print(totalDistance)


if __name__ == "__main__":
    main()
