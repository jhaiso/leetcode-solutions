# 40. Combination Sum II

## Relevant Topics

Array, Backtracking, Sorting

## Solution Thought Proccess

Because we are looking for ALL unique combinations, backtracking comes to mind. Additionally, since we are avoiding duplicate combinations, we should sort the array.

```python
# sort the candidates array
# initialize result
# initialize current

# funciton backtrack(index, sum)
#   if the sum is equal to the target
#       append a copy of current to result
#       return
#   otherwise
#   for the elements from index to the length of the candidates
#       if j > index and candidates[j] == candidates[j-1]:
#           continue
#       otherwise
#       modify, backtrack, remove :)
```
