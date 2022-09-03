from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        """
        Link: https://leetcode.com/problems/numbers-with-same-consecutive-differences/
        Return all non-negative integers of length n such that
        the absolute difference between every two consecutive digits is k.
        Numbers must not have leading zeros.
        You may return the answer in any order.
        """

        # We will start with a list of 1-9
        # We will iterate through the list and add numbers 1 digit longer
        # Loop until all numbers are of length n

        answer = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for _ in range(n - 1):
            for _ in range(len(answer)):
                curr = answer.pop(0)
                last_dig = curr % 10
                if last_dig - k >= 0:
                    answer.append(curr * 10 + last_dig - k)
                if last_dig + k <= 9 and k != 0:
                    answer.append(curr * 10 + last_dig + k)

        return answer


if __name__ == "__main__":
    sol = Solution()

    assert sorted(sol.numsSameConsecDiff(3, 7)) == sorted(
        [181, 292, 707, 818, 929]
    )
    assert sorted(sol.numsSameConsecDiff(2, 1)) == sorted(
        [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]
    )
    assert sorted(sol.numsSameConsecDiff(2, 0)) == sorted(
        [11, 22, 33, 44, 55, 66, 77, 88, 99]
    )
