from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """
        Link: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
        Return the maximum area of a piece of cake after you cut
        at each horizontal and vertical position provided in the arrays
        horizontalCuts and verticalCuts. Since the answer can be a large
        number, return this modulo 10^9 + 7.
        """
        
        # We treat horizontal/vertical separately
        # We want to maximize the gaps
        # Go through each gap to find the max
        
        horizontalCuts.sort()
        verticalCuts.sort()

        # Can instead append 0 and h at the front and end for simpler code
        max_hori = max(horizontalCuts[0], h - horizontalCuts[-1])
        max_vert = max(verticalCuts[0], w - verticalCuts[-1])
        
        # Would be faster as list comprehension but less readable
        for i in range(len(horizontalCuts) - 1):
            max_hori = max(max_hori, horizontalCuts[i + 1] - horizontalCuts[i])
        for i in range(len(verticalCuts) - 1):
            max_vert = max(max_vert, verticalCuts[i + 1] - verticalCuts[i])

        return (max_hori * max_vert) % (10 ** 9 + 7)

        # Space Complexity: O(1)
        # Time Complexity: O(n + m)


if __name__ == "__main__":
    sol = Solution()

    assert sol.maxArea(5, 4, [1, 2, 4], [1, 3]) == 4
    assert sol.maxArea(5, 4, [3, 1], [1]) == 6
    assert sol.maxArea(5, 4, [3], [3]) == 9
