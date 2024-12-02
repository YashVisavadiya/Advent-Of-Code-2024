from collections import defaultdict


class Solution:
    def safe_reports(self) -> int:
        reports = self.read_input()

        safe_reports_count = 0

        for report in reports:
            if self.is_safe_report(report):
                safe_reports_count += 1

        return safe_reports_count

    def is_safe_report(self, report):
        prev = report[0]
        inc_or_dec = report == sorted(report) or report == sorted(report, reverse=True)

        if not inc_or_dec:
            return False

        for curr in report[1:]:
            if not (1 <= abs(curr - prev) <= 3):
                return False
            prev = curr

        return True

    def safe_reports_with_tolerating_one_bad_level(self) -> int:
        reports = self.read_input()

        safe_reports_count = 0
        for report in reports:
            is_safe_report = self.is_safe_report(report)

            for i in range(0, len(report) - 1):
                diff1 = report[i + 1] - report[i]
                if not (1 <= abs(diff1) <= 3):
                    is_safe_report |= self.is_safe_report(report[:i] + report[i + 1:])
                    is_safe_report |= self.is_safe_report(report[:i + 1] + report[i + 2:])
                    break

                if i + 2 < len(report):
                    diff2 = report[i + 2] - report[i + 1]
                    if (diff1 > 0) != (diff2 > 0):
                        is_safe_report |= self.is_safe_report(report[:i] + report[i + 1:])
                        is_safe_report |= self.is_safe_report(report[:i + 1] + report[i + 2:])
                        is_safe_report |= self.is_safe_report(report[:i + 2] + report[i + 3:])
                        break

            if is_safe_report:
                safe_reports_count += 1

        return safe_reports_count

    def read_input(self) -> list[list[int]]:
        with open('input.txt', 'r') as file:
            lines = file.readlines()

            reports = []
            for line in lines:
                report = list(map(int, line.strip().split()))
                reports.append(report)

            return reports


sol = Solution()
total_distance = sol.safe_reports()
print(total_distance)

similarity_score = sol.safe_reports_with_tolerating_one_bad_level()
print(similarity_score)
