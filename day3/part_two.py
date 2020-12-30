traverses = [[1, 3, 5, 7, 1], [1, 1, 1, 1, 2]]


def main():
    f = open("input1.txt", "r")
    biome = []
    for i in f:
        biome.append(i.strip("\n"))
    length = len(biome[0])

    product = 1
    for i in range(len(traverses[0])):
        trees = 0
        index = 0
        row = 0
        while row < len(biome) - 1:
            index = (index + traverses[0][i]) % length
            row += traverses[1][i]
            if biome[row][index] == "#":
                trees += 1
        product *= trees
        print(trees)
    print("product:", product)


main()
