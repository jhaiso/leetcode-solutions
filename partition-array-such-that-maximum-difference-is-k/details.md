# 2294. Partition Array Such That Maximum Difference is K

## Relevant Topics

Array, Sorting, Greedy

## Solution Thought Process

### Sorting/Greedy
After looking at the examples, my first instinct would be sorting (since numbers are grouped by closeness). We also see that it exhibits the greedy choice property: If the minimum value of a group is start, then the range for that group would be [start, start + k]. Removing any from the group would strictly not decrease the number of gruops.