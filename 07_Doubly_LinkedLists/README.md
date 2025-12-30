# Double Linked Lists

A **Double Linked List (DLL)** is a linear data structure where elements are stored in **nodes**, and each node points to the previous and next one in the sequence.

Unlike Python lists (arrays), linked lists **do not use indexes** and **do not store elements contiguously in memory.**

**Node Components**
- **Value** → value of the node
- **Next** → points to the next node
- **Prev** → points to the previous node

**DLL Components**
- **Head** → points to the first node
- **Tail** → points to the last node
- **Node** → stores a value and a reference to the next node

---

## Constructor
This section introduces the **constructor** for a doubly linked list. The goal is to initialize a linked list with a single node while properly setting up internal pointers.

### Requirements

**Node Class**
- A constructor that accepts a `value`
- A `value` attribute to store data
- A `next` attribute initialized to `None` (pointer to the next node)
- A `prev` attribute initialized to `None` (pointer to the previous node)

**Doubly LinkedList Class**
- A constructor that accepts a `value`
- Creates a new `Node` using that value
- Initializes:
    - `head` → first node
    - `tail` → last node
- Initializes `length` to `1`

### Code Implementation
```
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
```

### Explanation

**Node Class**
- `class Node:`: Defines the `Node` class, which represents a single element in the linked list.
- `def __init__(self, value):`: Constructor for the `Node` class called when you create a new instance.
- `self.value = value`: Stores the data passed into the node.
- `self.next = None`: Initializes the pointer to the next node as `None`. A new node does not point to anything yet.
- `self.prev = None`: Initializes the pointer to the previous node as `None`. A new node does not point to anything yet.

**LinkedList Class**
- `class LinkedList:`: Defines the **LinkedList** class, which manages nodes and pointers.
- `def __init__(self, value):`: Constructor for the LinkedList class called when you create a new instance of the LinkedList class.
- `new_node = Node(value)`: Creates the first node in the linked list.
- `self.head = new_node`: Sets the head of the list to the new node.
- `self.tail = new_node`: Sets the tail of the list to the same node. Since the list has only one node, head and tail point to the same location in memory.
- `self.length = 1`: Tracks the number of nodes in the list. Starts at 1 because one node exists.

---

## Append
The `append` method adds a **new node to the end** of the linked list. This is an efficient operation because we maintain a `tail` pointer.

### Requirements
- Handle the cases where the list is empty
- Create a new `node`
- Update the current tail's `next` pointer
- Update the current tail's `prev` pointer
- Move the `tail` reference to the new node
- Increment `length`
- Return True if successful

### Code Implementation
```
def append(self, value):
      new_node = Node(value)
      
      if self.head is None: # Empty List
          self.head = new_node
          self.tail = new_node
      else:
          self.tail.next = new_node
          new_node.prev = self.tail
          self.tail = new_node

      self.length += 1
      return True
```

### Explanation
- `new_node = Node(value)` → Create a new node.
- `self.head is None:` → Check if the linked list is empty.
    - If the LL is empty, set the `head` and `tail` to point at `new_node`.
- `self.tail.next = new_node` → Update the next attribute.
- `new_node.prev = self.tail` → Update the prev attribute.
- `self.tail = new_node` → set tail to point to new_node.
- `self.length += 1` → Increment the length of the linked list by 1.

---

## Pop
The `pop` method should remove the last node (`tail`) from the linked list and return the removed node. If the list is **empty**, the method should return `None`.

### Requirements
- Handle the cases where the list is empty, has only one node, or has multiple nodes
- Update the `tail` attribute
- Update the `length` attribute
- Return either the removed node or `None` if the list is **empty**.

### Code Implementation
```
def pop(self):
    if (self.length == 0): 
        return None
    elif (self.length == 1): 
        node = self.head
        self.head = None
        self.tail = None
        self.length = 0
        return node
        
    temp = self.tail
    self.tail = self.tail.prev
    self.tail.next = None
    temp.prev = None
    self.length -= 1
    return temp
```

### Explanation
- `if (self.length == 0):` → List is empty, return `None`.
- `elif (self.length == 1):` → Only one item in the list, set head and tail to `None`, length to `0` and return the `node`.
- `temp = self.head` → Points to tail.
- `self.tail = self.tail.prev` → Set the tail to the previous node.
- `self.tail.next = None`, `temp.prev = None` → Set the `next` and `prev` of the detached node to `None`.
- `self.length -= 1`, `return node` → decrements the length and returns the node.

---

## Prepend
The `prepend` method should add a new node with a given value to the **beginning** of the linked list, updating the head attribute and the length attribute accordingly.

### Requirements
- Handle the cases where the list is empty, has only one node, or has multiple nodes
- Create a new node with the given value and add it to the beginning of the list
- Update the `head` attribute
- Update the `length` attribute
- Return `True` if the operation is successful.

### Code Implementation
```
def prepend(self, value):
    new_node = Node(value)
    if (self.length == 0): # list is empty
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    self.length += 1
    return True
```

### Explanation
- `if self.length == 0:` → List is empty, set the head and tail to the new node
- `new_node.next = self.head`, `self.head.prev = new_node` → Runs when list is not empty. Connect the `new_node` to the head by adjusting the `next` and `prev` attribute.
- `self.head = new_node` → Reset the head.

---

## Pop First
The `pop_first` method removes the first node (the head) from the linked list, update the head attribute and the length attribute accordingly, and return the removed node.

