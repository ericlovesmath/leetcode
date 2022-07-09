class Solution:
    def isValid(self, s: str) -> bool:
        """
        Link: https://leetcode.com/problems/valid-parentheses/
        Given a string of '(){}[]', determine if it is valid
            1. All brackets must be closed by the same type of bracket
            2. All brackets must be closed in order
        """

        # We can use a stack to add open brackets and remove closed brackets

        stack = []
        open = set("({[")
        to_open = {")": "(", "]": "[", "}": "{"}

        for bracket in s:
            if bracket in open:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != to_open[bracket]:
                    return False

        # Stack should be empty by end
        return len(stack) == 0

        # Space Complexity: O(n)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("(]") is False

    assert sol.isValid("([)]{}") is False
