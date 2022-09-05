from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
        Given a string containing digits from 2-9 inclusive,
        return all possible letter combinations that the number could represent.
        Answer may be returned in any order.
        """

        # We can make a hash map of all the keys by index
        # Then we can backtrack digit by digit, appending the possibilites
        # Sort of like BFS

        if len(digits) == 0:
            return []

        key_to_letters = [
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz",
        ]
        combos = [""]

        for digit in digits:
            temp = []
            for combo in combos:
                for letter in key_to_letters[ord(digit) - ord("2")]:
                    temp.append(combo + letter)
            combos = temp

        return combos


if __name__ == "__main__":
    sol = Solution()

    assert sol.letterCombinations("23") == [
        "ad",
        "ae",
        "af",
        "bd",
        "be",
        "bf",
        "cd",
        "ce",
        "cf",
    ]
    assert sol.letterCombinations("") == []
    assert sol.letterCombinations("2") == ["a", "b", "c"]