### Requirements
- Handle the cases where the list is empty, has only one node, or has multiple nodes
- Save a reference to the current head node before updating the head attribute
- Update the `head` attribute
- Update the `length` attribute
- If the list becomes empty after removing the node, set the `tail` attribute to `None`
- Return either the removed node or `None` if the list is **empty**.

### Code Implementation
```
def pop_first(self):
    if (self.length == 0): # list is empty
        return None
    elif (self.length == 1): # only 1 Item
        node = self.head
        self.head = None
        self.tail = None
        self.length -= 1
        return node
    node = self.head
    self.head = self.head.next
    self.head.prev = None
    node.next = None
    self.length -= 1
    return node
```

### Explanation
- `if (self.length == 0):` → List is empty, return `None`
- `elif (self.length == 1): # only 1 Item` → Only one item 
  - `node = self.head` → Save the head reference
  - `self.head = None`, `self.tail = None` → Set the **head** and **tail** to `None`
  - `self.length -= 1`, `return node` → Reduce length and return the node
- `node = self.head` → Save the head reference
- `self.head = self.head.next` → Set the head to the next node
- `self.head.prev = None`, `node.next = None` → Cut off the node to be removed. 
- `self.length -= 1`, `return node` → Reduce length and return the node

---

## Get
The `get` method should take an integer index as a parameter and return a pointer to the node at the specified index in the linked list.

### Requirements
- Handle the cases where the index is **out of bounds**.
- Start at the `head` of the list
- If the `index` is **less than** half of the list length, iterate through the head.
- If the `index` is **greater than or equal** to half of the list length, start iterating from the tail.
- Stop traversing the list when it reaches the specified index and return the node at that position.
- If the index is out of bounds, the method should return `None`.

### Code Implementation
```
def get(self, index):
    if (index < 0 or index >= self.length): # Out of Bounds
        return None
        
    if index < (0.5 * self.length):
        temp = self.head
        for _ in range(index):
            temp = temp.next
    else:
        temp = self.tail
        for _ in range(self.length - 1, index, -1):
            temp = temp.prev
    return temp
```

### Explanation
- `if (index < 0 or index >= self.length): # Out of Bounds` → Index Out of Bounds, return `None`
- `if index < (0.5 * self.length):` → Start at the head
  - `for _ in range(index):` → Iterate until it reaches the index
  - `temp = temp.next` → Move to the next node
- `temp = self.tail` → Start at the tail
- `for _ in range(self.length - 1, index, -1):` → Loop from the tail until the index.
- `temp = temp.prev` → Move to the prev node. 
- `return temp` → Return `temp` as it stores the `node` at `index`.

---

## Set
The `set_value` method should take an integer index and a value as parameters and update the value of the node at the specified index in the linked list.

### Requirements
- Handle the cases where the index is **out of bounds**.
- Utilize the `get` method to find the node at the specified index.
- Update the value of the node if the node is found.
- If the index is out of bounds, the method should return `False`. Return `True` is successful.

### Code Implementation
```
def set_value (self, index, value):
    temp = self.get(index)
    if (temp is not None):
        temp.value = value
        return True
    return False   
```

### Explanation
- `temp = self.get(index)` → Get the `node` at that index.
- `if (temp is not None):` → Node Exists.
  - `temp.value = value` → Change the value and return `True`.
- `return False ` → Return `False`. 

---

## Insert
The insert method should take an integer index and a value as parameters and insert a new node with the given value at the specified index in the linked list.

### Requirements
- Handle the cases where the index is **out of bounds** and edge cases, such as inserting a new node at the beginning or end of the list
- Utilize the `prepend`, `append`, and `get` methods
- Create a new `node` with the given value and insert it at the specified index
- Update the `next` and `prev` attributes
- Increment the `length` attribute
- If the index is out of bounds, the method should return `False`. Return `True` is successful

### Code Implementation
```
def insert(self, index, value):
    if index == 0: # prepend
        return self.prepend(value)
    elif index == self.length: # append
        return self.append(value)
    
    if index >= 1 and index <= self.length:
        new_node = Node(value)
        node = self.get(index)
        
        before = node.prev
        node.prev = new_node
        before.next = new_node
        self.length += 1 
        return True
    return False
```

### Explanation
- `new_node = Node(value)` → Create a new Node.
- `node = self.get(index)`, `before = node.prev` → Store the pointers to the node at that index and the node before that.
- `node.prev = new_node`, `before.next = new_node` → Attach the new node.
- `self.length += 1` → Increase the length

---

## Remove
The remove method should take an integer index as a parameter and remove the node at the specified index in the linked list, returning the removed node.

### Requirements
- Handle the cases where the index is **out of bounds** and edge cases, such as removing a node at the beginning or end of the list
- Utilize the `pop_first`, `pop`, and `get` methods
- Update the `next` attribute
- Decrement the `length` attribute
- If the index is out of bounds, the method should return `None`. Return the removed node if successful

### Code Implementation
```
def remove(self, index):
    if index < 0 or index >= self.length: # OOB
        return None
    elif index == 0: # Remove from the head 
        return self.pop_first()
    elif index == self.length - 1: # Remove from the tail 
        return self.pop()
    else:
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev = temp.next
        
        temp.prev = None
        temp.next = None
        
        self.length -= 1
        return temp     
```

### Explanation
- `temp = self.get(index)` → Store the reference to the node to be removed.
- `temp.next.prev = temp.prev`, `temp.prev = temp.next` → Adjust the `prev` and `next` attributes by skipping the node.
- `temp.prev = None`, `temp.next = None` → Detach the node from the DLL. 
- `self.length -= 1`, `return temp ` → Adjust the length and return the removed node.

---