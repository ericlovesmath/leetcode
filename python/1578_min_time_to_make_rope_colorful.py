from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        Link: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
        There are n ballons, where colors[i] is the color of the ith balloon.
        Alice doesn't want consecutive colors.
        Removing ballon_i takes neededTime[i] seconds.
        Return the minimum time needed to make the rope colorful.
        """

        # We essentially want to get each "group" of consecutive balloons
        # From each group len x, we want to remove the fastest x-1 balloons

        curr_color = ""
        group_total = 0
        group_max = 0
        total_time = 0

        for i in range(len(colors)):
            if curr_color != colors[i]:
                total_time += group_total - group_max
                curr_color = colors[i]
                group_total, group_max = 0, 0
            group_total += neededTime[i]
            group_max = max(group_max, neededTime[i])

        total_time += group_total - group_max

        return total_time

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.minCost("abaac", [1, 2, 3, 4, 5]) == 3
    assert sol.minCost("abc", [1, 2, 3]) == 0
    assert sol.minCost("aabaa", [1, 2, 3, 4, 1]) == 2
