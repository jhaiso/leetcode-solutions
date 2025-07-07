# 1353. Maximum Number of Events That Can Be Attended

## Relevant Topics

Array, Sorting, Greedy, Heap Priority Queue

## Solution Thought Process

When looking at the example solutions to the problem, I naturally take a greedy approach:
For the example [[1,2], [2,3], [3,4], [1,2]]. 

```python
# sort the array
# for each day
#   we take the first available meeting with the earliest end time (to save space for other events)
```