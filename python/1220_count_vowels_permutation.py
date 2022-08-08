class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        Link: https://leetcode.com/problems/count-vowels-permutation/
        Given length `n`, how many strings can be constructed?
        Each string only consists of vowels, each of which can only be 
        followed by a specific set of vowels.
        """

        # Adjacency List of directed graph
        # Any solution will be a traversal of this graph
        # Replace "AEIOU" with 0,1,2,3,4
        adj_list = [[1], [0, 2], [0, 1, 3, 4], [2, 4], [0]]

        # This question boils down to "How many paths are there on this directed graph?"

        # Bottom Up Solution
        # Let `ends` represent the number of strings ending in each char of AEIOU
        # For example, [1, 2, 0, 0, 0] is 1 string ending in A, and 2 strings ending in E.
        # We just have to track the last char each time
        # Starting from [1, 1, 1, 1, 1] when n=1, iterate forward

        ends = [1, 1, 1, 1, 1]

        for _ in range(n - 1):
            new_ends = [0, 0, 0, 0, 0]
            for i in range(5):
                for end in adj_list[i]:
                    new_ends[end] += ends[i]
            ends = new_ends

        return sum(ends) % (10**9 + 7)

        # Space Complexity: O(1)
        # Time Complexity: O(n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.countVowelPermutation(1) == 5
    assert sol.countVowelPermutation(2) == 10
    assert sol.countVowelPermutation(5) == 68
