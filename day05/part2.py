from util.io import readLines

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
    
    def isValidByRule(self, rule: Rule) -> bool:
        return self.pages.count(rule.firstPage) == 0 \
                or self.pages.count(rule.secondPage) == 0 \
                or self.pages.index(rule.firstPage) < self.pages.index(rule.secondPage)

    
    def fix(self, brokenRules: list[Rule]) -> None:
        for rule in brokenRules:
            a, b = self.pages.index(rule.firstPage), self.pages.index(rule.secondPage)
            self.pages[a], self.pages[b] = self.pages[b], self.pages[a]

    def getBrokenRules(self, rules: list[Rule]) -> list[Rule]:
        return [rule for rule in rules if not self.isValidByRule(rule)]
                

def main():
    input = readLines("./day05/data/input1.txt")

    rules = [Rule(line) for line in input if line.count("|") > 0]
    updates = [Update(line) for line in input if line.count(",") > 0]
    
    score = 0
    for update in updates:
        brokenRules = update.getBrokenRules(rules)
        if len(brokenRules) > 0:
            while len(brokenRules) > 0:
                update.fix([brokenRules[0]])
                brokenRules = update.getBrokenRules(rules)
            score += update.getMiddlePage()
    
    print(score)
    

if __name__ == "__main__":
    main()
