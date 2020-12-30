
def isValid(p, skipCid):
    if len(p) == 8:
        return True
    if len(p) == 8-skipCid:
            ok = True
            for i in p:
                if i.startswith("cid"):
                    ok = False
            return ok
    return False


def main():
    f = open("input.txt", "r")
    passports = f.read().split("\n\n")

    valids = 0
    for p in passports:
        if isValid(p.split(), 1):
            valids += 1
    print(valids)

main()