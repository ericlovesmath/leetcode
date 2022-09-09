from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        """
        Link: https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
        `Properties` is a list of characters, who each have an [attack, defense].
        It is weak if its attack and defense are weaker than some other character.
        Return the number of total weak characters.
        """

        # We can sort by attack to only care about defense
        # Then, we can start from the "high" attack and move down
        # As we move down, we track the highest defense so far
        # If we don't update the highest defense, then it must be weak

        # This is a mix of sorting, then kind of greedy/DP

        max_def = 0
        count_weak = 0
        for char in sorted(properties, key=lambda prop: (-prop[0], prop[1])):
            if max_def > char[1]:
                count_weak += 1
            else:
                max_def = max(max_def, char[1])

        return count_weak

        # Space Complexity: O(1)
        # Time Complexity: O(n log n)


if __name__ == "__main__":
    sol = Solution()

    assert sol.numberOfWeakCharacters([[5, 5], [6, 3], [3, 6]]) == 0
    assert sol.numberOfWeakCharacters([[2, 2], [3, 3]]) == 1
    assert sol.numberOfWeakCharacters([[1, 5], [10, 4], [4, 3]]) == 1
    assert (
        sol.numberOfWeakCharacters([[1, 5], [10, 4], [10, 3], [10, 5], [4, 3]])
        == 1
    )
    assert (
        sol.numberOfWeakCharacters(
            [[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]]
        )
        == 2
    )
