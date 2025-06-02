# 150. Evaluate Reverse Polish Notation

## Relevant Topics

Stack

## Solution Thought Process

Because the operator comes after the operands, after we see an operand, we only need the two most recent values. Therefore, we can utilize a stack.

```python
# initialize stack
# for each element in the array
#   push if not operator
#   otherwise pop 2x and perform the operation on the two values
```