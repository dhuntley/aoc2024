from util.io import readLines

Coords = tuple[int, int]

def main() -> None:
    input = readLines("./day08/data/input1.txt")
    antennas : dict[str, list[Coords]] = dict()

    for row in range(len(input)):
        for col in range(len(input[row].strip())):
            freq = input[row][col]
            if freq == ".":
                continue
            freqAntennas = antennas.get(freq, [])
            freqAntennas.append((row, col))
            antennas[freq] = freqAntennas

    def isInBounds(coords: Coords) -> bool:
        return coords[0] >=0 and coords[1] >= 0 and coords[0] < len(input) and coords[1] < len(input[0].strip())

    def getAntinodes(a: Coords, b: Coords) -> list[Coords]:
        deltaRow = abs(a[0] - b[0])
        deltaCol = abs(a[1] - b[1])

        if (a[0] < b[0] and a[1] < b[1]) or (a[0] > b[0] and a[1] > b[1]):
            c = (min(a[0], b[0]) - deltaRow, min(a[1], b[1]) - deltaCol)
            d = (max(a[0], b[0]) + deltaRow, max(a[1], b[1]) + deltaCol)
        else:
            c = (min(a[0], b[0]) - deltaRow, max(a[1], b[1]) + deltaCol)
            d = (max(a[0], b[0]) + deltaRow, min(a[1], b[1]) - deltaCol)

        antinodes = []
        if isInBounds(c):
            antinodes.append(c) 
        if isInBounds(d):
            antinodes.append(d)

        return antinodes

    antinodes: set[Coords] = set()
    
    for freq in antennas.keys():
        print(freq)
        freqAntennas = antennas.get(freq, [])
        for aIndex in range(len(freqAntennas)):
            for bIndex in range(aIndex + 1, len(freqAntennas)):
                a = freqAntennas[aIndex]
                b = freqAntennas[bIndex]
                antinodes.update(getAntinodes(a,b))

    print(len(antinodes))

if __name__ == "__main__":
    main()
