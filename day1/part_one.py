file = open("input.txt", "r")
nums = []

def main():
    for line in file:
        nums.append(int(line))

    print(solve(nums))

def solve(nums):
    for x in nums:
        for y in nums:
            if(x+y==2020):
                print(x,y)
                return x*y
    return 0

main()