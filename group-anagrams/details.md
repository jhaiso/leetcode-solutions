# 49. Group Anagrams
## Relevant Topics
String, Array, Sorting, Hash Table

## Solution Thought Process
### Sorting
As with any anagram problem, an inefficient way to check anagrams is by sorting the characters in a string...
```python
# initialize a hash table to keep track of (sorted, set(original)) key value pairs
# for each string
#   sort
#   insert into table
# return values of table
```
Time complexity: O(m + nlogn) - m is the number of strings, n is the length of the longest string
Space Complexity: O(m * n)

### Idea: 
The count of each character in a string can be stored in a hash table and computed in linear time!
```python
# initialize a hash table to keep track of (counter, set(original)) key value pairs
# for each string
#   initialize a counter
#   count each character
#   insert string into table
# return values of hash table
```