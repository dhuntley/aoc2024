from util.io import readLines

def isChar(x: int, y: int, char: str, grid: list[list[str]]) -> bool:
    return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[x]) and grid[x][y] == char

def countXmasCrossFromOrigin(x: int, y: int, grid: list[list[str]]) -> int:
    if not isChar(x,y,'A', grid):
        return 0
    elif isChar(x-1, y-1, 'M', grid) and isChar(x+1, y+1, 'S', grid) and isChar(x-1, y+1, 'M', grid) and isChar(x+1, y-1, 'S', grid):
        return 1
    elif isChar(x-1, y-1, 'M', grid) and isChar(x+1, y+1, 'S', grid) and isChar(x-1, y+1, 'S', grid) and isChar(x+1, y-1, 'M', grid):
        return 1
    elif isChar(x-1, y-1, 'S', grid) and isChar(x+1, y+1, 'M', grid) and isChar(x-1, y+1, 'M', grid) and isChar(x+1, y-1, 'S', grid):
        return 1
    elif isChar(x-1, y-1, 'S', grid) and isChar(x+1, y+1, 'M', grid) and isChar(x-1, y+1, 'S', grid) and isChar(x+1, y-1, 'M', grid):
        return 1
    else:
        return 0

def main():
    input = readLines("./day04/data/input1.txt")
    letterGrid = list(map(lambda line: list(map(lambda letter: letter, line.strip())), input))
    
    count = 0
    for x in range(len(letterGrid)):
        for y in range(len(letterGrid[x])):
            count += countXmasCrossFromOrigin(x, y, letterGrid)
    print(count)

if __name__ == "__main__":
    main()
