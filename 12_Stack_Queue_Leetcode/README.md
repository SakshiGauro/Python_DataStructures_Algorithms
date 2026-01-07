# Stack and Queue: Interview/LeetCode Exercise

## Implement Stack Using a List

The objective is to create a constructor for Class Stack that implements a new stack with an empty list called stack_list

### Code Implementation

```
class Stack:
    def __init__(self):
        self.stack_list = []
```

---

## Push

The objective is to push a value onto the Stack implementation. 

### Requirements
- This Stack implementation uses a list instead of a linked list.

### Code Implementation

```
def push(self, value):
    self.stack_list.append(value)
```

---

## Pop

The objective is to pop a value onto the Stack implementation.

### Requirements
- This Stack implementation uses a list instead of a linked list.

### Code Implementation

```
def pop(self):
    if self.size() == 0: # empty 
        return None
    return self.stack_list.pop()
```

---

## Reverse String

The objective is to reverse a single parameter string, and return that string.

> **An example:**
>
> String: `apple` -> 'elppa'

### Requirements/Tips
- Create a new stack object
- Iterate over the characters in the string parameter and push each character onto the stack.
- Pop each character off the stack and append it to a new string

### Code Implementation

```
def reverse_string(my_string):
    if len(my_string) > 1:
        my_stack = Stack()
        for char in my_string: 
            my_stack.push(char)
            
        new_word = ""
        while (not my_stack.is_empty()):
            new_word += my_stack.pop()
        
        return new_word
    return my_string
```

### Explanation

- Initialize a new stack, `my_stack` to store the characters.
- `for char in my_string:`: This loop iterates through each character (stores in `char`) of `my_string`. 
    - `my_stack.push(char)`: Push that character in the stack.
- Initialize a new string, `new_word` to store the reversed string.
- `while (not my_stack.is_empty()):`: This loop iterates until the stack is empty.
    - `new_word += my_stack.pop()`: Appends each character to the string.
- Returns `new_word` if the given string has more than one character, if not it returns the given string(my_string).

---

## Parentheses Balanced

The objective is to check to see if a string of parentheses is balanced or not. By "balanced," we mean that for every open parenthesis, there is a matching closing parenthesis in the correct order.

> **An example:**
>
> String: `((()))` -> Balanced
> String: `(()))` -> Not Balanced
> String: `)(` -> Not Balanced

### Requirements
- In order to solve this problem, use a Stack data structure.

### Code Implementation

```
def is_balanced_parentheses(my_string):
    my_stack = Stack()
    
    for char in my_string:
        if char == '(':
            my_stack.push(char)
        else:
            if my_stack.is_empty(): 
                return False
            my_stack.pop()
    
    if my_stack.is_empty():
        return True
    return False
```

### Explanation

- Initialize a stack, `my_stack`.
- `for char in my_string:`: Start a `for loop` to iterate through each character of the string. 
  - `if char == '(':`: If we have an open parenthesis 
    - `my_stack.push(char)`: Add it to the stack
  - If not
    - `if my_stack.is_empty():`: Check if the stack is empty. 
      - If it is, string is not balanced, return `False`. 
    - `my_stack.pop()`: Pop one `'('` out of the stack. 
- `if my_stack.is_empty():` Check if the stack is empty after going through the strings.
  - If it is, string is balanced, return `True`.
- Otherwise, return `False`.

---

## Sort Stack

The objective is to sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack.

> **An example:**
>
> List: `[5, 1, 3, 7]` -> `[7, 5, 3, 1]`
> List: `[5, 4, 3, 2, 9]` -> `[9, 5, 4, 3, 2, 1]`

### Requirements
- In order to solve this problem, use a Stack data structure.

### Code Implementation

```
def sort_stack (my_stack):
    storted_stack = Stack()
    
    while(not my_stack.is_empty()):
        temp = my_stack.pop()
        while (not storted_stack.is_empty() and storted_stack.peek() > temp):
            my_stack.push(storted_stack.pop())
        
        storted_stack.push(temp)
    
    while(not storted_stack.is_empty()):
        my_stack.push(storted_stack.pop())
```

### Explanation

- Initialize a stack, `storted_stack`.
- `while(not my_stack.is_empty()):`: Loop until the stack is not empty.
    - `temp = my_stack.pop()`: Store the popped item in a variable
    - `while (not storted_stack.is_empty() and storted_stack.peek() > temp):`: Run the loop until the `storted_stack` is empty or the top element of storted_stack is less than or equal to temp.
        - `my_stack.push(storted_stack.pop())`: Add that top item of the `storted_stack` back to the original stack.
    - `storted_stack.push(temp)`: Store that item to the `storted_stack`
- `while(not storted_stack.is_empty()):`: Loop until the `storted_stack` is not empty.
    - `my_stack.push(storted_stack.pop())`: Remove the top element from the storted_stack using the `pop` method and adds it back to the original stack using the `push`

---

## Queue Using Stacks: Enqueue

The objective is to add an element to the back of the queue using two stacks.

### Requirements
- The method signature should be def enqueue(self, value).
- The method should add the element value to the back of the queue.

### Code Implementation

```
def enqueue(self, value):
    # make sure stack1 is empty
    while len(self.stack1) > 0:
        self.stack2.append(self.stack1.pop())
        
    self.stack1.append(value)
    
    while len(self.stack2) > 0:
        self.stack1.append(self.stack2.pop())
```

### Explanation

- `while len(self.stack1) > 0:`: Run this loop until stack1 is empty.
  - `self.stack2.append(self.stack1.pop())`: Pop the elements out of stack1 and push it to stack2.
- `self.stack1.append(value)`: Add the new value to stack1. 
- `while len(self.stack2) > 0:`: Run this until stack2 is empty.
    - `self.stack1.append(self.stack2.pop())`: Pop the elements out of stack2 and push it to stack1.

---

## Queue Using Stacks: Dequeue

The objective is to remove an element from the front of the queue using two stacks.

### Requirements
- The method signature should be def dequeue(self, value).
- The method should remove the element value from the front of the queue.

### Code Implementation

```
def dequeue(self):
    if self.is_empty():
        return None
    return self.stack1.pop()
```

### Explanation

- ` if self.is_empty():`: Check if the stack is empty, return None if it is.
- `return self.stack1.pop()`: Return the top item from the queue.

---
