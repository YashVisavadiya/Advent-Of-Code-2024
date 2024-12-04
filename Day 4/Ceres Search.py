def read_input():
    with open("input.txt", "r") as f:
        lines = f.readlines()
        grid = []

        for line in lines:
            row = list(line.strip())
            grid.append(row)

    return grid


def match_counts_1(x, y):
    counts = 0

    # right
    if y + 3 < C and G[x][y] == 'X' and G[x][y + 1] == 'M' and G[x][y + 2] == 'A' and G[x][y + 3] == 'S':
        counts += 1
    # down
    if x + 3 < R and G[x][y] == 'X' and G[x + 1][y] == 'M' and G[x + 2][y] == 'A' and G[x + 3][y] == 'S':
        counts += 1
    # down right
    if x + 3 < R and y + 3 < C and G[x][y] == 'X' and G[x + 1][y + 1] == 'M' and G[x + 2][y + 2] == 'A' and G[x + 3][y + 3] == 'S':
        counts += 1
    # left
    if y + 3 < R and G[x][y] == 'S' and G[x][y + 1] == 'A' and G[x][y + 2] == 'M' and G[x][y + 3] == 'X':
        counts += 1
    # up
    if x + 3 < R and G[x][y] == 'S' and G[x + 1][y] == 'A' and G[x + 2][y] == 'M' and G[x + 3][y] == 'X':
        counts += 1
    # up left
    if x + 3 < R and y + 3 < C and G[x][y] == 'S' and G[x + 1][y + 1] == 'A' and G[x + 2][y + 2] == 'M' and G[x + 3][y + 3] == 'X':
        counts += 1
    # down left
    if x + 3 < R and y - 3 >= 0 and G[x][y] == 'X' and G[x + 1][y - 1] == 'M' and G[x + 2][y - 2] == 'A' and G[x + 3][y - 3] == 'S':
        counts += 1
    # up right
    if x + 3 < R and y - 3 >= 0 and G[x][y] == 'S' and G[x + 1][y - 1] == 'A' and G[x + 2][y - 2] == 'M' and G[x + 3][y - 3] == 'X':
        counts += 1

    return counts


def match_counts_2(x, y):
    if G[x][y] != "A":
        return 0

    counts = 0

    if x - 1 >= 0 and y - 1 >= 0 and x + 1 < R and y + 1 < C:
        if G[x + 1][y + 1] == G[x - 1][y + 1] == 'S' and G[x + 1][y - 1] == G[x - 1][y - 1] == 'M':
            counts += 1
        if G[x + 1][y + 1] == G[x - 1][y + 1] == 'M' and G[x + 1][y - 1] == G[x - 1][y - 1] == 'S':
            counts += 1
        if G[x + 1][y + 1] == G[x + 1][y - 1] == 'S' and G[x - 1][y + 1] == G[x - 1][y - 1] == 'M':
            counts += 1
        if G[x + 1][y + 1] == G[x + 1][y - 1] == 'M' and G[x - 1][y + 1] == G[x - 1][y - 1] == 'S':
            counts += 1

    return counts


G = read_input()
R, C = map(len, (G, G[0]))

ans = 0
for row in range(R):
    for col in range(C):
        ans += match_counts_2(row, col)

print(ans)