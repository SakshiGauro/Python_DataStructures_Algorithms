# LL: Interview/LeetCode Exercise

## Find Middle Node

The objective is to find the middle node of a singly linked list efficiently, without using a length variable and with only one traversal.

### Requirements
- Use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.
- When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.
- Return the middle node when the number of nodes is odd or the first node of the second half of the list if the list has an even number of nodes.
- The method should only traverse the linked list once.

### Code Implementation

```
def find_middle_node (self):
    slow = self.head
    fast = self.head
    
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        
    return slow
```

### Explanation

- Initialize two pointers, `slow` and `fast`: `slow` will move **one node** at a time, while `fast` will move **two nodes**. By the time fast reaches the end, `slow` will be at the **middle**.
- `while fast is not None and fast.next is not None:`: This loop ensures that we continue as long as fast and the node after fast (fast.next) are not `None`.
- Move the slow pointer one node and the fast pointer two nodes.
- Return the node the slow pointer is currently at.

---

## Has Loop

The objective is to detect if there is a cycle or loop present in the linked list.

### Requirements
- Use a two-pointer approach, where one pointer (`slow`) moves one node at a time and the other pointer (`fast`) moves two nodes at a time.
- If there is a loop in the list, the `fast` pointer will eventually **meet** the `slow` pointer. If this occurs, the method should return `True`.
- If the fast pointer reaches the end of the list or encounters a `None` value, it means there is **no loop** in the list. In this case, the method should return `False`.
- The method should only traverse the linked list once.

### Code Implementation

```
def has_loop (self):
    slow = self.head
    fast = self.head
    
    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        
        if (slow == fast): # it is a loop!
            return True
            
    return False
```

### Explanation

- Initialize two pointers, `slow` and `fast`: `slow` will move **one node** at a time, while `fast` will move **two nodes**.
- `while fast is not None and fast.next is not None:`: This loop ensures that we continue as long as fast and the node after fast (fast.next) are not `None`.
- Move the slow pointer one node and the fast pointer two nodes.
- Check if the slow pointer meets the fast pointer.
  - If there's a loop, the fast pointer will eventually catch up to the slow pointer inside the loop. When they meet (point to the same node), we've found a loop, and the function returns `True`.
- Return `False` if no loop is found.

---

## Kth Node from End

The objective is to find the kth node of a singly linked list efficiently, without using a length variable and with only one traversal.

Given this LinkedList:

`1 -> 2 -> 3 -> 4 -> 5`

- If `k=1` then return the first node from the end (the last node) which contains the value of `5`.
- If `k=2` then return the second node from the end which contains the value of `4`, etc.

### Requirements
- Use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves kth nodes at a time.
- When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the `kth` node of the list.
- If the fast pointer becomes `None` before moving `k` nodes, the function should return `None`, as the list is shorter than `k` nodes.
- The method should only traverse the linked list once.

### Code Implementation

```
def find_kth_from_end(ll, k):       
    slow = ll.head
    fast = ll.head
    
    for _ in range(k): # move k nodes
        if (fast is None): # list is shorter than k nodes
            return None
        fast = fast.next
            
    while(fast is not None):
        slow = slow.next # move one node 
        fast = fast.next
        
    return slow
```

### Explanation

- Initialize two pointers, `slow` and `fast`: `slow` will move **one node** at a time, while `fast` will move **kth nodes**. By the time fast reaches the end, `slow` will be at the **kth node from the end**.
- `if (fast is None):`: While moving the fast pointer `k` steps, we find that fast becomes `None`, it means that the linked list has fewer than `k` nodes.
- `while (fast is not None):`: This loop ensures that we continue as long as fast are not `None`.
- Move the slow pointer one node and the fast pointer k nodes.
- Return the node the slow pointer is currently at.

---

## Remove Duplicates

The objective is to remove nodes with duplicate values from singly linked list with only one traversal.

### Two Approaches 
#### Using a Set
This approach will have a time complexity of **O(n)**, where **n** is the number of nodes in the linked list.

#### Without using a Set
This approach will have a time complexity of **O(n^2)**, where **n** is the number of nodes in the linked list.

### Code Implementation

#### Using Set
```
def remove_duplicates(self):
    values = set()
    previous = None
    current = self.head
    while current:
        if current.value in values:
            previous.next = current.next
            self.length -= 1
        else:
            values.add(current.value)
            previous = current
        current = current.next
```

