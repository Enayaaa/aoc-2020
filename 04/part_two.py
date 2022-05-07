
def okChars(word):
    for w in word:
        if not (w in "abcdef0123456789"):
            return False
    return True


def validCredentials(p):
    print(p)
    for i in p:
        val = i[4:]
        if i.startswith("byr") and (not (int(val)>=1920 and int(val)<=2002)):
            return False
        if i.startswith("iyr") and (not (int(val)>=2010 and int(val)<=2020)):
            return False
        if i.startswith("eyr") and (not (int(val)>=2020 and int(val)<=2030)):
            return False
        if i.startswith("hgt"):
            if val.endswith("cm") and not (int(val[:-2])>=150 and int(val[:-2])<=193):
                return False
            if val.endswith("in") and not (int(val[:-2])>=59 and int(val[:-2])<=76):
                return False
            if not (val.endswith("cm") or val.endswith("in")):
                return False
        if i.startswith("hcl"):
            if not (val.startswith("#") and len(val)>=7):
                return False
            elif not okChars(val[1:]):
                return False
        if i.startswith("ecl") and not (val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            return False
        if i.startswith("pid"):
            if not (val.isdigit() and len(val) == 9):
                return False
    return True


def isValid(p, skipCid):
    if len(p) == 8:
        return validCredentials(p)
    if len(p) == 8-skipCid:
            ok = True
            for i in p:
                if i.startswith("cid"):
                    ok = False
            return ok and validCredentials(p)
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