# 2561. Rearranging Fruits

## Relevant Topics

Hash Map, Greedy, Sort

## Solution Thought Process

By the definition of equal baskets provided by the problem, the total number of each fruit among the two baskets must be even. Additionally, if the two baskets have different amounts of each fruit, we must swap half of the difference.

We see that we can either perform a direct swap of a and b (where the cost is min(a, b)), or we can perform an indirect swap using an element c, where the cost would be 2 \* c if c is smaller than a and b.

```python
# create a counter to keep track of differences between baskets
# create a list of items that need to be swapped
# for each key, count in the counter
#   if count is odd, return -1 (since an even distribution is never possible)
#   append count // 2 of the key to the list of items

# identify the minimum value
# sort the array of items needed to be swapped
# look through the first half of the array, and aggregate the cost of either the value or 2 * minimum
```
Time Complexity: O(nlogn)
Space Complexity: O(n)