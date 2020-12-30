

class Group:
    def __init__(self, code):
        self.code = code

    def getmembers(self):
        return self.code.split()


def main():
    f = open("input.txt", "r")
    inputs = f.read().split("\n\n")

    yeses = 0
    for i in inputs:
        group = Group(i)

        ans = list(group.getmembers()[0])
        acc = list(group.getmembers()[0])

        for a in ans:
            removed = False
            for m in group.getmembers()[1:]:
                if not a in m and not removed:
                    acc.remove(a)
                    removed = True
        yeses += len(acc)

    print(yeses)


main()
