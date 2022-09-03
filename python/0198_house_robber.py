from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Link: https://leetcode.com/problems/house-robber/
        `nums` represents the money in each house.
        You cannot rob consecutive houses.
        Return the maximum amount of money you can rob.
        """

        # The problem can be represented recursively
        # We can probably translate this to bottom-up DP
        # rob_to(n) = max(rob_to(n-1), nums[n-1] + rob_to(n-2))
        # rob_to(0) = nums[0], rob_to(1) = max(nums[0], nums[1])

        rob_to = [-1 for _ in range(len(nums))]
        rob_to[0] = nums[0]
        rob_to[1] = max(nums[:2])

        for i in range(2, len(nums)):
            rob_to[i] = max(nums[i] + rob_to[i - 2], rob_to[i-1])

        return rob_to[-1]

        # Space Complexity: O(n)
        # Time Complexity: O(n)

        # Building on this DP Solution,
        # we notice we just need to track the last two vals
        # We can save space to O(1) like so

        prev, curr = nums[0], max(nums[:2])
        for i in range(2, len(nums)):
            prev, curr = curr, max(nums[i] + prev, curr)
        return curr


if __name__ == "__main__":
    sol = Solution()

    assert sol.rob([1, 2]) == 2
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([2, 7, 9, 3, 1]) == 12
