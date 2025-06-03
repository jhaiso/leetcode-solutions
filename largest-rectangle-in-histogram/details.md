# 84. Largest Rectangle in Histogram
## Relevant topics
Stack

## Solution Thought Process
### Brute Force
For every rectangle, expand the retangle left and right until smaller rectangles are found on either side or the end is reached.

Time Complexity: O(n^2)
Space Complexity: O(1)

### Stack
We see that we are looking for the next smallest rectangle (or edge) to define the left and right of the rectangle (and therefore area). Intuitively, we can utilize a stack.
```python
# initialize a stack to keep track of height and index

# for each rectangle in the histogram
#   while the rectangle is shorter than peek
#     pop
#     compare the maximum to the height of the popped rectangle * difference of indices
#   push current height & popped index (the rectangle can extend to the left if the previous rectangles are taller)

#   for the remaining rectangles
#     calculate area from height * (end - index)
#     update max

#   return the maximum
```