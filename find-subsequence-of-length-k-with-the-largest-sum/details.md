# 2099. Find Subsequence of Length K With the Largest Sum

## Relevant Topics

Array, Heap, Hash Set, Sorting, Greedy

## Solution Thought Process

Although the order matters, because we are looking for the maximal sum subsequence of length k (and are effectively deciding if we should include/exclude each element), we can utilize a greedy approach and concern ourselves with the index later...

```python
# push all (element, index) pairs to a max heap
# initialize a set to keep track of included indices
# pop from heap until the set is at length k
# iterate through the array again and append to result if the index is in the set
```
Time Complexity: O(nlogn)
Space Complexity: O(n)