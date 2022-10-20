class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Link: https://leetcode.com/problems/integer-to-roman/description/
        Convert integer to the roman numeral string
        """

        # Hash map time

        int_to_roman = {
            1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
            50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I",
        }

        ans = []
        for integer, roman in int_to_roman.items():
            while num >= integer:
                ans.append(roman)
                num -= integer

        return "".join(ans)

        # Space Complexity: O(1)
        # Time Complexity: Amortized O(log(n))


if __name__ == "__main__":
    sol = Solution()

    assert sol.intToRoman(1) == "I"
    assert sol.intToRoman(3) == "III"
    assert sol.intToRoman(4) == "IV"
    assert sol.intToRoman(5) == "V"
    assert sol.intToRoman(8) == "VIII"
    assert sol.intToRoman(9) == "IX"
    assert sol.intToRoman(58) == "LVIII"
    assert sol.intToRoman(1994) == "MCMXCIV"
