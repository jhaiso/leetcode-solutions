# 2402. Meeting Rooms III

## Relevant Topics

Array, Sorting, Hash Map, Heap Priority Queue

## Solution Thought Process

Because the meetings occur in chronological order by start time (and all the start times are uniqeu), we should sort the initial array. We keep track of the rooms utilizing 2 different data structures.

1. We use a binary array to keep track of whether or not the rooms are occupied.
2. We keep the meetings in a min priority queue sorted by end time.

```python
# declare a hashmap to act as a counter for the meetings held in the rooms
# sort the given array
# declare a pq for the available rooms
# declare a pq for (end, room)

# for each meeting
#   if the length of the pq >= n
#       pop from the heap
#       if the end time is greater than the start time of the next meeting
#           "delay" the meeting
#   add to priority queue
#   increment first available room in counter and pop from rooms
# return the largest value in the counter
```