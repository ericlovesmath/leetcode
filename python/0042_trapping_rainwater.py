from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        water = 0
        while l < r:
            if height[l] < height[r] and l < r:
                curr = height[l]
                while height[l] <= curr:
                    water += curr - height[l]
                    l += 1
            else:
                curr = height[r]
                while height[r] <= curr and l < r:
                    water += curr - height[r]
                    r -= 1
        return water
