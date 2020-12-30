
def main():
    f = open("input.txt", "r")
    biome = []
    for i in f:
        biome.append(i.strip("\n"))
    length = len(biome[0])

    trees = 0
    index = 0
    row = 0
    while row < len(biome) - 1:
        index = (index + 3) % length
        row += 1
        if biome[row][index] == "#":
            trees += 1
    print(trees)
        
main()