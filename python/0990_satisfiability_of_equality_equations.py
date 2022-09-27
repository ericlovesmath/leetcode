from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
        Link: https://leetcode.com/problems/satisfiability-of-equality-equations/
        Given "a==b" and "a!=b" type strings, determine if all can be true
        """

        # This is just the definition of Union Find

        relations = [i for i in range(26)]

        # Find with Path Compression, effectively constant  
        def find(i):
            if relations[i] == i:
                return i
            parent = find(relations[i])
            relations[i] = parent
            return parent

        c_to_i = {chr(ord("a") + i): i for i in range(26)}

        for l, op, _, r in equations:
            if op == "=":
                relations[find(c_to_i[l])] = find(c_to_i[r])  # union op

        for l, op, _, r in equations:
            if op == "!" and find(c_to_i[l]) == find(c_to_i[r]):
                return False

        return True

        # Time Complexity: O(n)
        # Space Complexity: O(1)


if __name__ == "__main__":
    sol = Solution()

    assert sol.equationsPossible(["a==b", "b!=a"]) is False
    assert sol.equationsPossible(["b==a", "a==b"]) is True
    assert (
        sol.equationsPossible(["f==a", "a==b", "f!=e", "a==c", "b==e", "c==f"])
        is False
    )
