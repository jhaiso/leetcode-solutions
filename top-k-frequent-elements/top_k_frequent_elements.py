from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for element, freq in freq.items():
            buckets[freq].append(element)
        
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for e in buckets[i]:
                res.append(e)
                if len(res) == k:
                    return res