from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Link: https://leetcode.com/problems/house-robber/
        `nums` represents the money in each house.
        You cannot rob consecutive houses.
        The houses are in a circle
        Return the maximum amount of money you can rob.
        """

        # See 0198_house_robber.py for non-circle explanation
        # This is just house robber, except you run it twice
        # First for when you ignore house 0, second for house -1

        if len(nums) <= 2:
            return max(nums)
        return max(self.house_robber(nums[1:]), self.house_robber(nums[:-1]))

    def house_robber(self, nums: List[int]) -> int:
        """From 0198_house_robber.py"""

        prev, curr = nums[0], max(nums[:2])
        for i in range(2, len(nums)):
            prev, curr = curr, max(nums[i] + prev, curr)
        return curr


if __name__ == "__main__":
    sol = Solution()

    assert sol.rob([0]) == 0
    assert sol.rob([5, 6]) == 6
    assert sol.rob([2,3,2]) == 3
    assert sol.rob([1,2,3,1]) == 4
    assert sol.rob([1,2,3]) == 3
