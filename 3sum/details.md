# 15. 3Sum
## Relevant Topics
Array, Sorting, Two Pointers

## Solution Thought Process
### Brute Force
Time Complexity: O(n^3)
Space Coomplexity: O(m) - output array size

### Sorting
As the name implies, we see that this is basically n * Two Sum (if that makes sense?), since for every value, we find other combinations of two values that equal 0 - first number. Therefore a hasmap can be used for O(n^2) time and O(n + m) space, or two pointers can be used for O(n^2) time and O(m) space.