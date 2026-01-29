# Heaps

A heap (also called a priority queue) is a special data structure that allows quick access to the smallest (min-heap) or largest (max-heap) element. They are arranged in a such a way that the parent is always larger or smaller than its child.

### Big 0:
highest value remove
BST: Log(n) but not always balanced
heap is always balanced. Add or remove O(logn)

| Operation          | Heap (Binary)                           | Balanced BST | Unbalanced BST |
|--------------------|-----------------------------------------|--------------|----------------|
| Find Min/Max       | `O(1)`                                  | `O(log n)`   | `O(n)`         |
| Search (arbitrary) | `O(n)`                                  | `O(log n)`   | `O(n)`         |
| Insert             | `O(log n)` _(worst)_ `O(1)` _(average)_ | `O(log n)`   | `O(n)`         |
| Delete             | `O(log n)`                              | `O(log n)`   | `O(n)`         |
| Build              | `O(n)`                                  | `O(n log n)` | `O(n²)`        |

---

## MaxHeap: Insert
The `insert` method should take an integer as input and add it to the heap. The insertion of a new element should preserve the Max Heap property, i.e., for every node `i` other than the root, the value of node `i` is less than or equal to the value of its parent, with the maximum value at the root of the heap. It should ideally achieve a time complexity of `O(log n)`, where n is the number of elements in the heap.

### Code Implementation
```
def insert (self, value):
    self.heap.append(value)
    current = len(self.heap) - 1 
    
    while(current > 0 and self.heap[current] > self.heap[self._parent(current)]):
        self._swap(current, self._parent(current))
        current = self._parent(current)
```

### Explanation

- Append the new value to the heap. 
- Set the current to the last element of the heap. 
- Start a loop that continues while **current is not the root** and the **value at current is greater than its parent**.
  - Swap values at the current with its parents. 
  - Move the tracking index so the current is in the index of its parents.

---

## MaxHeap: Remove
This method should remove the maximum element from the heap, i.e., the root element, and reorganize the heap, so it maintains its max heap property. The max heap property states that for any given node i other than the root, the value of i is at most the value of its parent.

### Code Implementation
```
def remove(self):
    if len(self.heap) == 0: # empty
        return None
    elif len(self.heap) == 1: # only one item
        return self.heap.pop()
    max_value = self.heap[0]    
    self.heap[0] = self.heap.pop()
    self._sink_down(0)
    return max_value
```

### Explanation
- If the heap is **empty**, the remove method returns `None`.
- If the heap has **only one element**, the remove method removes and return this element.
- Set the `max_value` to be the **root** of the heap (largest item). 
- Set the root to be the item at the last index of the heap. 
- Call the `sinkdown` method to reorganize the heap, maintaining the max heap property.
- Return the `max_value`. 

---

## MaxHeap: Sink Down
Implement the `_sink_down` helper method in the `MaxHeap` class. This method is a private helper method that is crucial to maintaining the max heap property when the root element is removed from the heap.

### Code Implementation
```
def _sink_down(self, index): 
    max_index = index
    
    while True: 
        left_index = self._left_child(index)
        right_index = self._right_child(index)
        
        if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]): 
            max_index = left_index
        
        if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]): 
            max_index = right_index
            
        if max_index != index:
            self._swap(max_index, index)
            index = max_index
        else:
            return
```

### Explanation
- Set the `max_index` to the current `index`. Both of them should point to the **root of the heap**. 
- Run an _infinite while loop_. We will be breaking out of it later!
  - Find the `left_index` and `right_index` for that index. 
  - Essentially, we now check if either the left child or the right child is larger than the parent. 
  - If the `left_index` is a **valid** index (aka less than the size of the heap) **AND** the value of the `left_index` is **larger** than the value of `max_index`.
    - Set the max_index to be that left child. 
  - If the `right_index` is a **valid** index **AND** value of the `right_index` is **larger** than the value of `max_index`.
      - Set the max_index to be that right child.
  - If `max_index` and the `index` are **NOT EQUAL.**
    - Swap those two and update the index. 
  - Otherwise, (which means the index is bigger than the child)
    - Return which means to **break out** of the infinite loop. 

---

## MinHeap: Insert
The `insert` method should take an integer as input and add it to the heap. The insertion of a new element should preserve the Min Heap property, i.e., for every node i other than the root, the value of node i is greater than or equal to the value of its parent, with the minimum value at the root of the heap. It should ideally achieve a time complexity of `O(log n)`, where n is the number of elements in the heap.

### Code Implementation
```
def insert(self, value): 
    self.heap.append(value)
    current = len(self.heap) - 1 
    
    while (current > 0 and self.heap[current] < self.heap[self._parent(current)]):
        self._swap(current, self._parent(current))
        current = self._parent(current)
```

### Explanation

- Append the new value to the heap.
- Set the current to the last element of the heap.
- Start a loop that continues while **current is not the root** and the **value at current is smaller than its parent**.
    - Swap values at the current with its parents.
    - Move the tracking index so the current is in the index of its parents.

---

## MinHeap: Remove
This method should remove the minimum element from the heap, i.e., the root element, and reorganize the heap so it maintains its min heap property. The min heap property states that for any given node i other than the root, the value of i is at most the value of its parent.

### Code Implementation
```
def remove(self): 
    if len(self.heap) == 0: # empty
        return None
    elif len(self.heap) == 1: # only one item
        return self.heap.pop()
    
    min_val = self.heap[0]
    self.heap[0] = self.heap.pop()
    self._sink_down(0)
    return min_val
```

### Explanation
- If the heap is **empty**, the remove method returns `None`.
- If the heap has **only one element**, the remove method removes and return this element.
- Set the `min_val` to be the **root** of the heap (largest item).
- Set the root to be the item at the last index of the heap.
- Call the `sinkdown` method to reorganize the heap, maintaining the max heap property.
- Return the `min_val`.

---

## MinHeap: Sink Down
Implement the `_sink_down` helper method in the `MinHeap` class. This method is a private helper method that is crucial to maintaining the min heap property when the root element is removed from the heap.

### Code Implementation
```
def _sink_down(self, index):
    min_index = index
    
    while (True):
        left_index = self._left_child(index)
        right_index = self._right_child(index)
        
        if (left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]):
            min_index = left_index
        
        if (right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]): 
            min_index = right_index
            
        if min_index != index:
            self._swap(index, min_index)
            index = min_index
        else:
            return
```

### Explanation
- Set the `min_index` to the current `index`. Both of them should point to the **root of the heap**.
- Run an _infinite while loop_. We will be breaking out of it later!
    - Find the `left_index` and `right_index` for that index.
    - Essentially, we now check if either the left child or the right child is **smaller** than the parent.
    - If the `left_index` is a **valid** index (aka less than the size of the heap) **AND** the value of the `left_index` is **smaller** than the value of `min_index`.
        - Set the min_index to be that left child.
    - If the `right_index` is a **valid** index **AND** value of the `right_index` is **smaller** than the value of `min_index`.
        - Set the min_index to be that right child.
    - If `min_index` and the `index` are **NOT EQUAL.**
        - Swap those two and update the index.
    - Otherwise, (which means the parent is smaller than the child)
        - Return which means to **break out** of the infinite loop.

---

_source: https://www.geeksforgeeks.org/python/heap-queue-or-heapq-in-python/_

---




