class Solution:
    def fib(self, n: int) -> int:
        """
        Link: https://leetcode.com/problems/fibonacci-number/
        Return the nth fibbonacci number.
        """

        # Method 1: Dynamic Programming
        # Bottom up, because recursion is slow
        # We could also to recursion with caching too
        # Space O(n), Time O(n)

        fibb = [0, 1]
        for _ in range(n - 1):
            fibb.append(fibb[-2] + fibb[-1])
        return fibb[n]

        # Method 2: Dynamic Space O(1)

        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

        # Method 2: Binet's Formula
        # Probably worse for interviews, but explicit formula exists
        # Space O(1), Time O(1)

        sq_5 = 5**0.5
        return int(((1 + sq_5) ** n - (1 - sq_5) ** n) / (2**n * sq_5))


if __name__ == "__main__":
    sol = Solution()

    assert sol.fib(0) == 0
    assert sol.fib(1) == 1
    assert sol.fib(2) == 1
    assert sol.fib(3) == 2
    assert sol.fib(4) == 3
    assert sol.fib(5) == 5
