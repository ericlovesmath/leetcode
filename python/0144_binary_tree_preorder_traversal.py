# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        path = [root.val]
        if root.left != None:
            path.extend(self.preorderTraversal(root.left))
        if root.right != None:
            path.extend(self.preorderTraversal(root.right))
        return path
