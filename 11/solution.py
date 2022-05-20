# (.) floor
# (L) empty seat
# (#) occupied seat

# if (L) AND no (#) adjacent to it          -> becomes (#)
# if (#) AND four or more adjacent also (#) -> (L)
# otherwise no change

import copy


def print_map(map):
    [print("".join(x)) for x in map]


def count_neighbours(state, r, c, k):
    rows = len(state)
    cols = len(state[0])
    neighs = filter(
        lambda p: 0 <= p[0] < rows and 0 <= p[1] < cols,
        [
            (r - 1, c - 1),
            (r - 1, c),
            (r - 1, c + 1),
            (r, c - 1),
            (r, c + 1),
            (r + 1, c - 1),
            (r + 1, c),
            (r + 1, c + 1),
        ],
    )
    res = [state[p[0]][p[1]] for p in neighs]
    return res.count(k)


def solve_one(state):
    while True:
        new_state = copy.deepcopy(state)
        for r, xs in enumerate(state):
            for c, x in enumerate(xs):
                if x == "L" and count_neighbours(state, r, c, "#") == 0:
                    new_state[r][c] = "#"
                elif x == "#" and count_neighbours(state, r, c, "#") >= 4:
                    new_state[r][c] = "L"
        if new_state == state:
            break
        state = new_state
    return sum(x.count("#") for x in state)


def ray(w, h, r, c, offset_r, offset_c):
    while 0 <= r + offset_r < h and 0 <= c + offset_c < w:
        r += offset_r
        c += offset_c
        yield r, c


def count_visible(state, r, c, k):
    w = len(state[0])
    h = len(state)
    offsets = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]
    visible = []
    for offset_r, offset_c in offsets:
        for (r_new, c_new) in ray(w, h, r, c, offset_r, offset_c):
            if state[r_new][c_new] in "#L":
                visible.append(state[r_new][c_new])
                break
    return visible.count(k)


def solve_two(state):
    while True:
        new_state = copy.deepcopy(state)
        for r, xs in enumerate(state):
            for c, x in enumerate(xs):
                if x == "L" and count_visible(state, r, c, "#") == 0:
                    new_state[r][c] = "#"
                elif x == "#" and count_visible(state, r, c, "#") >= 5:
                    new_state[r][c] = "L"
        if new_state == state:
            break
        state = new_state
    return sum(x.count("#") for x in state)


def main():
    with open("input.in", "r") as f:
        inp = list(map(list, f.read().splitlines()))
    print(solve_one(inp))
    print(solve_two(inp))


if __name__ == "__main__":
    main()