### Explanation

- `values = set()`: Initialize a set to store unique values.
- `previous = None`, `current = self.head`: The `current` pointer will traverse through the list, while `previous` will keep track of the last unique node.
- Iterate through the list to remove duplicates.
- `if current.value in values:`: If the current node's value is a duplicate, we'll bypass it by pointing the `next` attribute of the `previous` node directly to `current.next`, effectively skipping over the current node.
- Otherwise, we add it to our set (`values`) and move the `previous` pointer to point at the `current` node since it's unique.
- We update the `current` pointer to move on to the next node.

#### Without using Set
```
def remove_duplicates(self):
    if (self.length > 1):
        current = self.head
        
        while(current):
            runner = current
            while(runner.next):
                if (current.value == runner.next.value):
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
            
            current = current.next 
```

### Explanation

- `while(current):`: While loop that runs as long as current is not None. `current` is going to hold a unique value we will compare the other values to.
  - `while(runner.next):` Another while loop that runs as long as the `runner.next` is not None. 
  - `if (current.value == runner.next.value):`: Compare those two values together.
    - `runner.next = runner.next.next`, `self.length -= 1`: Values match so remove them.
  - If not, go to the `next` attribute.
- Go to the `next` attribute of current to start comparison with the rest of the list.

---

## Binary to Decimal

The objective is to convert a binary number, represented as a linked list, to its decimal equivalent. In this context, a binary number is a sequence of **0s** and **1s**.

### Requirements
- Start from the head of the linked list and use each node's value to calculate the corresponding decimal number.
- The Linked List does not have a tail or a length. 
- The method should only traverse the linked list once.

### Code Implementation

```
def binary_to_decimal (self):
    decimal_node = self.head
    decimal = decimal_node.value
    
    while(decimal_node.next):
        decimal = (decimal * 2) + (decimal_node.next.value)
        decimal_node = decimal_node.next
        
    return decimal
```

### Explanation

- Initialize two variables, `decimal_node` and `decimal`: `decimal_node` points to the head, while `decimal` stores it value.
- `while(decimal_node.next):`: This loop ensures that we continue as long as `decimal_node.next` are not `None`.
  - `decimal = (decimal * 2) + (decimal_node.next.value)`: **Multiply** existing decimal with **2** and **add** the next decimal value. 
  - set `decimal_node` to its `next` attribute.
- Return the collected `decimal` value.

---

## Partition List

The objective is to partition the list such that all nodes with values **less than** `x` come **before** nodes with values **greater than or equal to** `x`.

> **An example:** 
> 
> Linked List: `3 -> 8 -> 5 -> 10 -> 2 -> 1` `x: 5`
> 
> **Process:**
> 
> Values less than 5: 3, 2, 1
> Values greater than or equal to 5: 8, 5, 10
> 
> **Output:**
> 
> Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10

### Requirements/Tips
- Takes an integer `x` as a parameter and **modifies** the current linked list in place according to the specified criteria.
- If the linked list is empty (i.e., head is null), the function should return immediately without making any changes.
- While traversing the linked list, maintain **two separate chains**: one for values **less than x** and one for values **greater than or equal to x**.
- Must maintain the relative order of nodes.
- The method should only traverse the linked list once.

### Code Implementation

```
def partition_list (self, x):
    if (self.length > 1): # LL has more than one node
        D1 = Node(0) # less than x
        D2 = Node(0) # greater than or equal to x
        prev1 = D1
        prev2 = D2
        
        current = self.head
        while(current):
            # less than x
            if (current.value < x):
                prev1.next = current
                prev1 = prev1.next
            else:
                prev2.next = current
                prev2 = prev2.next
            
            current = current.next
        
        prev2.next = None
        prev1.next = D2.next
        self.head = D1.next
```

### Explanation

- Initialize two nodes and three pointers, `D1`, `D2`, `prev1`, `prev2` and `current`.
- `while(current):`: This loop ensures that we continue as long as current is not `None`.
  - `if (current.value < x):`: Start comparing the value with `x`.
    - connect the `current` to `prev1` (pointer that stores less than values). Move to the `next` attribute. 
  - Otherwise, value is greater than or equal to `x`.
    - connect the `current` to `prev2`(pointer that stores greater than or equal to values). Move to the `next` attribute.
