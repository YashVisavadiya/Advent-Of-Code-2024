from os import startfile

def read_input():
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        grid = []

        for line in lines:
            grid.append(list(line.strip()))

    return grid

def guard_walk(x, y, di):
    if not in_bounds(x, y):
        return

    dx, dy = get_next(x, y, di)

    while in_bounds(dx, dy) and G[dx][dy] in ['.', 'X']:
        x, y = dx, dy
        G[x][y] = 'X'
        dx, dy = get_next(x, y, di)


    if in_bounds(dx, dy) and G[dx][dy] == '#':
        guard_walk(x, y, (di + 1) % 4)


def in_bounds(x, y):
    return R > x >= 0 <= y < C

def get_previous(x, y, di):
    return x - d[di][0], y - d[di][1]

def get_next(x, y, di):
    return x + d[di][0], y + d[di][1]

def get_next_with_di_change(x, y, di):
    return x + d[(di + 1) % 4][0], y + d[(di + 1) % 4][1]

G = read_input()
R, C = len(G), len(G[0])
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = [0]

for r in range(R):
    for c in range(C):
        if G[r][c] == '^':
            G[r][c] = 'X'
            guard_walk(r, c, 0)

[print(''.join(row)) for row in G]
print(sum([row.count('X') for row in G]))