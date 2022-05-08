from functools import cache

def possibles(output, ratings):
    return [x for x in ratings if x <= output+3 and x > output]


def solve_one(ratings):
    diffs = []
    output = 0
    for _ in ratings:
        possible = possibles(output, ratings)
        if len(possible) > 0:
            diffs.append(possible[0]-output)
            output = possible[0]
    return diffs.count(1)*(diffs.count(3)+1)

def solve_two(ratings):
    goal = max(ratings)

    @cache
    def combs(output: int) -> int:
        if output == goal:
            return 1
        possible = possibles(output, ratings)
        if len(possible) == 0:
            return 0
        return sum(combs(poss) for poss in possible)

    return combs(0)


def main():
    f = open("input.txt", "r")
    inp = sorted(map(lambda x: int(x), f.read().split()))
    print(solve_one(inp))
    print(solve_two(inp))


main()
