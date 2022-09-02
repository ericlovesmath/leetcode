from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
        `heights` is an `mxn` grid of heights
        Water flows to adjacent cells with less than or equal height
        The pacific ocean is the top and left adjacent space.
        The atlantic ocean is the bottom and right adjacent space.
        Return the coordinates of cells flowing to both oceans.
        """

        # We will store a matrix of if that cell can get to the oceans
        # We will store one for pacific, one for atlantic
        # If a cell has both true, then we add it to the answer

        # We will run dfs on each cell, on the ocean, go backwards
        # We are essentially dfs-ing "uphill"

        ROWS, COLS = len(heights), len(heights[0])

        def dfs(row, col, visited):
            visited[row][col] = True
            for row_dir, col_dir in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                i, j = row + row_dir, col + col_dir
                if i < 0 or i >= ROWS or j < 0 or j >= COLS or visited[i][j]:
                    continue
                if heights[row][col] <= heights[i][j]:
                    dfs(i, j, visited)

        pacific = [[False for _ in range(COLS)] for _ in range(ROWS)]
        atlantic = [[False for _ in range(COLS)] for _ in range(ROWS)]

        # DFS Starting for Ocean Edges
        for row in range(ROWS):
            dfs(row, 0, pacific)
            dfs(row, COLS - 1, atlantic)
        for col in range(COLS):
            dfs(0, col, pacific)
            dfs(ROWS - 1, col, atlantic)

        # Find where DFS from pacific and atlantic worked
        both_runoff = []
        for row in range(ROWS):
            for col in range(COLS):
                if pacific[row][col] and atlantic[row][col]:
                    both_runoff.append([row, col])

        return both_runoff

        # Space Complexity: O(n*m)
        # Time Complexity: O(n*m)


if __name__ == "__main__":
    sol = Solution()

    assert sol.pacificAtlantic(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    ) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert sol.pacificAtlantic([[1]]) == [[0, 0]]
