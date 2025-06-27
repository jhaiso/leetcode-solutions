from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []
        def backtrack(idx):
            if idx >= len(s):
                res.append(curr[:])
                return
            for i in range(idx, len(s)):
                if self.isPalindrome(s[idx:i+1]):
                    curr.append(s[idx:i+1])
                    backtrack(i+1)
                    curr.pop()
        backtrack(0)
        return res

    def isPalindrome(self, s: str): # can be faster with 2 pointers
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True