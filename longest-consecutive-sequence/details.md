# 128. Longest Consecutive Sequence
## Relevant Topics
Array, Hash Set

## Solution Thought Process
### Brute Force
```python
# for each integer in the array
#   check the longest sequence starting at that number
```
Time Complexity: O(n^2)
Space Complexity: O(n)

### Sorting
Sorting would prevent the overlapping counting, since the integers would be in ascending order.
```python
# sort the array
# for i frmo 0 to length of array
#   increment i and count consecutive integers
```
Time Complexity: O(nlogn)
Space Complexity: O(n)

### Hash Set
We notice from sorting that each maximal consecutive sequence begins with a number n such that n-1 is not present in the array. Therefore, if we add all the integers into a set, we can find the longest sequence in linear time!
```python
# add all integers from array to a hash set
# for each element in set
#   if element-1 not in set
#     count sequence
# return longest
```