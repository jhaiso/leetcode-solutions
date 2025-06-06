class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        res = ""
        longest = float('inf')

        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        
        l = 0
        met = 0
        running = {}

        for r in range(len(s)):
            running[s[r]] = running.get(s[r], 0) + 1
            if s[r] in count and count[s[r]] == running[s[r]]:
                met += 1
            while met == len(count):
                if (r - l + 1) < longest:
                    longest = r - l + 1
                    res = s[l:r+1]
                running[s[l]] -= 1
                if s[l] in count and count[s[l]] - 1 == running[s[l]]:
                    met -= 1
                l += 1
        
        return res
