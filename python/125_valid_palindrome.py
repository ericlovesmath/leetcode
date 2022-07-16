class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Link: https://leetcode.com/problems/valid-palindrome/
        Determine if `s` is a palindrome.
        A palindrome must be the same read forwards and backwards.
        Ignore cases, only read alphanumeric chars.
        """

        # Keep a front and back pointer
        # Identify if they differ, stop when they meet

        # Pythonic, shorter solution:
        # chars = [c.lower() for c in s if c.isalnum()]
        # return chars == chars[::-1]
        # This solution uses O(n) space and is not faster in other languages
        # This is abusing underlying c libraries

        front = 0
        back = len(s) - 1

        while front < back:

            while front < back and not s[front].isalnum():
                front += 1

            while front < back and not s[back].isalnum():
                back -= 1

            if s[front].lower() != s[back].lower():
                return False

            front += 1
            back -= 1

        return True

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.isPalindrome("A man, a plan, a canal: Panama") is True
    assert sol.isPalindrome("race a car") is False
    assert sol.isPalindrome(" ") is True
    assert sol.isPalindrome("    ") is True
    assert sol.isPalindrome("") is True
    assert sol.isPalindrome("  r acecar ") is True
    assert sol.isPalindrome("  r aecar ") is False
