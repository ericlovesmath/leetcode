from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Link: https://leetcode.com/problems/rotting-oranges/
        mxn `grid` has 3 possible values:
            0: Empty Cell
            1: Fresh Orange
            2: Rotten Orange
        Every minute, any adjacent (no diagonal) fresh orange
        to a rotten orange becomes rotten.
        Return the minimum number of minutes for all to stop being fresh.
        If impossible, return -1
        """

        # We will use BFS starting at each rotten orange simultaneously
        # We will track the visited nodes
        # After BFS, we will iterate through the grid to see if we
        # did not visit any fresh oranges, meaning we return -1

        ROWS, COLS = len(grid), len(grid[0])

        queue = []
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        fresh_left = 0

        # Add rotten oranges to queue, count up the number of fresh oranges
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_left += 1

        minutes = 0

        # BFS
        while len(queue) > 0 and fresh_left > 0:
            for _ in range(len(queue)):
                x, y = queue.pop(0)

                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    new_x, new_y = x + dx, y + dy
                    if new_x < 0 or new_x == ROWS or new_y < 0 or new_y == COLS:
                        continue
                    if grid[new_x][new_y] == 0 or grid[new_x][new_y] == 2:
                        continue
                        
                    fresh_left -= 1
                    grid[new_x][new_y] = 2
                    
                    queue.append((new_x, new_y))

            minutes += 1
        
        return minutes if fresh_left == 0 else -1

        # Space Complexity: O(n*m)
        # Time Complexity: O(n*m)


if __name__ == "__main__":
    sol = Solution()

    assert sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert sol.orangesRotting([[0, 2]]) == 0
    assert sol.orangesRotting([[0]]) == 0
