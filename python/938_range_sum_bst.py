from typing import Optional


class TreeNode:
    """Binary Search Tree Node"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> int:
        """
        Link: https://leetcode.com/problems/range-sum-of-bst/
        Given `low` and `high`, find the sum of all nodes between
        `low` and `high` in the binary search tree.
        """

        # Use DFS to search through all elements
        # For an iterative solution, use BFS instead

        def dfs(curr):
            if curr is None:
                return 0
            if curr.val < low:
                return dfs(curr.right)
            if curr.val > high:
                return dfs(curr.left)
            return curr.val + dfs(curr.left) + dfs(curr.right)

        return dfs(root)
