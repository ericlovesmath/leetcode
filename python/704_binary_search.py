class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Link: https://leetcode.com/problems/binary-search/
        Given sorted integers `nums`, return the index of `target`.
        Otherwise, return -1.
        Algorithm must run at O(log n)
        All numbers are unique.
        """

        # Use Binary Search

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

        # Space Complexity: O(1)
        # Time Complexity: O(log n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert sol.search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert sol.search([5], 5) == 0
