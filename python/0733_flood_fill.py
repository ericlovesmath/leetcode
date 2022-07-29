from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """
        Link: https://leetcode.com/problems/flood-fill/
        `image` is an mxn image where image[i][j] is the pixel value.
        Flood fill the image with `color`, starting from image[sr][sr].

        Flood Fill:
            1. Paint the current pixel
            2. Paint edge-adj pixels of the same color as the start
            3. Repeat until all adj pixels are replaced
        """

        # In order to do a recursive solution,
        # we would have to know the original color
        # Therefore, we can use a stack based DFS OR recursive DFS
        # We will use the Recursive DFS to avoid StackOverflow

        start_color = image[sr][sc]
        if start_color == color:
            return image

        def dfs(row: int, col: int):
            if image[row][col] != start_color:
                return

            image[row][col] = color
            if row - 1 >= 0:
                dfs(row - 1, col)
            if row + 1 < len(image):
                dfs(row + 1, col)
            if col - 1 >= 0:
                dfs(row, col - 1)
            if col + 1 < len(image[0]):
                dfs(row, col + 1)

        dfs(sr, sc)

        return image

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ]

    assert sol.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [
        [0, 0, 0],
        [0, 0, 0],
    ]

    assert sol.floodFill([[0, 0, 0], [0, 0, 0]], 1, 0, 2) == [
        [2, 2, 2],
        [2, 2, 2],
    ]
