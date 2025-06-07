# 239. Sliding Window Maximum

## Relevant Topics

Array, Sliding Window, Monotonic Queue

## Solution Thought Process

### Brute Force

A brute force solution involves finding the maximum in each window, and adding that to the result.
Time Complexity: O(n\*k), n is length of array, and k is size of window
Space Complexity: O(n), size of result

### Priority Queue (Heap)

We see that in any window, we should keep track of the maximum value. When keeping track of a maximum/minimum value in a subseqence, a heap comes to mind (since insertion is O(logn) and checking the max/min value is O(1)). We can maintain the window maximum by popping if the index of the value is outside of the window at each step.

```python
# initialize heap
# initialize left
# for each value in the array
#   push value and index onto heap
#   while top index less than left
#       pop
#   set result to max value in heap
#   if value is greater than k
#       increment left
```

Time Complexity: O(nlogn), n elements, n potential insertions/pops
Space Complexity: O(n), size of heap

### Monotonic Queue

We see that each time we vind a maximum value, while the subsequent values should be considered (as the subsequent windows will not include that maximum), the previous values can be discarded. Therefore, we can keep a monotonic stack where the values are strictly decreasing. Each iteration, we left pop values if the index is outside of the window. Then, if the value being added is greater than the value at the left of the queue, we pop everything and enque the new largest value. In this way, we preserve the loop invariant that the left value of the queue is the maximum in the current window.

```python
# initialize queue
# initialize left

# for each value in the array
#   if current index >= k:
#       increment left
#   while left outside window:
#       pop
#   while current value >= left value:
#       pop
#   append left value to results

# return result
```
