preamble_len = 25


def find_sum(sum, preamble):
    list_of_lists = [[int(x)+int(y) for x in preamble if x !=
                      y if int(x)+int(y) == int(sum)] for y in preamble]
    flattened = [val for sublist in list_of_lists for val in sublist]
    return int(sum) in flattened


def solve_one(inputs):
    preamble = inputs[:preamble_len]
    sums = inputs[preamble_len:]
    for i in range(len(sums)):
        index = i+preamble_len+1
        if not find_sum(sums[i], preamble):
            return int(sums[i])
        preamble = inputs[:index][-preamble_len:]
    return -1


def solve_two(inputs):
    inv = solve_one(inputs)
    for i in range(len(inputs)):
        nums = []
        sum = 0
        j = 0
        while sum < inv:
            sum += int(inputs[i+j])
            nums.append(int(inputs[i+j]))
            j += 1
        if sum == inv:
            nums.sort()
            return nums[0]+nums[-1]
    return -1


def main():
    f = open("input.txt", "r")
    inputs = f.read().split()

    print(solve_one(inputs))
    print(solve_two(inputs))


main()
