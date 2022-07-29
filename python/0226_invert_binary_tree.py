from typing import Optional


class TreeNode:
    """Binary Tree"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Link: https://leetcode.com/problems/invert-binary-tree/
        Given the root of a binary tree, invert it and return the root.
        """

        if root is None:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()
