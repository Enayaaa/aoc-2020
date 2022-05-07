import math

def decode(code, lower, upper, lo_code, up_code):
    for c in code:
        if c == lo_code:
            upper -= math.ceil((upper-lower)/2)
        if c == up_code:
            lower += math.ceil((upper-lower)/2)
    return lower

def get_id(code):
    row = decode(code,0,127,"F","B")
    col = decode(code,0,7,"L", "R")
    return row*8+col

def main():
    f = open("input.txt", "r")
    inputs = f.read().split()

    highest_id = 0
    for i in inputs:
        id = get_id(i)
        if id > highest_id:
            highest_id=id
    print(highest_id)

main()