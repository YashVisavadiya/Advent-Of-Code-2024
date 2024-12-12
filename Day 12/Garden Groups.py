from collections import deque


def bfs():
    Q = deque([(r, c)])
    area = 0
    perimeter = 0

    while Q:
        r2, c2 = Q.popleft()
        if (r2, c2) in SEEN:
            continue
        SEEN.add((r2, c2))
        area += 1

        for dr, dc in DIRS:
            rr = r2 + dr
            cc = c2 + dc
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == G[r2][c2]:
                Q.append((rr, cc))
            else:
                perimeter += 1
    return area * perimeter


DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up right down left

p1 = 0
D = open('input.txt').read().strip()

G = D.split('\n')
R = len(G)
C = len(G[0])

SEEN = set()

for r in range(R):
    for c in range(C):
        if (r, c) in SEEN:
            continue
        p1 += bfs()

print(p1)
