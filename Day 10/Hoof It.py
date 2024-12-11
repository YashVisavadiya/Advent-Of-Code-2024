from collections import defaultdict


def read_input():
    with open('input.txt', 'r', encoding='utf-8-sig') as f:
        data = f.readlines()
        grid = []

        for line in data:
            grid.append(list(line.strip()))

        return grid


def try_to_reach_end(x, y, visited):
    if not in_bounds(x, y):
        return

    if G[x][y] == '9':
        # print('Reached end', x, y)
        visited.add((x, y))
        return {(x, y)}
    
    if (x, y) not in visited and (x, y) in M:
        # print('Cycle detected', x, y)
        return M[(x, y)]
    
    counts = set()
    visited.add((x, y))
    
    if (x, y) in M:
        return M[(x, y)]
    
    for dx, dy in D:
        if is_next_valid(x, y, dx, dy):
            counts = counts.union(try_to_reach_end(x + dx, y + dy, visited))
    
    M[(x,y)] = M[(x, y)].union(counts)
    return counts

def is_next_valid(x, y, dx, dy):
    return in_bounds(x + dx, y + dy) and int(G[x + dx][y + dy]) == int(G[x][y]) + 1


def in_bounds(x, y):
    return R > x >= 0 <= y < C


def print_grid(grid):
    for row in grid:
        print(row)


G = read_input()
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
R, C = map(len, (G, G[0]))

M = defaultdict(set)

# print_grid(G)
sp = []

for r in range(R):
    for c in range(C):
        if G[r][c] == '0':
            sp.append((r, c))

ret = 0
for r, c in sp:
    # print('start', r,c)
    d = try_to_reach_end(r, c, set())
    
    ret += len(d)
    # print('for r, c', r, c, d)
    # break

# print_grid(V)
print(ret)