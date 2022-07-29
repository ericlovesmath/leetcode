from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
        Get the maximum depth of a binary tree.
        """

        def dfs(curr, depth):
            if curr is None:
                return depth
            return max(dfs(curr.left, depth + 1), dfs(curr.right, depth + 1))

        return dfs(root, 0)
