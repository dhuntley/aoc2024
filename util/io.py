def readTokens(path: str) -> list[list[str]]:
    tokens: list[list[str]] = []

    with open(path) as f:
        for line in f:
            tokens.append(line.split())
    
    return tokens

def readLines(path: str) -> list[str]:
    lines: list[str] = []
    with open(path) as f:
        lines = f.readlines()
    return lines