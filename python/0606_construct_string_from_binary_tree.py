from typing import Optional

from utils import TreeNode, binaryTree


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        Link: https://leetcode.com/problems/construct-string-from-binary-tree/
        Take a binary tree and generate a representative string
        """

        # Honestly its just recursive bashing

        if root is None:
            return ""
        if root.left is None and root.right is None:
            return str(root.val)
        if root.right is None:
            return f"{root.val}({self.tree2str(root.left)})"

        return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"

        # Space Complexity: O(n)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.tree2str(binaryTree([1])) == "1"
    assert sol.tree2str(binaryTree([1, 2, 3, 4])) == "1(2(4))(3)"
    assert sol.tree2str(binaryTree([1, 2, 3, None, 4])) == "1(2()(4))(3)"
