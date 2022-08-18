from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Link: https://leetcode.com/problems/coin-change/
        Return the fewest number of coins that you need to make up that amount.
        If that amount of money cannot be made up by any combination, return -1.
        """

        # Use Bottom-Up DP
        # For each index, we will track the minimum amount required
        # to get to that index

        MAX_VAL = amount + 1
        counts = [MAX_VAL for _ in range(amount + 1)]
        counts[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i + coin <= amount:
                    counts[i + coin] = min(counts[i + coin], counts[i] + 1)

        if counts[amount] == MAX_VAL:
            return -1

        return counts[amount]

        # Space Complexity: O(n)
        # Time Complexity: O(n*m)


if __name__ == "__main__":
    sol = Solution()

    assert sol.coinChange([1, 2, 5], 11) == 3
    assert sol.coinChange([2], 3) == -1
    assert sol.coinChange([1], 0) == 0
