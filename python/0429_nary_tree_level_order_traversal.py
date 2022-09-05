from typing import List
from collections import deque


class Node:
    """ Definition for a Node. """
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        """
        Link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/
        Given an n-ary tree, return the level order traversal of its nodes' values
        """

        # This is essentially literally just BFS
        # Instead of clearing the queue, we'll just add a new layer

        if root is None:
            return []

        traversal = []
        queue = deque([root])

        while len(queue) != 0:
            traversal.append([])
            for _ in range(len(queue)):
                node = queue.popleft()
                traversal[-1].append(node.val)
                for child in node.children:
                    queue.append(child)

        return traversal

        # Space Complexity: O(n)
        # Time Complexity: O(n)
