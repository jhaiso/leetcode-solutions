class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        l = 0
        fmax = 0

        for i, c in enumerate(s):
            count[c] = count.get(c,0) + 1
            fmax = max(fmax, count[c])

            while (i - l + 1) - fmax > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, i - l + 1)
        
        return res