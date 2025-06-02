# 347. Top K Frequent Elements
## Relevant Topics
Arrays, Hash Table, Sorting, Heap, Bucket Sort

## Solution Thought Process
### Brute Force/ Sorting:
```python
# initialize a hash table as a frequency counter
# iterate through all elements and count for frequency

# sort by frequency
# pop elements from end until k elements are found
```
Time Complexity: O(nlogn)
Space Complexity: O(n)

### Min Heap:
When considering a maximum/minimum k elements problem, a heap should always be considered, as heapification takes only O(logn) time.

```python
# initialize min heap
# initialize counter hash table
# iterate through elements
#   increase count

# for each element in counter
#   remove minimum if size >= k (reduces push time)
#   insert into heap

# pop from heap until k elements
```

Time Complexity: O(nlogk) - each element is pushed onto a heap of size k
Space Complexity: O(n + k)
### Bucket Sort:
Because there is n elements, the frequency is limited to n. Therefore, since the elements can be returned in ANY ORDER the elements can be placed into buckets of frequency!
```python
# initialize frequency counter
# count frequencies

# initialize buckets
# iterate through frequency counter (element, frequency)
#   add element to bucket[frequency]

# iterate through buckets in descending order
#   add element to result
#   return result if size of result = k
```