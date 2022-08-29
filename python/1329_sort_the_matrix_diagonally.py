from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Link: https://leetcode.com/problems/sort-the-matrix-diagonally/
        Sort the top-left to bottom-right diagonals of `mat` in order.
        """

        # We will sort mat in-place.
        # We will go through each diagonal and add them to a buffer
        # Then, sort the buffer and return it back to the diagonal
        # The i-j being identical will mean they are the same diagonal

        ROW_LEN = len(mat)
        COL_LEN = len(mat[0])

        # Diagonals indexed by -ROW_LEN to COL_Len
        # Shifted right by ROW_LEN
        diagonals = [[] for _ in range(ROW_LEN + COL_LEN - 1)]

        # Get diagonal values
        for row in range(ROW_LEN):
            for col in range(COL_LEN):
                id = col - row + ROW_LEN - 1
                diagonals[id].append(mat[row][col])

        # Sort diagonals
        diagonals = [sorted(diagonal) for diagonal in diagonals]

        # Return diagonal values
        for row in range(ROW_LEN):
            for col in range(COL_LEN):
                id = col - row + ROW_LEN - 1
                mat[row][col] = diagonals[id].pop(0)

        return mat

        # Space Complexity: O(m*n)
        # Time Complexity: O(m*log(n))


if __name__ == "__main__":
    sol = Solution()

    # fmt: off
    assert sol.diagonalSort(
        [
            [3, 3, 1, 1],
            [2, 2, 1, 2],
            [1, 1, 1, 2],
        ]
    ) == [
        [1, 1, 1, 1],
        [1, 2, 2, 2],
        [1, 2, 3, 3],
    ]
    assert sol.diagonalSort(
        [
            [11, 25, 66, 1, 69, 7],
            [23, 55, 17, 45, 15, 52],
            [75, 31, 36, 44, 58, 8],
            [22, 27, 33, 25, 68, 4],
            [84, 28, 14, 11, 5, 50],
        ]
    ) == [
        [5, 17, 4, 1, 52, 7],
        [11, 11, 25, 45, 8, 69],
        [14, 23, 25, 44, 58, 15],
        [22, 27, 31, 36, 50, 66],
        [84, 28, 75, 33, 55, 68],
    ]
    # fmt: on
