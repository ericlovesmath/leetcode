from collections import deque
from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        Link: https://leetcode.com/problems/deepest-leaves-sum/
        Return the sum of the values of the deepest leaves
        """

        # Using BFS to traverse while tracking depth
        # When depth increases, reset max_sum
        # Can use DFS for less space time

        max_sum = 0
        max_depth = 0
        visiting = deque()

        visiting.append((root, 0))

        while visiting:

            curr, depth = visiting.popleft()

            if depth > max_depth:
                max_sum = 0
                max_depth = depth

            max_sum += curr.val

            if curr.left is not None:
                visiting.append((curr.left, depth + 1))
            if curr.right is not None:
                visiting.append((curr.right, depth + 1))

        return max_sum
