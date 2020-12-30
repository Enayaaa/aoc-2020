import math

class Seat:
    def __init__(self, code):
        self.row=decode(code,0,127,"F","B")
        self.col=decode(code,0,7,"L","R")
        self.id=get_id(code)

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
    seats = []

    for i in inputs:
        seat = Seat(i)
        seats.append(seat)
    
    rows=[["O","O","O","O","O","O","O","O"] for x in range(128)]
    for i in range(len(seats)):
        rows[seats[i].row][seats[i].col] = "X"
    
    for row in range(len(rows)):
        for col in range(len(rows[0])):
            if rows[row][col]=="O" and rows[row][col-1]=="X" and rows[row][col+1]=="X":
                print(row*8+ col)
    
main()