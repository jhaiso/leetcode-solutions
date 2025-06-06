# 74. Minimum Window Substring

## Relevant Topics

String, Hash Table, Sliding Window

## Solution Thought Process
### Brute Force Solution
Generate all possible substrings, count the characters in each. If the condition is met, compare to current minimum.
Time Complexity: O(n^3), finding all substrings O(n^2), counting frequencies O(n)

### Sliding Window
In addition to the name of the problem having window in it, we are exploring substrings/subsequences to find a single minimum/maximum, so sliding window comes to mind. My initial thoughts are that we should maintain the condition that all the characters in t are in the substring, but how can we do this?

 - have a loop invariant such that the substring in the window includes all the characters from t
 - we maintain this invariant by moving the right pointer until the condition is met
 - HERE is where the loop invariant holds true, so we compare minimums
 - moving the left pointer until condition is no longer met

 This would still be O(n^2) time complexity, so I'm thinking there's a better way than comparing the hashtables directly. Maybe we keep track of a variable keeping track of how many of the character conditions are met? Then each time we see a character, we update the counts, and update the conditions variable accordingly.

 Therefore, the time complexity would be O(n) (yayyy), and the space complexity would be O(m), where m is the number of distinct characters in t. Maybe we could use arrays with length of 26 as well for O(1) space (?)

 ```python
 # if t is empty, return empty string

 # count the characters in t
 
 # initialize left and right pointers
 # initialize met conditions
 # initialize count for s
 
 # for each character in s (right pointer)
 #  update the counts and met conditions
 #  if met conditions is the length of count of t
 #      increment left pointer until condition no longer holds
 #      compare to minimum

 # return the minimum
 ```