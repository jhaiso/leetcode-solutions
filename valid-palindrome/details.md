# 125. Valid Palindrome
## Relevant Topics
Two-Pointer

## Solution Thought Process
### Brute Force
Reverse the string and check if it is the same.
Time Complexity: O(n)
Space Complexity: O(n)

### Two-Pointer
We see that palindromes are symmetric about the middle of the string. We can start a pointer at the beginning of the string, and another at the end and compare the character at each until the reach the middle.
Time Complexity: O(n)
Space Complexity: O(1)