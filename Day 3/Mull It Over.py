import re


class Solution:
    def solve(self) -> int:
        queries = self.read_input()
        ans = 0

        enabled = True
        for query in queries:
            matches = list(re.findall(r"mul\((\d+),(\d+)\)|(do\(\)|don't\(\))", query))
            print(matches)
            for a, b, do_or_dont in matches:
                if do_or_dont == "" and enabled:
                    ans += int(a) * int(b)
                else:
                    if do_or_dont == "do()":
                        enabled = True
                    else:
                        enabled = False

        return ans

    def read_input(self):
        with open("input.txt", "r") as f:
            lines = f.readlines()
            queries = []
            for line in lines:
                queries.append(line.strip())  # added strip() to remove newline characters
        return queries


sol = Solution()
print(sol.solve())
