# 567. Permutation In String

## Relevant Topics

Sliding Window, Hash Table

## Solution Thought Process

### Brute Force

Check every substring in s2, count the characters, and compare it to the count of s1.
Time Complexity: O(n \* m), n is length of s2, m is length of s1
Space Complexity: O(1), we can allocate an array of length 26 for lowercase characters

### Sliding Window

We are checking over possible substrings/subsequences of a specific length, so sliding window comes to mind. To prevent repeated comparison of the count of s1 to the running window count, we can keep track of the matches between each character in s1 and s2. Then, we can simply return if all the characters have the same count (number of matches is 26)

```python
# count frequencies of s1
# initialize l & r

# increment r and count frequencies until size of s1 is reached
# initialize matches
# count matches in first window instance

# while r is less than the length of s2 starting at length of s1
#   if matches == 26 return True
#   increment the running count
#   if the running count is equal to s1 count
#       increment matches
#   otherwise if s1 count + 1 == running count # we use the +1 rather than > so we don't repeatedly decrement matches
#       decrement

#   decrement running count for left
#   if the count of left pointer is equal to s1 count
#       increment matches
#   otherwise if s1 count - 1 == running count
#       decrement

# return matces == 26 # the condition isn't checked for the last iteration
```
