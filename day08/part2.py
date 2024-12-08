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

    def generateAntinodes(origin: Coords, deltaRow, deltaCol) -> set[Coords]:
        antinodes = set()
        factor = 0
        while True:
            node = (origin[0] + deltaRow * factor, origin[1] + deltaCol * factor)
            if not isInBounds(node):
                break
            antinodes.add(node)
            factor = factor + 1
        return antinodes
        

    def getAntinodes(a: Coords, b: Coords) -> set[Coords]:
        deltaRow = abs(a[0] - b[0])
        deltaCol = abs(a[1] - b[1])
        antinodes = set()
        if (a[0] < b[0] and a[1] < b[1]) or (a[0] > b[0] and a[1] > b[1]):
            antinodes.update(generateAntinodes((min(a[0], b[0]), min(a[1], b[1])), -deltaRow, -deltaCol))
            antinodes.update(generateAntinodes((max(a[0], b[0]), max(a[1], b[1])), deltaRow, deltaCol))
        else:
            antinodes.update(generateAntinodes((min(a[0], b[0]), max(a[1], b[1])), -deltaRow, deltaCol))
            antinodes.update(generateAntinodes((max(a[0], b[0]), min(a[1], b[1])), deltaRow, -deltaCol))
        return antinodes

    antinodes: set[Coords] = set()
    
    for freq in antennas.keys():
        freqAntennas = antennas.get(freq, [])
        for aIndex in range(len(freqAntennas)):
            for bIndex in range(aIndex + 1, len(freqAntennas)):
                a = freqAntennas[aIndex]
                b = freqAntennas[bIndex]
                antinodes.update(getAntinodes(a,b))

    print(len(antinodes))

if __name__ == "__main__":
    main()
