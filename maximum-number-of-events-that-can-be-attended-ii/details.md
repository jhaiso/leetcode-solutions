# 1751. Maximum Number of Events That Can Be Attended II

## Relevant Topics

Array, Sorting, Binary Search, Dynamic Programming

## Solution Thought Process
This problem involves a series of choices, each depended on the previous one. Additionally, we are looking for an optimal sum. Therefore, DP comes to mind. We sort the events by start time, and for each event, we can either choose to include or exclude it in our schedule. We can utilize binary search to find the next available event!

Time Complexity: O(n * (k + logn))
Space Complexity: O(n*k)