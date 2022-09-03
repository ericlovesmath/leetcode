class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Link: https://leetcode.com/problems/climbing-stairs/
        You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps.
        In how many distinct ways can you climb to the top?
        """

        # Use Dynamic Programming
        # p(n) = p(n-1) + p(n-2), p(1) = 1, p(2) = 2
        # We can do bottom-up DP, but we can also just notice its fibbonacci
        
        a, b = 1, 2
        for _ in range(n - 1):
            a, b = b, a + b
        return a

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(45) == 1836311903
