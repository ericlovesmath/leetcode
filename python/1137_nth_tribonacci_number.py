class Solution:
    def fib(self, n: int) -> int:
        """
        Link: https://leetcode.com/problems/n-th-tribonacci-number/
        Return the nth tribbonacci number.
        """

        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return a


if __name__ == "__main__":
    sol = Solution()

    assert sol.fib(0) == 0
    assert sol.fib(1) == 1
    assert sol.fib(2) == 1
    assert sol.fib(3) == 2
    assert sol.fib(4) == 4
    assert sol.fib(25) == 1389537
