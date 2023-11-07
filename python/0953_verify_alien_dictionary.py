from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order = {c: i for (i, c) in enumerate(order)}
        for i in range(len(words) - 1):
            for l, r in zip(words[i], words[i+1]):
                if order[l] > order[r]:
                    return False
                elif order[l] < order[r]:
                    break
            else:
                if len(words[i]) > len(words[i+1]):
                    return False
        return True
