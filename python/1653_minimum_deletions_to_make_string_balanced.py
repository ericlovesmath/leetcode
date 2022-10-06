class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        Link: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
        `s` is a string with only "a" and "b" characters.
        Return the min number of deletions needed to have no "a"s on the right of any "b"
        """

        # Naively, we can check each "center position"
        # At each center position, count "b"s on left and "a"s on right
        # However this would be O(n^2)
        # We can just update the count based on the current pos
        # This would require only 1 iteration

        # Goal is to minimize b + a needed

        b, a = 0, s.count("a")
        min_diff = a
        for char in s:
            if char == "b":
                b += 1
            else:
                a -= 1
                min_diff = min(min_diff, a + b)

        return min_diff

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.minimumDeletions("aababbab") == 2
    assert sol.minimumDeletions("bbaaaaabb") == 2
    assert sol.minimumDeletions("bbabbbbbababbbbbabab") == 5
    assert sol.minimumDeletions("aaaabaabaaaababbaaaa") == 5
