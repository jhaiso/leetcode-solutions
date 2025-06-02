# 217. Contains Duplicate

## Relevant Topics
Array, Hash Table

## Solution Thought Process
### Brute Force:
```python
# iterate through each index
#   iterate through every other index
#       if values same
#           return True
# return False
```
The brute force solution runs in O(n^2)/polynomial time, we could probably do better...

### Idea:
By definition of consecutive sequence, for all starting sequence numbers n, n-1 is not in values
```python
# keep track of a set of values (or hashtable if indices are returned)
# iterate through each item
#   if the set contains the item
#       return True
#   add item to set
# return False
```