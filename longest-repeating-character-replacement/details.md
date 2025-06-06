# 424. Longest Repeating Character Replacement

## Relevant Topics

Sliding Window

## Solution Thought Process

### Brute Force

Look at every possible substring, if the conditions are met, then compare against the largest.
Time Complexity: O(n^2)

### Sliding Window

We see that for the condition to be met, the count of all characters except for the most frequent must be <= k. We can utilize a sliding window to maintain this condition. We expand the window until the condition is not met, and then contract it until the condition is met again. We can utilize a hashtable to keep track of the counts

```python
# initialize count hashtable
# initialize left pointer
# initialize largest frequencey (we don't acutally need to know the most frequent character
#                               just the largest frequency so we know when the condition is met)

# for each character in the string
#   increment the count of the character
#   update the maximum
#   
#   while size of the window - maximum > k (checking condition)
#       decrement count of char at left pointer
#       increment left pointer
#   update result

# return result
```
