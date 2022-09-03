from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Link: https://leetcode.com/problems/min-cost-climbing-stairs/
        `cost[i]` is the cost to step on the ith step.
        You can climb one or two steps at a time.
        Return the min cost to reach the top floor.
        """

        # Use bottom-up DP
        # p(i) = p(i) + min(p(i-1), p(i-2))
        # We can make another array if language copies by reference

        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])

        # We can stop at the last or second to last step
        return min(cost[-1], cost[-2])

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.minCostClimbingStairs([10, 15, 20]) == 15
    assert sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
