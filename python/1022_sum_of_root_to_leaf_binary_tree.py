from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
        `root` is a binary tree of 0s and 1s.
        When creating a line from the root to each leaf, you get a binary number.
        Find the sum of all such binary numbers.
        """

        def dfs(curr, total):

            if curr is None:
                return 0

            total <<= 1
            total += curr.val

            # If leaf, stop here
            if curr.left is None and curr.right is None:
                return total

            return dfs(curr.left, total) + dfs(curr.right, total)

        return dfs(root, 0)
