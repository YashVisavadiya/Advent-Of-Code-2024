from collections import defaultdict

from sortedcontainers import SortedDict


def read_input():
    with open('input.txt', 'r') as f:
        disk = f.read().strip()
        d = []
        file_map = SortedDict(int)
        free_map = SortedDict(int)
        c = 0
        for i, ch in enumerate(disk):
            n = int(ch)
            if i % 2 == 0:
                file_map[c] = n
                d.extend([i // 2 for _ in range(n)])
            else:
                free_map[c] = n
                d.extend(['.' for _ in range(n)])
            c += n
        return d, file_map, free_map


def get_free_space(i):
    free_space = 1
    while i < N and D[i] == '.':
        free_space += 1
        i += 1
    return free_space


def get_file_size(j):
    file_size = 1
    while j >= 0 and D[j] == D[j - 1]:
        file_size += 1
        j -= 1
    return file_size


D, fm, frm = read_input()
N = len(D)

for i, si in reversed(fm.items()):
    for j, sj in frm.items():
        if sj >= si and i > j:
            v = D[i]
            for k in range(si):
                D[j + k] = v
                D[i + k] = '.'
            del frm[j]
            frm[j + si] = sj - si
            break


ans = 0
for ind, ch in enumerate(D):
    if ch != '.':
        ans += ind * int(ch)

print(ans)
