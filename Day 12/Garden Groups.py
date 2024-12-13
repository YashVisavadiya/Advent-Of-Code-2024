from collections import deque, defaultdict


def read_input():
    with open('input.txt') as f:
        return f.read().strip().split('\n')


def dfs(i, j, plant, node):
    if i in range(R) and j in range(C):
        if (i, j) in cc:
            return
        if G[i][j] == plant:
            cc[i, j] = node
            for dr, dc in DIRS:
                dfs(i + dr, j + dc, plant, node)


DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up right down left

ans = 0
G = read_input()
R = len(G)
C = len(G[0])

cc = {}
part1 = part2 = 0

node = 0
for r in range(R):
    for c in range(C):
        if (r, c) not in cc:
            dfs(r, c, G[r][c], node)
            node += 1

ccr = defaultdict(set)
for k, v in cc.items():
    ccr[v].add(k)

for nodes in ccr.values():
    area = len(nodes)
    per1 = set()

    for x, y in nodes:
        for dx, dy in DIRS:
            if x not in range(R) or y not in range(C) or (x + dx, y + dy) not in nodes:
                per1.add(((x, y), (x + dx, y + dy)))

    per2 = set()

    for p1, p2 in per1:
        keep = True
        for dx, dy in [(0, 1), (1, 0)]:
            n1 = (p1[0] + dx, p1[1] + dy)
            n2 = (p2[0] + dx, p2[1] + dy)
            if (n1, n2) in per1:
                keep = False
        if keep:
            per2.add((p1, p2))

    part1 += area * len(per1)
    part2 += area * len(per2)

print(part1)
print(part2)
