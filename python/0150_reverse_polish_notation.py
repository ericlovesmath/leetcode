from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
        Evaluate Reverse Polish Notation.
        """

        nums = []
        for token in tokens:
            if token.isdigit() or token[0] == "-" and token[1:].isdigit():
                nums.append(int(token))
                continue

            right, left = nums.pop(), nums.pop()
            if token == "+":
                nums.append(left + right)
            elif token == "-":
                nums.append(left - right)
            elif token == "*":
                nums.append(left * right)
            else:
                nums.append(int(left / right))

        return nums[0]

        # Space Complexity: O(n)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert (
        sol.evalRPN(
            [
                "10",
                "6",
                "9",
                "3",
                "+",
                "-11",
                "*",
                "/",
                "*",
                "17",
                "+",
                "5",
                "+",
            ]
        )
        == 22
    )
