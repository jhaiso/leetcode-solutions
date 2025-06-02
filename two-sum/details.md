# 1. Two Sum
## Relevant Topics
Array, Hash Table

## Solution Thought Process
### Brute Force:
```python
# for each index
#   for every subsequent index
#       check if sum is target
```
The brute force solution has as time complexity of O(n^2).

### Idea:
When checking if the target can be reached for a specific index, we only have to check if target-current_value exists. To check if something exists in an array, we can just add it to a set of seen values!
```python
# initialize a set for seen values
# for each value
#   check if target-value is in set
#       return
#   otherwise add to set (could be (value, index) pair depending on requirements)
```