from collections import defaultdict


def read_input():
    with open("input.txt", 'r') as file:
        lines = file.readlines()
        r = defaultdict(list)

        for line in lines:
            k, v = line.split(':')
            r[int(k.strip())] = list(map(int, v.strip().split()))

    return r


def dfs(index: int, values: list[int], s: int, tar: int):
    if index == len(values):
        if s == tar:
            return True
        return False

    return (dfs(index + 1, values, s + values[index], tar)
            | dfs(index + 1, values, s * values[index], tar)
            | dfs(index + 1, values, calc_3rd_op(s, values[index]), tar))


def calc_3rd_op(a: int, b: int):
    return (a * (10 ** len(str(b)))) + b


m = read_input()
ans = 0

for k, v in m.items():
    if dfs(1, v, v[0], k):
        ans += k

print(ans)
