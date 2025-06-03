# 853. Car Fleet
## Relevant Topics
Stack, Sorting
## Solution Thought Process
### Stack
This is effectively a "next smaller" time of arrival problem. When the cars are arranged by position in reverse order (i.e. from finish line to last car), if a subsequent car has a smaller time of arrival, it cannot pass the car in front of it and can effectively be removed from consideration in the fleet. Therefore, we can utilize a stack, and each time a car has a smaller arrival time than the car ahead of it, it can be popped!
```python
# initialize stack
# sort cars by position in reverse order

# iterate through the cars
#   push
#   if the arrival time of recent car is less than or the same as the second most recent car
#     pop! ()

# return the size of the stack
```