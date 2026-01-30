# Heap: Interview/LeetCode Exercise

## Kth Smallest Element in an Array

The objective is to write a function `find_kth_smallest(nums, k)` to find the `kth` smallest number in the list.

The list can contain duplicate numbers and `k` is guaranteed to be within the range of the length of the list.

> **An example:**
>
> nums = `[3, 2, 1, 5, 6, 4]`, k = `2` 
> 
> sorted -> `[1, 2, 3, 4, 5, 6]`, output = `2`. 
> 
> nums = `[3, 2, 3, 1, 2, 4, 5, 5, 6]`, k = `4`
>
> sorted -> `[1, 2, 2, 3, 3, 4, 5, 5, 6]`, output = `3`.

### Code Implementation

```
def find_kth_smallest(nums, k):
    my_heap = MaxHeap()
    
    for num in nums: 
        my_heap.insert(num)
        if len(my_heap.heap) > k: 
            my_heap.remove()
            
    return my_heap.remove()
```

### Explanation

- Initialize a heap.
- Iterate through each number in the array. 
  - Insert the number in the heap. 
  - Check if the length of heap is greater than k. 
    - Remove the root of the heap. 
- After the loop ends, the root would be the kth smallest item. Return it. 

---

## Maximum Element in a Stream

Write a function named `stream_max` that takes as its input a list of integers (`nums`). The function should return a list of the same length, where each element in the output list is the maximum number seen so far in the input list.

More specifically, for each index i in the input list, the element at the same index in the output list should be the maximum value among the elements at indices 0 through i in the input list.


### Code Implementation

```
def stream_max(nums):
    my_heap = MaxHeap()
    max_stream = []
    
    for num in nums:
        my_heap.insert(num)
        max_stream.append(my_heap.heap[0])

    return max_stream
```

### Explanation

- Initialize a heap and an array.
- Iterate through each number in the array.
    - Insert the number in the heap.
    - Append the root of the heap to the array. The root stores the largest number.
- After the loop ends, return the array.

---
