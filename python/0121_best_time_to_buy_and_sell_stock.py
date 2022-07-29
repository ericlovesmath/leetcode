from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
        Given `prices` where `prices[i]` is the price of a stock on day `i`.
        Choose a day to buy and a later day to sell.
        Return the maximum possible profit.
        If you can't profit, return 0.
        There is at least one price in `prices`.
        """

        min_buy = prices[0]
        max_profit = 0

        for price in prices[1:]:
            max_profit = max(price - min_buy, max_profit)
            min_buy = min(min_buy, price)

        return max_profit

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([7]) == 0
