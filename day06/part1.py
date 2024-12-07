from util.io import readLines
from enum import Enum


class Bearing(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


def getInitialPos(input) -> tuple[int, int, Bearing]:
    pos: tuple[int, int, Bearing] = (0, 0, Bearing.NORTH)   
    for line in input:
        for char in line:
            if char == "^":
                return pos
            pos = (pos[0], pos[1] + 1, Bearing.NORTH)
        pos = (pos[0] + 1, 0, Bearing.NORTH)
    raise Exception("Error finding initial position")


def advancePos(pos: tuple[int, int, Bearing], obstacleMap: list[list[bool]]) -> tuple[int, int, Bearing]:
    if (pos[2] == Bearing.NORTH):
        if isObstacle((pos[0] - 1, pos[1]), obstacleMap):
            return (pos[0], pos[1], Bearing.EAST)
        else:
            return (pos[0] - 1, pos[1], Bearing.NORTH)
    if (pos[2] == Bearing.EAST):
        if isObstacle((pos[0], pos[1] + 1), obstacleMap):
            return (pos[0], pos[1], Bearing.SOUTH)
        else:
            return (pos[0], pos[1] + 1, Bearing.EAST)
    if (pos[2] == Bearing.SOUTH):
        if isObstacle((pos[0] + 1, pos[1]), obstacleMap):
            return (pos[0], pos[1], Bearing.WEST)
        else:
            return (pos[0] + 1, pos[1], Bearing.SOUTH)
    else: # WEST
        if isObstacle((pos[0], pos[1] - 1), obstacleMap):
            return (pos[0], pos[1], Bearing.NORTH)
        else:
            return (pos[0], pos[1] - 1, Bearing.WEST)

def isGone(pos: tuple[int, int], obstacleMap: list[list[bool]]) -> bool:
    return pos[0] < 0 or pos[1] < 0 or pos[0] >= len(obstacleMap) or pos[1] >= len(obstacleMap[0])

def isObstacle(pos: tuple[int, int], obstacleMap: list[list[bool]]) -> bool:
    return not isGone(pos, obstacleMap) and obstacleMap[pos[0]][pos[1]]

def main() -> None:
    input = readLines("./day06/data/input1.txt")
    obstacleMap: list[list[bool]] = [[char == '#' for char in line] for line in input]
    pos = getInitialPos(input)

    visited: set[tuple[int, int]] = set()
    visited.add(pos[:2])

    while True:
        pos = advancePos(pos, obstacleMap)
        if isGone(pos[:2], obstacleMap):
            break
        else:
            visited.add(pos[:2])
    
    print(len(visited))


if __name__ == "__main__":
    main()
