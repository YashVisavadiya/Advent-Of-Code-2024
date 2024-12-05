from collections import defaultdict
from functools import cmp_to_key


def read_input() -> (list[list[int]], list[list[int]]):
    with open("input.txt", "r") as f:
        lines = f.readlines()
        si = lines.index('\n')
        a = []
        b = []

        for line in lines[:si]:
            row = map(int, line.strip().split('|'))
            a.append(row)

        for line in lines[si + 1:]:
            row = list(map(int, line.strip().split(',')))
            b.append(row)

    return a, b

def is_valid_update(update):
    previous_pages = set()
    is_valid = True

    for i in range(1, len(update)):
        page_rule = order_rule[update[i]]
        previous_pages.add(update[i - 1])

        for page in previous_pages:
            if page not in page_rule:
                is_valid = False
                break

        if not is_valid:
            break
    return is_valid


def cmp(a, b):
    if b not in order_rule[a]:
        return -1
    return 1

ans = 0
rules, updates = read_input()
order_rule = defaultdict(set)

invalid_updates = []

for a, b in rules:
    order_rule[b].add(a)

for update in updates:
    if not is_valid_update(update):
        invalid_updates.append(update)

for update in invalid_updates:
    sorted_update = sorted(update, key=cmp_to_key(cmp))
    ans += sorted_update[len(sorted_update) // 2]

print(ans)
