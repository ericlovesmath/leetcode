from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = {}
        for c in words[0]:
            if c not in common:
                common[c] = 0
            common[c] += 1
            
        for word in words:
            curr = {}
            for c in word:
                if c not in common:
                    continue
                if c not in curr:
                    curr[c] = 0
                if curr[c] < common[c]:
                    curr[c] += 1
            common = curr

        ans = []
        for c in common:
            for _ in range(common[c]):
                ans.append(c)
        return ans
