# 2081. Sum of k-Mirror Numbers

## Relevant Topics

Math, Enumeration

## Solution Thought Process

### Brute Force

Go through every possible number within range. If it is a palindrome in base-10, we check if it is a palindrome in base-k. Then we add.

### Enuemration

We can generate palindromes rather than checking them twice. We see that given a number x with length n, we can generate palindromes of length 2n-1 and 2n by reversing part of the number and appending it. In each case, the resulting odd palindromes are less than the even ones, so we must first generate the odd palindromes.

```python
# declare left (the starting range of the current numbers)
# declare count and answer (total mirror numbers and sum of mirror numbers)
# while count < n:
#   right = left * 10 (define the range)
#   for odd and even options
#       for i in left, right
#           if count == n,
#               break
#           combined = i
#           make odd or even palindrome
#           check if it is a base-k palindrome
#   set left to right
```
