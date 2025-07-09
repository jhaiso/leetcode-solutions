# 3439. Reschedule Meetings for Maximum Free Time I

## Relevant Topics

Array, Greedy, Sliding Window

## Solution Thought Process

Since the meetings must remain non-overlapping and in the same order, any contiguous subarray of length <= k+2 (+2 comes from the events on the end that cannot be moved) has a maximum continuous free time of the total free time between all the events (kinda like parting the sea lol). Therefore, we keep a sliding window of size k+2, and we keep a running count of the total possible free time!

```python
# initialize variable to keep track of result
# initialize left pointer
# initialize variable for running count of free time
# for each event in the array
#   if the size of the window is greater than k+2
#       increment left
#   update running count
#   update result
```
