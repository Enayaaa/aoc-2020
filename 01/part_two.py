file = open("input.txt", "r")
nums = []

def main():
    for line in file:
        nums.append(int(line))

    print(solve(nums))

def solve(nums):
    for x in nums:
        for y in nums:
            for z in nums:
                if(x+y+z==2020):
                    print(x,y,z)
                    return x*y*z
    return 0

main()