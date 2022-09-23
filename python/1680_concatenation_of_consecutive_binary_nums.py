class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        Link: https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
        Concat the binary forms of 1 to n, return that mod 10^9 + 7
        """

        # We can just simulate it

        MAX = 10 ** 9 + 7

        ans = 0
        for i in range(1, n+1):
            ans = ((ans << i.bit_length()) + i) % MAX

        return ans

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.concatenatedBinary(1) == 1
    assert sol.concatenatedBinary(3) == 27
    assert sol.concatenatedBinary(12) == 505379714
