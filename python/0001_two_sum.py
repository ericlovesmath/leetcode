from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Link: https://leetcode.com/problems/two-sum/
        Return the indicies of two numbers that add up to `target`.
        You may assume that each input would have exactly one solution.
        You may not use the same element twice.
        """

        # Hash map of value to right most index
        index_map = {num: i for i, num in enumerate(nums)}

        # See if `target - num` exists on `index_map`
        for i, num in enumerate(nums):
            other = target - num
            if other in index_map and index_map[other] != i:
                return [i, index_map[other]]

        raise RuntimeError("Solution::twoSum failed to find solution")

        # Space Complexity: O(n) for hash map
        # Time Complexity: O(n) to iterate through list twice


if __name__ == "__main__":
    sol = Solution()

    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    assert sol.twoSum([3, 3], 6) == [0, 1]
