class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
        A node is good if all nodes to the root are not greater than it.
        Return the total number of good nodes given a binary tree.
        """

        return self.recur(root, root.val)

        # Space Complexity: O(1)
        # Time Complexity: O(n)

    def recur(self, root: TreeNode, curr_max: int) -> int:

        if root is None:
            return 0

        count = 1 if root.val >= curr_max else 0

        curr_max = max(curr_max, root.val)
        count += self.recur(root.left, curr_max)
        count += self.recur(root.right, curr_max)

        return count
