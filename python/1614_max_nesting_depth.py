class Solution:
    def maxDepth(self, s: str) -> int:

        max_height = 0
        curr_height = 0
        for c in s:
            if c == "(":
                curr_height += 1
                if curr_height > max_height:
                    max_height = curr_height
            elif c == ")":
                curr_height -= 1

        return max_height
