# 20. Valid Parenthesi
## Relevant Topics
String, Stack

## Solution Thought Process
### Brute Force
```python
# while the string is not empty
#   replace adjacent valid pairs with an empty string
# return if the string is empty
```

### Stack
We notice that in the brute force solution, we are looking at only adjacent pairs of parenthesis. Therefore, for an iterative solution, we only need too look at the most recent value, and can utilize a stack!
```python
# initialize a hashmap with (close, open pairs)
# initialize a character stack
# for each character
#   if is a key in hashmap
#     if peek is the value
#       pop
#     otherwise return False
#   otherwise push
# return if the set is not empty
```