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


def get_next(x, y, di):
    return x + d[di][0], y + d[di][1]


G = read_input()
R, C = len(G), len(G[0])
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = 0
st = end = 0

for r in range(R):
    for c in range(C):
        if G[r][c] == '^':
            st, end = r, c

for o_r in range(R):
    for o_c in range(C):
        r, c = st, end
        di = 0
        seen = set()

        while True:
            if (r, c, di) in seen:
                ans += 1
                break
            seen.add((r, c, di))
            rr, cc = get_next(r, c, di)

            if not in_bounds(rr, cc):
                break

            if G[rr][cc] == '#' or (rr, cc) == (o_r, o_c):
                di = (di + 1) % 4
            else:
                r, c = rr, cc

print(ans)
