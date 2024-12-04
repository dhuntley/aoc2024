from util.io import readLines

def checkWord(x: int, y: int, deltaX: int, deltaY: int, word: str, grid: list[list[str]]) -> bool:
    if len(word) == 0:
        return True
    
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]) or grid[x][y] != word[0]:
        return False

    return checkWord(x + deltaX, y + deltaY, deltaX, deltaY, word[1:], grid)

def countXmasFromOrigin(x: int, y: int, grid: list[list[str]]) -> int:
    count = 0
    for deltaX in range(-1,2):
        for deltaY in range(-1,2):
            if (checkWord(x, y, deltaX, deltaY, 'XMAS', grid)):
                count = count + 1
    return count


def main():
    input = readLines("./day04/data/input1.txt")
    letterGrid = list(map(lambda line: list(map(lambda letter: letter, line.strip())), input))
    
    count = 0
    for x in range(len(letterGrid)):
        for y in range(len(letterGrid[x])):
            count += countXmasFromOrigin(x, y, letterGrid)
    print(count)

if __name__ == "__main__":
    main()
