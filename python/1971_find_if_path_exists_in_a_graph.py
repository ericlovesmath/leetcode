from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        """
        Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
        You're given edges of a bidirectional graph with n nodes
        Given a source and destination, identify if there is a path between them
        """

        # Solution 1: DFS/BFS after building adjacency list
        # If you start at source, you should reach the destination
        # This is O(len(edges)) in space

        # Solution 2: Union Find
        # This will let us just use O(1) space

        parent = [i for i in range(n)]

        # Includes path compression, amortized O(1)
        def find(node):
            if parent[node] == node:
                return node
            rep = find(parent[node])
            parent[node] = rep
            return rep

        for a, b in edges:
            parent[find(a)] = find(b) # Union

        return find(source) == find(destination)

        # Space Complexity: O(n)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.validPath(5, [], 0, 0) is True
    assert sol.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2) is True
    assert (
        sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5)
        is False
    )
    assert (
        sol.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 3, 5)
        is True
    )
