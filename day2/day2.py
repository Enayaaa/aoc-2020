class Policy:
    def __init__(self, min, max, letter, password):
        self.min = int(min)
        self.max = int(max)
        self.letter = letter
        self.password = password

def objectify(line):
    input = line.split()
    min, max = input[0].split('-')
    letter = input[1][:1]
    password = input[2]
    return Policy(min, max, letter, password)

def main():
    passwords = []
    f = open("input.txt", "r")
    for line in f:
        passwords.append(objectify(line))

    valids = 0
    for i in passwords:
        count = i.password.count(i.letter)
        if count<=i.max and count>=i.min:
            valids += 1
    print(valids)

main()