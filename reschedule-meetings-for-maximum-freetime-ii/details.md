# 3440. Reschedule Meetings for Maximum Free Time II

## Relevant Topics

Array, Greedy, Enumeration

## Solution Thought Process

For each meeting, there are 2 cases:

1. The meeting can be moved to an available slot outside the adjacent meetings
2. The meeting cannot be moved outside the adjacent meetings

In case 1, the new free time becomes the existing adjacent freetime with the addition of the time of the moved event. In case 2, the new free time becomes the sum of the adjacent free times (since the event can just be shifted). 

We need to keep track of the free times! We can do this by keeping an array status[i] where each value indicates if the meeting can be moved. We iterate forwards and backwards through the array, and at each meeting, we compare its length to the longest we've seen so far to see if we can move it.

```python
# iterate fowards and backwards through the meetings to get the statuses
# iterate through the meetings to get result based on cases
```
Time Complexity: O(n)
Space Complexity: O(n)