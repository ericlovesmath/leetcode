from typing import List


class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        """
        Link: https://leetcode.com/problems/sum-of-even-numbers-after-queries/
        """

        # Realistically we can probably just simulate it
        # We will track if the number changes parity
        # If it does, we can adjust using nums[i-1]

        prev = sum(num for num in nums if num % 2 == 0)
        ans = []

        for val, i in queries:
            if val % 2 == 0 and nums[i] % 2 == 0:
                prev += val
            elif val % 2 == 1 and nums[i] % 2 == 1:
                prev += nums[i] + val
            elif val % 2 == 1 and nums[i] % 2 == 0:
                prev -= nums[i]
            ans.append(prev)
            nums[i] += val

        return ans

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.sumEvenAfterQueries(
        [1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    ) == [8, 6, 2, 4]
    assert sol.sumEvenAfterQueries([1], [[4, 0]]) == [0]
