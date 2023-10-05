from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = {}
        for s in strs:
            freq_s = self.strToFreq(s)
            if freq_s not in freqs:
                freqs[freq_s] = []
            freqs[freq_s].append(s)
        return freqs.values()

    def strToFreq(self, s: str):
        freq = [0 for _ in range(26)]
        for c in s:
            freq[ord(c) - ord("a")] += 1
        return tuple(freq)
