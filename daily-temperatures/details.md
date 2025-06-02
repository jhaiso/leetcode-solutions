# 739. Daily Temperatures 
## Relevant Topics
Stack

## Solution Thought Process
### Brute Force
```python
# for each temperature
#   search forwards in the array until a higher temperature is found
```
Time Complexity: O(n^2)

### Stack
We notice in the brute force solution that if we find a temperature, all temperatures less than than can be disregarded in the sequence. Therefore, unaccounted for temperatures are in decreasing order, and a stack can be used to compare the most recent (lowest) temperature and the current tempurature.
```python
# initialize stack (temp, index)
# for each temperature in the array
#   while peek is less than the current temperature
#     pop and update the result
#   push
```
Time Complexity: O(n)
Space Complexity: O(n)