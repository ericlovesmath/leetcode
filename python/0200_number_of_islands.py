from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Link: https://leetcode.com/problems/number-of-islands/
        Given a grid of 1s and 0s, find the number of islands of 1s.
        """

        # We will use DFS as it is more space efficient.
        # Track which islands are visited
        # Iterate through all of the tiles in the grid and DFS
        # Every time a new DFS occurs, it is a new island.

        height, width = len(grid), len(grid[0])
        visited = [[False for _ in range(width)] for _ in range(height)]

        def dfs(x: int, y: int):
            if x < 0 or x >= height or y < 0 or y >= width:
                return
            if visited[x][y] or grid[x][y] == "0":
                return

            visited[x][y] = True
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        islands = 0
        for x in range(height):
            for y in range(width):
                if not visited[x][y] and grid[x][y] == "1":
                    islands += 1
                    dfs(x, y)

        return islands

        # Space Complexity: O(m*n)
        # Time Complexity: O(m*n)


if __name__ == "__main__":
    sol = Solution()

    assert (
        sol.numIslands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
    assert (
        sol.numIslands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )
