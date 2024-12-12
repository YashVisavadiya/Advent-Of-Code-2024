from collections import deque


def read_input():
    with open('input.txt', 'r', encoding='utf-8-sig') as f:
        data = f.readlines()

        return [list(line.strip()) for line in data]


def bfs(i, j):
    plant = G[i][j]
    queue = deque([(i, j)])
    cnt = 0
    s = {(i, j)}
    unq = {(i, j, -1)}
    
    while queue:
        i, j = queue.popleft()
        visited[i][j] = True

        for ind, (dr, dc) in enumerate([(0, 1), (0, -1), (1, 0), (-1, 0)]):
            nr, nc = i + dr, j + dc

            if in_bounds(nr, nc) and G[nr][nc] == plant:
                if (nr, nc, ind) not in unq:
                    cnt += 1
                    unq.add((nr, nc, ind))
                if not visited[nr][nc]: 
                    queue.append((nr, nc))
                s.add((nr, nc))
                # cnt += 1
                visited[nr][nc] = True
    
    return len(s), cnt


def in_bounds(i, j):
    return R > i >= 0 <= j < C


G = read_input()
R, C = map(len, [G, G[0]])
visited = [[False] * C for _ in range(R)]
ans = 0

for r in range(R):
    for c in range(C):
        if not visited[r][c]:
            plants, overlap = bfs(r, c)
            # print(G[r][c], plants, overlap)
            ans += plants * ((plants * 4) - overlap)

print(ans)
