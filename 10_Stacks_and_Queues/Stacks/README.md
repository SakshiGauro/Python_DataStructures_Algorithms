# Stack

A **stack** is a data structure that can hold many elements, and the last element added is the first one to be removed.

Like a pile of pancakes, the pancakes are both added and removed from the top. So when removing a pancake, it will always be the last pancake you added. This way of organizing elements is called **LIFO: Last In First Out**.

**Basic operations:**
- Push: Adds a new element on the stack.
- Pop: Removes and returns the top element from the stack.
- Peek: Returns the top (last) element on the stack.
- isEmpty: Checks if the stack is empty.
- Size/Height: Finds the number of elements in the stack.

**How to implement a stack?**
Stacks can be implemented by using arrays or linked lists.

- Using Arrays:
  - Add and remove from the same end, preferably from the tail to get a time complexity of **O(1)**. 
  - Memory Efficient as the elements do not hold the next elements address like linked list nodes do.
- Using LinkedLists: 
  - Dynamic size as the stack can grow and shrink dynamically, unlike with arrays.
  - The head becomes the top and the tail becomes the bottom with time complexity of **O(1)**.

---

## Constructor
This section introduces the **constructor** for a stack. The goal is to initialize a stack with a single node while properly setting up internal pointers.

### Requirements

**Node Class**
- A constructor that accepts a `value`
- A `value` attribute to store data
- A `next` attribute initialized to `None` (pointer to the next node)

**Stack Class**
- A constructor that accepts a `value`
- Creates a new `Node` using that value
- Initializes:
    - `top` → the top of the stack
- Initializes `length` to `1`

### Code Implementation
```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
```

### Explanation

**Node Class**
- `class Node:`: Defines the `Node` class, which represents a single element in the stack.
- `def __init__(self, value):`: Constructor for the `Node` class called when you create a new instance.
- `self.value = value`: Stores the data passed into the node.
- `self.next = None`: Initializes the pointer to the next node as `None`. A new node does not point to anything yet.

**Stack Class**
- `class Stack:`: Defines the **Stack** class, which manages nodes and pointers.
- `def __init__(self, value):`: Constructor for the Stack class called when you create a new instance of the Stack class.
- `new_node = Node(value)`: Creates the first node in the stack.
- `self.top = new_node`: Sets the top of the stack to the new node.
- `self.height = 1`: Tracks the number of nodes in the stack. Starts at 1 because one node exists.

---

## Push
The `push` method adds a **new node to the beginning** of the stack and changes the top accordingly. 

### Requirements
- Handle the cases where the list is empty
- Create a new `node`
- Update the current node's `next` pointer
- Update the `top`
- Increment `length`

### Code Implementation
```
def push(self, value):
    new_node = Node(value)
    if self.height == 0:
        self.top = new_node
    else:
        new_node.next = self.top
        self.top = new_node
    self.height += 1
```

### Explanation
- `new_node = Node(value)` → Create a new node.
- `if self.height == 0:` → Check if the stack is empty.
    - If the stack is empty, set the `top` to point at `new_node`.
- `new_node.next = self.top` → Update the next attribute to the top.
- `self.top = new_node` → Update the top attribute of the Stack class to point to the new node.
- `self.length += 1` → Increment the length of the stack by 1.

---

## Pop
The `pop` method should remove the top node from the stack and return it. If the list is **empty**, the method should return `None`.

### Requirements
- Handle the cases where the list is empty, has only one node, or has multiple nodes
- Update the `top` attribute
- Update the `length` attribute
- Return either the removed node or `None` if the list is **empty**.

### Code Implementation
```
def pop(self):
    if self.height == 0: # empty
        return None
    else:
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
```

### Explanation
- `if (self.height == 0):` → List is empty, return `None`.
- `temp = self.top` → Store a reference to the current top node in a temporary variable
- `self.top = self.top.next` → Update the top attribute of the Stack class to point to the next node in the stack.
- `temp.next = None` → Set the next attribute of the removed node (stored in the temporary variable) to None.
- `self.length -= 1`, `return node` → decrements the length and returns the node.

---
