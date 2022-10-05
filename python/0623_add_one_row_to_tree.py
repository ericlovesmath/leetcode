from typing import List, Optional

from utils import TreeNode


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        """
        Link: https://leetcode.com/problems/add-one-row-to-tree/
        Given a tree, add a row of nodes with `val` at `depth` of `root`.
        If depth = 1, treat root as a left branch.
        """

        # Basic BFS

        dummy = TreeNode(val)
        dummy.left = root

        row = [dummy]
        for _ in range(depth - 1):
            for _ in range(len(row)):
                curr = row.pop(0)
                if curr.left is not None:
                    row.append(curr.left)
                if curr.right is not None:
                    row.append(curr.right)

        for node in row:
            new_node = TreeNode(val)
            new_node.left = node.left
            node.left = new_node
            new_node = TreeNode(val)
            new_node.right = node.right
            node.right = new_node

        return dummy.left

        # Space Complexity: O(Max width of tree up to depth)
        # Time Complexity: O(Nodes to depth)
