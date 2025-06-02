# 36. Valid Sudoku
## Relevant Topics
Array, Hash Set, Bit-Masking

## Solution Thought Process
### Brute Force
```python
# for every space
#   check all other spaces in same column, row, and 3x3 grid
```
Time Complexity: O(n^3)

### Hash Set
Instead of checking every space to see if another of the same number exists in the same row, column, grid, we can keep a set of all values in each column, row, grid
```python
# initialize array of sets for rows, columns grid
# iterate through the board
#   check if number is in corresponding sets
```

Time Complexity: O(n^2)
Space Complexity: O(n^2)

### Bit-Masking
Because we using python (unapped bits in an integer) we can use bitmasking with bitshifting and bitwise-and to check if values are present.
```python
# initialize integer arrays for rows, cols, grid
# iterate through the board
#   check if (1 << num) & row || col || grid
```