# LL: Interview/LeetCode Exercise

## Palindrome Checker

The objective is to determine whether a given doubly linked list reads the same forwards and backwards.

> **An example:**
>
> Doubly Linked List: `[1, 2, 3, 2, 1]` **# True**
> 
> Doubly Linked List: `[1, 2, 3, 4, 5]` **# False**

### Code Implementation

```
def is_palindrome(self):
    if (self.length == 0 or self.length == 1): # empty list and one item 
        return True
    
    forward = self.head
    backward = self.tail
    for _ in range(int(self.length/2)): 
        if (forward.value != backward.value):
            return False
        forward = forward.next
        backward = backward.prev
    return True
```

### Explanation

- Initialize two pointers, `forward` and `backward`: `forward` will move from the head, while `backward` will move from the tail.
- `for _ in range(int(self.length/2)):`: This loop ensures that we only loop half of the list.
- `if (forward.value != backward.value):`: If at any point the `forward` and `backwards` are **not equal**, return `False` since it's **not a palindrome**. 
- `forward = forward.next`, `backward = backward.prev`: Move the forward using the `next` attribute and backwards with the `prev` attribute.
- Return `True` after it goes through the loop.

---

## Reverse

The objective is to reverse the order of the nodes in the list, i.e., the first node becomes the last node, the second node becomes the second-to-last node, and so on.

### Requirements
- Change the direction of the pointers between the nodes so that they point in the opposite direction.
- Do not change the value of any of the nodes.
- Update the head and tail pointers to reflect the new order of the nodes.

### Code Implementation

```
def reverse(self):
    if (self.length > 1): # only run this for more than one item
        current = self.head
        temp = None
        
        while(current):
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        temp = self.head
        self.head = self.tail
        self.tail = temp
```

### Explanation

- Initialize two variables, `current` and `temp`: `current` points to the head, while `temp` stores temporary value during the switch.
- `while(current):`: This loop ensures that we continue as long as `current` is not `None`.
    - `temp = current.prev`: store the previous node
    - `current.prev = current.next`, `current.next = temp`: Flip the `next` and `prev` attributes
    - `current = current.prev`: set new current node
- Reset the `head` and `tail`. 

---

## Partition List

The objective is to partition the list such that all nodes with values **less than** `x` come **before** nodes with values **greater than or equal to** `x`.

> **An example:**
>
> Linked List: `3 <-> 8 <-> 5 <-> 10 <-> 2 <-> 1` `x: 5`
>
> **Process:**
>
> Values less than 5: 3, 2, 1
> Values greater than or equal to 5: 8, 5, 10
>
> **Output:**
>
> Linked List: 3 <-> 2 <-> 1 <-> 8 <-> 5 <-> 10

### Requirements/Tips
- Takes an integer `x` as a parameter and **modifies** the current linked list in place according to the specified criteria.
- If the linked list is empty (i.e., head is null), the function should return immediately without making any changes.
- While traversing the linked list, maintain **two separate chains**: one for values **less than x** and one for values **greater than or equal to x**.
- Must maintain the relative order of nodes.
- The method should only traverse the linked list once.

### Code Implementation

```
def partition_list(self, x):
    if (self.length > 1):
        D1 = Node(0)
        D2 = Node(0)
        dummy1 = D1
        dummy2 = D2
        
        current = self.head
        while(current):
            if(current.value < x):
                dummy1.next = current
                current.prev = dummy1
                dummy1 = dummy1.next
                
            else:
                dummy2.next = current
                current.prev = dummy2
                dummy2 = dummy2.next
            
            current = current.next
        
        dummy1.next = D2.next
        if (D2.next):   
            D2.next.prev = dummy1
        dummy2.next = None
        self.head = D1.next
        self.head.prev = None
```

### Explanation

- Initialize two nodes and three pointers, `D1`, `D2`, `dummy1`, `dummy2` and `current`.
- `while(current):`: This loop ensures that we continue as long as current is not `None`.
    - `if (current.value < x):`: Start comparing the value with `x`.
        - connect the `current` to `dummy1` (pointer that stores less than values). Do this with both `prev` and `next` attributes.
    - Otherwise, value is greater than or equal to `x`.
        - connect the `current` to `dummy2`(pointer that stores greater than or equal to values). Do this with both `prev` and `next` attributes.
    - Move the `next` node.
