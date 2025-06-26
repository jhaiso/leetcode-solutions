import collections


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = collections.Counter(s)
        total = 0
        res = count["0"]
        for i in range(len(s)-1, -1, -1):
            if s[i] == "1":
                if 2**(len(s)-i-1) + total > k:
                    return res
                else:
                    total += 2**(len(s)-i-1)
                    res += 1
        
        return res