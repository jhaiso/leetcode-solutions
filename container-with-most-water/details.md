# 11. Container With Most Water
## Relevant Topics
Array, Two Pointers, Greedy

## Solution Thought Process
### Brute Force
Go through all possible containers, calculate the area, update maximum.
Time Complexity: O(n^2)
Space Complexity: O(1)

### Two Pointers
We observe that the container has two sides, and the area is only dependent on the smaller one. Start at both sides of the array. It doesn't make sense to move the larger one, since no matter what the height of the next container wall is, the area will get smaller. So, we move the smaller one closer until the pointers cross (greedy choice property!!)!

