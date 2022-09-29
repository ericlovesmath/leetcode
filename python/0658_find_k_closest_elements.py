from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        Link: https://leetcode.com/problems/find-k-closest-elements/description/
        Given sorted arr, return the k closest elements to the value x
        """

        # First, we want to do binary search to get the position of x in arr
        # Then, we can check left and right from there to get the next k vals

        l, r = 0, len(arr) - k

        while l < r:
            mid = l + ((r - l) // 2)
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid

        return arr[l : l + k]

        # Space Complexity: O(1)
        # Time Complexity: O(log(n-k) + k)


if __name__ == "__main__":
    sol = Solution()

    assert sol.findClosestElements([1, 2, 3, 4, 5], 3, 3) == [2, 3, 4]
    assert sol.findClosestElements([1, 2, 3, 4, 5, 6, 7, 8], 1, 3) == [3]
    assert sol.findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
    assert sol.findClosestElements([1, 2, 3, 4, 5], 4, 6) == [2, 3, 4, 5]
    assert sol.findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
