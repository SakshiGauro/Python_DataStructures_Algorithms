# Queue

A **queue** is a linear data structure that follows the **First-In-First-Out (FIFO)** principle.

Like a queue of people in line for a ticket, the person first in line, pays first and leaves first.  

**Basic operations:**
- Enqueue: Adds a new element to the queue.
- Dequeue: Removes and returns the first (front) element from the queue.
- Peek: Returns the first element in the queue.
- isEmpty: Checks if the queue is empty.
- Size/Length: Finds the number of elements in the queue.

**How to implement a queue?**
Queue can be implemented by using arrays or linked lists.

- Using Arrays:
  - Add and remove from the different end, preferably from the tail and remove from the head. 
  - Memory Efficient: The elements do not hold the next elements address like linked list nodes do.
  - Fixed Size: The maximum capacity must be defined at the start and cannot grow dynamically, which can lead to overflow.
- Using LinkedLists:
  - Dynamic size as the queue can grow and shrink dynamically, unlike with arrays.
  - The head becomes the first and the tail becomes the last.

---

## Constructor
This section introduces the **constructor** for a queue. The goal is to initialize a queue with a single node while properly setting up internal pointers.

### Requirements

**Node Class**
- A constructor that accepts a `value`
- A `value` attribute to store data
- A `next` attribute initialized to `None` (pointer to the next node)

**Queue Class**
- A constructor that accepts a `value`
- Creates a new `Node` using that value
- Initializes:
  - `first` → the start of the queue
  - `last` → the end of the queue
- Initializes `length` to `1`

### Code Implementation
```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
```

### Explanation

**Node Class**
- `class Node:`: Defines the `Node` class, which represents a single element in the queue.
- `def __init__(self, value):`: Constructor for the `Node` class called when you create a new instance.
- `self.value = value`: Stores the data passed into the node.
- `self.next = None`: Initializes the pointer to the next node as `None`. A new node does not point to anything yet.

**Queue Class**
- `class Queue:`: Defines the **Queue** class, which manages nodes and pointers.
- `def __init__(self, value):`: Constructor for the queue class.
- `new_node = Node(value)`: Creates the first node in the queue.
- `self.first = new_node`: Sets the start (first) of the queue to the new node.
- `self.last = new_node`: Sets the end (last) of the queue to the new node.
- `self.length = 1`: Tracks the number of nodes in the queue. Starts at 1 because one node exists.

---

## Enqueue
The `enqueue ` method adds a **new node to the end** of the queue.

### Requirements
- Handle the cases where the list is empty
- Create a new `node`
- Update the current node's `next` pointer
- Update the `last`
- Increment `length`

### Code Implementation
```
def enqueue(self, value):
    new_node = Node(value)
    if self.length == 0: # empty
        self.first = new_node
        self.last = new_node
    else:
        self.last.next = new_node
        self.last = new_node
    self.length += 1
```

### Explanation
- `new_node = Node(value)` → Create a new node.
- `if self.height == 0:` → Check if the queue is empty.
  - If the queue is empty, set the `first` and `last` to point at `new_node`.
- `self.last.next = new_node` → Update the next attribute of the current last node to point to the new node.
- `self.last = new_node` → Update the last attribute of the Queue class to point to the new node.
- `self.length += 1` → Increment the length of the queue by 1.

---

## Dequeue
The `dequeue` method should remove the first node from the queue and returns it. If the list is **empty**, the method should return `None`.

### Requirements
- Handle the cases where the list is empty, has only one node, or has multiple nodes
- Update the `first` attribute
- Update the `length` attribute
- Return either the removed node or `None` if the list is **empty**.

### Code Implementation
```
def dequeue(self):
    if self.length == 0: # empty
        return None
    temp = self.first
    if self.length == 1: # only 1 Item
        self.first = None
        self.last = None
    else: 
        self.first = self.first.next
        temp.next = None
    self.length -= 1 
    return temp
```

### Explanation
- `if (self.height == 0):` → List is empty, return `None`.
- `temp = self.first` → Store a reference to the current first node in a temporary variable
- If the queue has only one item
  - Set the `first` and `last` to None.
- `self.first = self.first.next` → Update the first attribute of the queue class to point to the next node in the queue.
- `temp.next = None` → Set the next attribute of the removed node (stored in the temporary variable) to None.
- `self.length -= 1`, `return node` → Decrements the length and returns the node.

---
