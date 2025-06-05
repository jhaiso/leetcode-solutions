# 3. Longest Substring Without Repeated Characters

## Relevant Topics

String, Hash Table, Sliding Window

## Solution Thought Process

### Brute Force

Search Every possible substring. If there is a duplicate value, do not consider that substring.
Time Complexity: O(n^2)
Space Complexity: O(n) - set with included characters

### Two Pointer

We see that in each maximal substring without repeated characters that they are bounded by edges of the word, or repetitions of included characters (since the substring is no longer maximal if that character is included). Therefore, we can utilize a sliding window / two pointer approach. When the right side of the window reaches a character that already exists in the window, we increment the left side of the window until it is again a maximal substring.

```python
# initialize counter hashtable
# initialize left side

# for each character
#   increment the character in the counter
#   if new count > 1
#       increment left counter until it is the character
#   increment left again
#   update the maximum
#
# return the maximum
```

I'm dumb and realized that: If the condition is whether or not the current substring contains 1 of each character, then I can simply use a hashset to keep track of the characters...

```python
# initialize longest length
# initialize set
# initialize left

# for each character
#   while the character is in the set
#       remove left and increment left
#   add character back into set
#   update longest

# return longest

```

Time Complexity: O(n)
Space Complexity: O(n) - hashtable counter to check if substring is maximal
