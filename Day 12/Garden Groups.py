from collections import deque, defaultdict


def bfs():
    Q = deque([(r, c)])
    area = 0
    perimeter = 0
    directions = defaultdict(set)

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
                directions[(dr, dc)].add((rr, cc))

    sides = 0
    for k, v in directions.items():
        sides_seen = set()
        for r2, c2 in v:
            if (r2, c2) not in sides_seen:
                sides += 1

                Q = deque([(r2, c2)])
                while Q:
                    r3, c3 = Q.popleft()
                    if (r3, c3) in sides_seen:
                        continue
                    sides_seen.add((r3, c3))
                    for dr, dc in DIRS:
                        rr, cc = r3 + dr, c3 + dc
                        if (rr, cc) in v:
                            Q.append((rr, cc))

    return area * sides


DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up right down left

ans = 0
D = open('input.txt').read().strip()

G = D.split('\n')
R = len(G)
C = len(G[0])

SEEN = set()

for r in range(R):
    for c in range(C):
        if (r, c) in SEEN:
            continue
        ans += bfs()

print(ans)
