from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False

        part_sum = total // 3
        split_first = False
        cumn = 0
        for i in range(len(arr)):
            cumn += arr[i]
            if split_first and cumn == 2 * part_sum:
                return i != len(arr) - 1
            if cumn == part_sum:
                split_first = True
        return False
