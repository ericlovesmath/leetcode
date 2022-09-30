from typing import Optional

from utils import TreeNode, binaryTree


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
        You are given the root of a binary tree containing digits
        Each root-to-leaf path in the tree represents a number
        Return the total sum of all root-to-leaf numbers
        """

        # Its just DFS

        def dfs(curr, acc):
            if curr is None:
                return 0
            next = acc * 10 + curr.val
            if curr.left is None and curr.right is None:
                return next
            return dfs(curr.left, next) + dfs(curr.right, next)

        return dfs(root, 0)

        # Space Complexity: O(depth)
        # Time Complexity: O(nodes)


if __name__ == "__main__":
    sol = Solution()

    assert sol.sumNumbers(binaryTree([1, 2, 3])) == 25
    assert sol.sumNumbers(binaryTree([4, 9, 0, 5, 1])) == 1026
    assert sol.sumNumbers(binaryTree([4, 9, 0, None, 1])) == 531
