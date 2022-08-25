class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Link: https://leetcode.com/problems/ransom-note/
        Return if `ransomNote` can be made from `magazine`'s letters
        """

        # Track character frequency
        # randomNote should use less than magazine

        char_freq = [0 for _ in range(26)]

        for char in magazine:
            char_freq[ord(char) - ord("a")] += 1

        for char in ransomNote:
            pos = ord(char) - ord("a")
            if char_freq[pos] == 0:
                return False
            char_freq[pos] -= 1

        return True

        # Space Complexity: O(1)
        # Time Complexity: O(m+n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.canConstruct("a", "b") == False
    assert sol.canConstruct("aa", "ab") == False
    assert sol.canConstruct("aa", "aab") == True
