from collections import defaultdict
from itertools import combinations


def read_input():
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        grid = []

        for line in lines:
            row = list(line.strip())
            grid.append(row)

    return grid


def in_bounds(x, y):
    return R > x >= 0 <= y < C


def find_antinodes(x, y, dx, dy):
    while in_bounds(x, y):
        if G[x][y] == '.':
            G[x][y] = '#'
        s.add((x, y))
        x, y = x + dx, y + dy


G = read_input()
p = defaultdict(list)
R, C = map(len, (G, G[0]))
s = set()

for i in range(0, len(G)):
    for j in range(0, len(G[i])):
        if G[i][j] != '.':
            p[G[i][j]].append((i, j))

for k, v in p.items():
    for (x1, y1), (x2, y2) in combinations(v, 2):
        dx, dy = x1 - x2, y1 - y2

        find_antinodes(x1, y1, dx, dy)
        find_antinodes(x2, y2, -dx, -dy)

print('\n'.join([''.join(row) for row in G]))
print(len(s))