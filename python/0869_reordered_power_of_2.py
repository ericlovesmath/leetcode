from collections import Counter


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        """
        Link: https://leetcode.com/problems/reordered-power-of-2/
        Return if the digits of `n` can be reordered to be a power of 2
        """

        hash_n = Counter(str(n))
        for i in range(30):
            if Counter(str(1 << i)) == hash_n:
                return True
        return False

        # Space Complexity: O(1)
        # Time Complexity: O(1)


if __name__ == "__main__":
    sol = Solution()

    assert sol.reorderedPowerOf2(1) == True
    assert sol.reorderedPowerOf2(10) == False
