class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
        Return the length of the longest substring without repeating characters.
        """

        # The general idea is that its a window with 2 pointers
        # We can push the right pointer forward until it can't
        # Then, we can push the left pointer forward until we can push the right again
        # We can track the hash constantly with a set

        window = set()
        back = 0
        max_width = 0

        for front in range(0, len(s)):
            while s[front] in window:
                window.remove(s[back])
                back += 1
            max_width = max(max_width, front - back + 1)
            window.add(s[front])

        return max_width

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("w") == 1
    assert sol.lengthOfLongestSubstring("") == 0
