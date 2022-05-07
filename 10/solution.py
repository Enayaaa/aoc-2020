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
    return "Ofcoarse I don't know dynamic programming"


def main():
    f = open("input1.txt", "r")
    input = list(map(lambda x: int(x), f.read().split()))
    input.sort()

    print(solve_one(input))
    print(solve_two(input))


main()
