class Bag:
    def __init__(self, code):
        c = code.strip().split()
        self.count = int(c[0])
        self.color = c[1] + " " + c[2]


def canHold(elem, list):
    can_hold = []
    for r in list:
        for m in r:
            for b in r[m]:
                if b.color == elem:
                    if m not in can_hold:
                        can_hold.append(m)
                    for i in canHold(m, list):
                        if i not in can_hold:
                            can_hold.append(i)
    return can_hold


def solve_1(rules):
    return len(canHold("shiny gold", rules))


def count_children(color, rules):
    count = 0
    for r in rules:
        for m in r:
            if m == color:
                for b in r[m]:
                    count += b.count + b.count * count_children(b.color, rules)
    return count


def solve_2(rules):
    return count_children("shiny gold", rules)


def main():
    f = open("input.txt")
    inputs = f.read().split("\n")

    rules = []
    for i in inputs:
        rule = i.split(" bags contain ")
        bags = {rule[0]: []}
        for r in rule[1].split(","):
            if r.startswith("no other bags"):
                continue
            else:
                bags[rule[0]].append(Bag(r))
        rules.append(bags)

    print(f"part one: {solve_1(rules)}")
    print(f"part two: {solve_2(rules)}")


main()
