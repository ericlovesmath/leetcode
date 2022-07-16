class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Link: https://leetcode.com/problems/valid-anagram/
        Return if `s` and `t` are anagrams.
        Works even with unicode characters.
        """

        # Pythonic short equivalent:
        # return collections.Counter(s) == collections.Counter(t)

        # They are anagrams if their character count is the same

        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Remove from map
        for char in t:
            if char in char_count:
                char_count[char] -= 1
            else:
                return False

        # Verify map is empty
        return all(count == 0 for count in char_count.values())

        # Space Complexity: O(n)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False
