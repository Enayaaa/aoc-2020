

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

        ans = []
        for m in group.getmembers():
            for a in m:
                if not a in ans:
                    ans.append(a)
        yeses += len(ans)
    print(yeses)


main()
