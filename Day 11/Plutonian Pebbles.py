from functools import cache


def read_input() -> list[int]:
    with open('input.txt', 'r', encoding='utf-8-sig') as f:
        data = f.readlines()[0].strip()
    return list(map(int, data.split()))

@cache
def solve(stone: int, it: int) -> int:
    if it == 0:
        return 1
    s = str(stone)
    l = len(s)
    if stone == 0:
        return solve(1, it - 1)
    if len(s) % 2 == 0:
        return solve(int(s[:l // 2]), it - 1) + solve(int(s[l // 2:]), it - 1)
    else:
        return solve(stone * 2024, it - 1)

S = read_input()
iterations = 75
ans = 0

for stone in S:
    ans += solve(stone, iterations)

print(ans)