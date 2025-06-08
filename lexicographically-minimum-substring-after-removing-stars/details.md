# 3170. Lexicographically Minimum Substring After Removing Stars

## Relevant Topics

String, Stack, Heap, Priority Queue, Greedy

## Solution Thought Process

### Brute Force

Traverse through the string. When a star is found, check the entire string before it, and remove the lexigraphically smallest character furthest to the right.
Time Complexity: O(n^2)
Space Complexity: O(n) - for storing result

### Greedy - Stack

Since we are removing the most recent lexigraphically smallest character when traversing through the string, we can utilize stacks to store the indices of where they occur! Additionally, at each step, by definition we are removing the optimal choice, so it has the greedy choice property.

```python
# create an array of stacks to store the occurences of each character

# for each character in the string
#   if the character is NOT an *    # we use NOT here because it is more likely that the character isn't a *
#       find the most recent occurence of the smallest seen character
#       remove it and the * from the result
#   otherwise
#       add the character

# return the result
```

Time Complexity: O(n\*m) - n size of string, m size of charcter set (could be considered 26??)
Space Complexity: O(n+m) - for result and size of stacks

### Greedy - Priorty Queue / Heap

We see that we are looking for the latest occuring, lexigraphically smallest character that we've seen, so we can maintain a min heap to get the minimum in O(1) time!

```python
# initialize heap
# for each character in s
#   if character is NOT *:
#       push (character, -index) pair to heap  # we utilize the -index becaus we want the maximal index (latest) occurence
#   otherwise:
#       pop from heap
#       set result at index of the * and the popped character to be empty

# return the result
```