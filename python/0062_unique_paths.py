class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Link: https://leetcode.com/problems/unique-paths/
        Find the number of paths from (0,0) to (m,n).
        You may only travel +x or +y.
        Note: Found DP and Math solution.
        """
        
        # The solution will use dynamic programming.
        # Let p(x, y) get the number of paths to (x,y)
        # Then, p(x, y) = p(x - 1, y) + p(x, y - 1)
        # Additionally, p(0, y) and p(x, 0) are 1
        # This way we can solve the problem in O(m*n) with memoization
        # We will solve it bottom-up
        
        sols = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    sols[i][j] = 1
                else:
                    sols[i][j] = sols[i-1][j] + sols[i][j-1]
        
        return sols[-1][-1]
        
        # We can alternatively use math.
        # The above solution works, but takes O(mxn) space and time
        # Let "R" and "D" signify the moves "Right" and "Down".
        # We can rearrange a sequence of (m-1) Ds and (n-1) Rs.
        # To do this, we have (m+n-2)!/((m-1)!(n-1)!)
        # This will take O(min(2m, 2n)) time and O(1) space
        
        # Make n < m to ensure O(2n)
        if m < n:
            m, n = n, m
        
        ans = 1
        for val in range(m, m+n-1):
            ans *= val
        for val in range(2, n):
            ans //= val

        return ans

if __name__ == "__main__":
    sol = Solution()

    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 2) == 3
    assert sol.uniquePaths(7, 16) == 54264
