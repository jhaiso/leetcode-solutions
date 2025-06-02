# 242. Valid Anagram

## Relevant Topics
String, HashTable

## Solution Thought Process
### Sorting?:
```python
# sort each string
# compare the values at each index
```
The above solution runs in O(nlogn + mlogm) / logarithmic time. 

### Idea:
Utilize a hash table or hash map as a counter for each string. Then, compare the two counters.
Time: O(n + m)
Space: O(1) - 26 letters of the alphabet
```python
# initialize counters
# iterate through strings
# compare
```