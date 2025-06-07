import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        # iterate through the string
        # use a heap to keep track of the smallest element
        #   the heap contains, char, index
        res = list(s)
        h = []
        for i, c in enumerate(s):
            if c == "*":
                char, negative_index = heapq.heappop(h)
                res[-negative_index] = ""
                res[i] = ""
            else:
                heapq.heappush(h, (c, -i)) # maintains maximum index first
        
        return "".join(res)