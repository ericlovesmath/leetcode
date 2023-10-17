from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = []
        for i in range(1 << len(nums)):
            next = []
            j = 0
            while i > 0:
                if i & 1:
                    next.append(nums[j])
                j += 1
                i >>= 1
            subs.append(next)
        return subs
