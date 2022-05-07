f = open("input.txt", "r")
inputs = f.read().split("\n")


def loops_forever(inputs):
    acc = 0
    pc = 0
    pcs = []

    while True:
        if pc in pcs:
            return True, acc
        if pc == len(inputs):
            return False, acc
        pcs.append(pc)

        ins = inputs[pc].split()
        # print(pc, ins)
        if ins[0] == "acc":
            acc += int(ins[1])
        elif ins[0] == "jmp":
            pc += int(ins[1])-1
        pc += 1


def part_two():
    for i in range(len(inputs)):
        ins = inputs[i].split()
        if ins[0] == "nop":
            inps = inputs[:i] + [f"jmp {ins[1]}"] + inputs[i+1:]
            loops, acc = loops_forever(inps)
            if not loops:
                return acc
        elif ins[0] == "jmp":
            inps = inputs[:i] + [f"nop {ins[1]}"] + inputs[i+1:]
            loops, acc = loops_forever(inps)
            if not loops:
                return acc


def main():
    print(f"part one: {loops_forever(inputs)}")
    print(f"part two: {part_two()}")


main()
