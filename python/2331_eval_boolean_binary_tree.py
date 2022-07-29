from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
        Link: https://leetcode.com/problems/evaluate-boolean-binary-tree/
        Evaluate the binary tree of boolean functions.
        """
        def dfs(curr):

            # Leaves
            if curr.left is None:
                return curr.val == 1

            # Check operations
            if curr.val == 2:
                return dfs(curr.left) or dfs(curr.right)
            else:
                return dfs(curr.left) and dfs(curr.right)

        return dfs(root)