- `dummy1.next = D2.next`: Connect the first chain to the second. 
- `if (D2.next):`, `D2.next.prev = dummy1`: Is the second chain is not `None`, connect the `prev` attribute as well. 
- `dummy2.next = None`: Set the `next` attribute of `prev2` to None (end of the LL).
- `self.head = D1.next`: Reset head. 
- `self.head.prev = None`: Detach the head's prev attribute.

---

## Reverse Between

The objective is to reverse the nodes of the linked list from `start_index` to  `end_index` (inclusive using 0-based indexing) in one pass and in-place.

> **An example:**
>
> Linked List: `1 <-> 2 <-> 3 <-> 4 <-> 5` `start_index = 2`  `end_index = 4`
>
> **Output:**
>
> Linked List: 1 <-> 2 <-> 5 <-> 4 <-> 3

### Requirements
- Indexing is zero-based.
- Modify the linked list in-place by reversing the nodes from `start_index` to  `end_index`.
- If the linked list is **empty** or has **only one node**, the method should return `None`.
- Make sure the list remains fully connected after the reversal in both directions.
- Does not have a tail which will make the implementation easier.
- Should only traverse the linked list once.

### Code Implementation

```
def reverse_between(self, start_index, end_index):
    if (start_index < 0 or end_index > self.length or self.length <= 1): # IOOB and only one item in list
        return None
    
    dummy = Node(0)
    dummy.next = self.head
    prev_node = dummy
    
    for _ in range (start_index):
        prev_node = prev_node.next
    
    current = prev_node.next
    
    for _ in range (end_index - start_index):
        node_to_move = current.next
        
        current.next = node_to_move.next
        if node_to_move.next:
            node_to_move.next.prev = current
        
        node_to_move.next = prev_node.next
        prev_node.next.prev = node_to_move
        
        prev_node.next = node_to_move
        node_to_move.prev = prev_node
        
    self.head = dummy.next
    self.head.prev = None
```

### Explanation

- Check if the list is empty, invalid start_index or end_index, or has only one node, return `None`.
- Initialize one node and one pointer, `dummy` and `prev_node`: `dummy` gets attached to the `head` and `prev_node` points to `dummy`.
- `for i in range(start_index):`: Start a `for loop` to iterate throught the DLL (no need to reverse them) until the `start_index`, the point we will start the reversing.
- `current = prev_node.next`: `currentNode` now points to the node where our reversal starts.
- Reverse nodes between `start_index` and `end_index`.
    - `node_to_move` is next node we want to reverse.
    - Connect the next attribute of `node_to_move` to the next attribute of `current_node`. Do the same with prev attribute if it's possible (the next attribute is not None).
    - Insert `node_to_move` at new position after `previous_node`. Do the same with prev attribute.
    - Link `previous_node` to `node_to_move`. Do the same with prev attribute.
- `self.head = dummy.next`: Reset the head.
- `self.head.prev = None`: Detach the prev attribute. 

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
- The method should only traverse the list once.

### Code Implementation

```
def swap_pairs (self):
    if (self.length > 1): # list has more than 1 Node
        dummy = Node(0)
        dummy.next = self.head
        
        prev = dummy
        current = self.head
        
        while(current and current.next): 
            after = current.next
            
            prev.next = after
            after.prev = prev
            
            current.next = after.next
            after.prev = current
            
            after.next = current
            current.prev = after
            
            prev = current
            current = current.next
        
        self.head = dummy.next
        dummy.next = None
        self.head.prev = None
```

### Explanation

- Initialize a node, two pointers, `dummy`, `prev` and `current`: `dummy` attaches to the front of the list, `prev` points to the `dummy` node and `current` points to the **head**.
- `while(current and current.next):`: This loop ensures that we continue as long as `current` and the node after current (`current.next`) are not `None`.
    - Store the next node of `current` to `after`.
    - Swapping:
        - `prev.next = after`, `after.prev = prev`: Connect the previous to after. For first instance, `dummy` points to `2`.
        - `current.next  = after.next`, `current.prev = after`: For first instance, `1` points to `3`.
        - `after.next = current`, `current.prev = after`: For first instance, `2` points to `1`.
        - `dummy <-> 2 <-> 1 <-> 3 ..`: This is what it looks like after the first loop.
    - Update the `prev` and `current` accordingly.
- Reset the head. Detach the prev attributes. 

---
