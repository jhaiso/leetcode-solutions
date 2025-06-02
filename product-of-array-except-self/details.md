# 238. Product of Array Except Self
## Relevant Topics
Array

## Solution Thought Process
### Brute Force
The brute force solution would involve calculating the product of every other element at each element.
Time Complexity: O(n^2)

### Division
Calculte the product of the entire array, and at each element, divide by element. (But the challenge is to not do it this way...)
Time Complexity: O(n).

### Prefix and Suffix
If you iterate forwards through the array, the total product would be the "prefix". And if you iterate backwards, you get the "suffix". The prefix and suffix at an index can be multiplied to get the product of all other elements.

```python
# initialize prefix array
# initialize suffix array
# initialize results array

# iterate forwards
# iterate backwards
# iterate through results array
#   calculate product at each index

# return
```
Time Complexity: O(n)
Space Complexity: O(n)

This can be further optimized by using integer variables for the prefix and suffix at any given index, and calculating the result during iteration.