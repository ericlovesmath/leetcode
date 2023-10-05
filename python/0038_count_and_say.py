class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Link: https://leetcode.com/problems/count-and-say/description/
        Return the nth Look-and-Say or Conway sequence
        e.g.: 1, 11, 21, 1211, 111221
        """

        # We just simulate it

        sequence = [1]

        for _ in range(n - 1):
            new_sequence = []
            curr, size = sequence[0], 0
            for num in sequence:
                if num == curr:
                    size += 1
                else:
                    new_sequence.extend([size, curr])
                    curr, size = num, 1
            new_sequence.extend([size, curr])
            sequence = new_sequence

        print(*sequence)
        return "".join(str(n) for n in sequence)

        # Space Complexity: O(len(ans))
        # Time Complexity: O(len(ans))


if __name__ == "__main__":
    sol = Solution()

    assert sol.countAndSay(1) == "1"
    assert sol.countAndSay(4) == "1211"
    assert sol.countAndSay(10) == "13211311123113112211"
