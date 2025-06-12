# 3423. Maximum Difference Between Adjacent Elements in a Circular Array
## Relevant Topics
Array

## Solution Thought Process
We iterate through the array, and at each index, we compare the value at that index to the value at the next index.
Time Complexity: O(n)
Space Complexity: O(1) OR O(n) if negative indices don't circle back to the end of the array and an array must be created with the first number appended.