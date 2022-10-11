from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Link: https://leetcode.com/problems/increasing-triplet-subsequence/
        return if there exists i, j, k such that nums[i] < nums[j] < nums[k]
        """

        # We want to track the minimum value so far
        # Then, we want to track the min value greater than the min val so far

        min_1 = 1 << 31
        min_2 = 1 << 31

        for num in nums:
            if min_1 < min_2 < num:
                return True
            if num <= min_1:
                min_1 = num
            elif num < min_2:
                min_2 = num

        return False

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.increasingTriplet([1, 2, 3, 4, 5]) is True
    assert sol.increasingTriplet([5, 4, 3, 2, 1]) is False
    assert sol.increasingTriplet([2, 1, 5, 0, 4, 6]) is True

    assert sol.increasingTriplet([1, 1, -2, 6]) is False
