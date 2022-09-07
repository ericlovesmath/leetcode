from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Link: https://leetcode.com/problems/jump-game/?envType=study-plan&id=dynamic-programming-i
        You are initially positioned at `nums[0]`
        `nums[i]` is your maximum jump length at position `i`.
        Return true if you can reach the last index, or false otherwise.
        """

        # We can use dynamic programming
        # We will keep an array to see if you can jump to arr[i]
        # If you can, you can mark that you can get to position i
        # Repeat until you get to the last position

        max_distance = 0

        for i in range(len(nums)):
            if i > max_distance:
                return False
            max_distance = max(nums[i] + i, max_distance)

        return True

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.canJump([0]) is True
    assert sol.canJump([2, 3, 1, 1, 4]) is True
    assert sol.canJump([3, 2, 1, 0, 4]) is False
