from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Link: https://leetcode.com/problems/jump-game-ii/?envType=study-plan&id=dynamic-programming-i
        You are initially positioned at `nums[0]`
        `nums[i]` is your maximum jump length at position `i`.
        Return the min number of jumps to get to the end.
        Assume you can always reach the end.
        """

        # We can use dynamic programming
        # We can track the max jump point, the prev max jump point, and total jumps
        # Every time we jump, we go through all points from the prev point
        # This way, we can just do one pass without repetition

        if len(nums) <= 1:
            return 0

        count = 1
        prev, curr = 0, nums[0]

        while curr < len(nums) - 1:
            new_max = max(nums[i] + i for i in range(prev, curr + 1))
            prev, curr = curr, new_max
            count += 1

        return count

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.jump([2, 3, 1, 1, 4]) == 2
    assert sol.jump([2, 3, 0, 1, 4]) == 2
