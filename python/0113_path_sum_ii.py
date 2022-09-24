from typing import List, Optional

from utils import TreeNode, binaryTree


class Solution:
    def pathSum(
        self, root: Optional[TreeNode], targetSum: int
    ) -> List[List[int]]:
        """
        Link: https://leetcode.com/problems/path-sum-ii/
        Return all root-to-leaf path that sum to targetSum
        """

        # We're basically stealing from path sum 0112
        # Treat as DFS

        ans = []

        def dfs(curr, target, path):

            if curr is None:
                return

            if curr.left is None and curr.right is None and target == curr.val:
                ans.append(path + [curr.val])

            target -= curr.val

            dfs(curr.left, target, path + [curr.val])
            dfs(curr.right, target, path + [curr.val])

        dfs(root, targetSum, [])

        return ans

        # Space Complexity: O(height)
        # Time Complexity: O(num nodes)


if __name__ == "__main__":
    sol = Solution()

    assert sol.pathSum(
        binaryTree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]),
        22,
    ) == [[5, 4, 11, 2], [5, 8, 4, 5]]
    assert (
        sol.pathSum(
            binaryTree([1, 2, 3]),
            5,
        )
        == []
    )
    assert (
        sol.pathSum(
            binaryTree([1, 2]),
            0,
        )
        == []
    )
