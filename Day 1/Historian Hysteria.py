from collections import defaultdict


class Solution:
    def total_distance(self) -> int:
        group_a, group_b = self.read_input()

        group_a.sort()
        group_b.sort()

        return sum(abs(a - b) for a, b in zip(group_a, group_b))


    def similarity_score(self) -> int:
        group_a, group_b = self.read_input()

        score = 0
        freq_counter_for_group_b = defaultdict(int)

        for b in group_b:
            freq_counter_for_group_b[b] += 1

        for a in group_a:
            score += freq_counter_for_group_b[a] * a

        return score


    def read_input(self)-> (list[int], list[int]):
        with open('input.txt', 'r') as file:
            group_a = []
            group_b = []
            lines = file.readlines()

            for line in lines:
                a, b = map(int, line.strip().split())
                group_a.append(a)
                group_b.append(b)

            return group_a, group_b


sol = Solution()
total_distance = sol.total_distance()
print(total_distance)

similarity_score = sol.similarity_score()
print(similarity_score)

