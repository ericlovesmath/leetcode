from typing import Optional

from utils import TreeNode, binaryTree


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Link: https://leetcode.com/problems/path-sum/
        Return if the tree has a root-to-leaf path that sum to targetSum
        """

        if root is None:
            return False

        if root.left is None and root.right is None:
            return targetSum == root.val

        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )

        # Space Complexity: O(height)
        # Time Complexity: O(num nodes)


if __name__ == "__main__":
    sol = Solution()

    assert (
        sol.hasPathSum(
            binaryTree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),
            22,
        )
        is True
    )
    assert sol.hasPathSum(binaryTree([1, 2, 3]), 5) is False
    assert sol.hasPathSum(binaryTree([]), 0) is False
