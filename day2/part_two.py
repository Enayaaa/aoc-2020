class Policy:
    def __init__(self, index1, index2, letter, password):
        self.index1 = index1
        self.index2 = index2
        self.letter = letter
        self.password = password


def objectify(line):
    input = line.split()
    index1, index2 = input[0].split('-')
    letter = input[1][:1]
    password = input[2]
    return Policy(int(index1)-1, int(index2)-1, letter, password)


def valid(i):
    if i.password[i.index1] == i.letter and i.password[i.index2] != i.letter:
        return True
    if i.password[i.index2] == i.letter and i.password[i.index1] != i.letter:
        return True
    return False


def main():
    passwords = []
    f = open("input1.txt", "r")
    for line in f:
        passwords.append(objectify(line))

    valids = 0
    for i in passwords:
        if valid(i):
            valids += 1
    print(valids)


main()
