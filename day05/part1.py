from util.io import readLines
from functools import reduce

class Rule:
    firstPage: int

    secondPage: int

    def __init__(self, line: str):
        pages = line.split("|")
        self.firstPage = int(pages[0])
        self.secondPage = int(pages[1])


class Update:
    pages: list[int]

    def __init__(self, line: str):
        self.pages = [int(x) for x in line.split(",")]

    def getMiddlePage(self) -> int:
        return self.pages[int(len(self.pages) / 2)]
    
    def _isValidByRule(self, rule: Rule) -> bool:
        return self.pages.count(rule.firstPage) == 0 \
                or self.pages.count(rule.secondPage) == 0 \
                or self.pages.index(rule.firstPage) < self.pages.index(rule.secondPage)
    
    def isValid(self, rules: list[Rule]) -> bool:
        return reduce(lambda valid, rule: valid and self._isValidByRule(rule), rules, True)
    
    def validityScore(self, rules: list[Rule]) -> int:
        return self.getMiddlePage() if self.isValid(rules) else 0

def main():
    input = readLines("./day05/data/input1.txt")

    rules = [Rule(line) for line in input if line.count("|") > 0]
    updates = [Update(line) for line in input if line.count(",") > 0]
    
    print(reduce(lambda score, update: score + update.validityScore(rules), updates, 0))
    

if __name__ == "__main__":
    main()
