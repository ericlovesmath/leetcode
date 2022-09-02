from typing import List, Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
        Return the average value of the nodes on each level.
        """

        # Use BFS

        averages = []
        queue = [root]

        while len(queue) != 0:

            size = len(queue)
            averages.append(0)

            for _ in range(size):

                curr = queue.pop(0)
                averages[-1] += curr.val
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)

            averages[-1] /= size

        return averages

        # Space Complexity: O(Max width)
        # Time Complexity: O(n)
