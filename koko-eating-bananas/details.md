# 875. Koko Eating Bananas
## Relevant Topics
Binary Search

## Solution Thought Process
### Brute Force
We see that the minimum eating rate is 1, and the upper bound is the largest pile (since all other piles would take 1 hour to eat each). Therefore, we search through every eating rate [1, max(piles)] to find the minimum k such that koko eats all the bananas in time.
Time Complexity: O(m * n)
Space Complexity: O(1)

### Binary Search
Rather than searcing linearly, we can utilize binary search!