- `prev2.next = None`: Set the `next` attribute of `prev2` to None (end of the LL).
- `prev1.next = D2.next`: Connect the `prev1` and `prev2` together using the `next` attribute of `D2` node. 
- `self.head = D1.next`: Reassign the head.

---

## Reverse Between

The objective is to reverse the nodes of the linked list from `start_index` to  `end_index` (inclusive using 0-based indexing) in one pass and in-place.

> **An example:**
>
> Linked List: `1 -> 2 -> 3 -> 4 -> 5` `start_index = 2`  `end_index = 4`
>
> **Output:**
>
> Linked List: 1 -> 2 -> 5 -> 4 -> 3

### Requirements
- Assumption: You can assume that `start_index` and `end_index` are not out of bounds.
- Modify the linked list in-place by reversing the nodes from `start_index` to  `end_index`.
- If the linked list is **empty** or has **only one node**, the method should return `None`.
- Does not have a tail which will make the implementation easier.
- Should only traverse the linked list once.

### Code Implementation

```
def reverse_between (self, start_index, end_index):
    if self.length <= 1: 
        return None
    
    dummy = Node(0)
    dummy.next = self.head
    prev_node = dummy
    
    for i in range(start_index):
        prev_node = prev_node.next
        
    current = prev_node.next
    for _ in range (end_index - start_index):
        node_to_move = current.next
        current.next = node_to_move.next
        node_to_move.next = prev_node.next
        prev_node.next = node_to_move
    
    self.head = dummy.next
```

### Explanation

- Check if the list is empty or has only one node, return `None`.
- Initialize one node and one pointer, `dummy` and `prev_node`: `dummy`'s next attribute points to the `head` and `prev_node` points to `dummy`.
- `for i in range(start_index):`: Start a `for loop` to iterate throught the LL (no need to revere them) until the `start_index`, the point we will start the reversing. 
- `current = prev_node.next`: `currentNode` now points to the node where our reversal starts.
- Reverse nodes between `start_index` and `end_index`.
  - `node_to_move` is next node we want to reverse.
  - Disconnect `node_to_move`, point `current_node` after it.
  - Insert `node_to_move` at new position after `previous_node`.
  - Link `previous_node` to `node_to_move`.
- `self.head = dummy.next`: Reset the head.

---

## Swap Nodes in Pairs

The objective is to swap every two adjacent nodes in the linked list by adjusting the pointers, not the node values. If the list has an odd number of nodes, the final node remains in its original position.

> **An example:**
>
> Linked List: `1 -> 2 -> 3 -> 4 -> 5` , `1 -> 2 -> 3 -> 4`
>
> **Output:**
>
> Linked List: `2 -> 1 -> 4 -> 3 -> 5`, `2 -> 1 -> 4 -> 3`

### Requirements
- Modify the list in-place and update the head accordingly.
- No return value (None); the method modifies the linked list in place.
- Handle edge cases like empty lists, single nodes, and lists with odd or even node counts.
- The method should only traverse the linked list once.

### Code Implementation

```
def swap_pairs(self):
    if (self.length > 1): # List has more than one nodes
        dummy = Node(0)
        dummy.next = self.head
        
        prev = dummy
        current = self.head
        
        while(current and current.next):
            after = current.next
            
            prev.next = after
            current.next  = after.next
            after.next = current
            
            prev = current
            current = current.next
                
        
        self.head = dummy.next
```

### Explanation

- Initialize a node, two pointers, `dummy`, `prev` and `current`: `dummy` attaches to the front of the list, `prev` points to the `dummy` node and `current` points to the **head**. 
- `while(current and current.next):`: This loop ensures that we continue as long as `current` and the node after current (`current.next`) are not `None`.
  - Store the next node of `current` to `after`. 
  - Swapping:
    - `prev.next = after`: connect the previous to after. For first instance, `dummy` points to `2`. 
    - `current.next  = after.next`: For first instance, `1` points to `3`.
    - `after.next = current`: For first instance, `2` points to `1`.
    - `dummy -> 2 -> 1 -> 3 ..`: This is what it looks like after the first loop. 
  - Update the `prev` and `current` accordingly.
- Reset the head.

---
