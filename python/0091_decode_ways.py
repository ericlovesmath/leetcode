class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Link: https://leetcode.com/problems/decode-ways/
        Chars "A"-"Z" can be mapped to strings "1"-"26".
        Given a string of digits, return how many combinations of 
        alphabetic characters could have resulted in the string.
        """

        # This looks like a dynamic programming problem.

        if s[0] == "0":
            return 0
        
        combos = [0 for _ in range(len(s))]
        combos[0] = 1

        for i in range(1, len(s)):
            if s[i] != "0":
                combos[i] += combos[i-1]
            if s[i-1] == "1" or (s[i-1] == "2" and s[i] <= "6"):
                combos[i] += combos[i-2 if i > 1 else 0]

        return combos[-1]

        # Space Complexity: O(n)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.numDecodings("12") == 2
    assert sol.numDecodings("226") == 3
    assert sol.numDecodings("06") == 0
    assert sol.numDecodings("9849859876379786") == 1
