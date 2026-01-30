# Recursive BST

## rBST: Contains

Implement the `r_contains` method of the BinarySearchTree class that recursively searches the binary search tree for a given value, starting from the root node, and return `True` if the value is found, and `False` otherwise.

You should use a private helper method `__r_contains` to perform the recursive search. This method should take two arguments: a `current` node in the tree, and the `value` to search for.

The `__r_contains` method checks whether the current node is `None`. If it is, the method should return `False`. If the value to search for is **equal** to the value of the current node, the method should return `True`. If the value is less than the value of the current node, the method should call itself recursively with the left child node and the value. If the value is greater than the value of the current node, the method should call itself recursively with the right child node and the value.

### Code Implementation
```
def __r_contains(self, current_node, value):
    if current_node == None: # doesn't exist
        return False
    
    if current_node.value == value: # exists!
        return True
        
    if value > current_node.value: # look right
        return self.__r_contains(current_node.right, value)
        
    if value < current_node.value: # look left
        return self.__r_contains(current_node.left, value)
        
    
def r_contains(self, value):
    return self.__r_contains(self.root, value)
```

### Explanation

**`r_contains` Function:** 
- Call the recursive function by passing in the root and passing the value. 

**`__r_contains` Function:**
- If the value is not found, return False. 
- If the value is found, return True.
- If the value is larger than the current_node value, look right!
  - Start a recursive call to the function by passing the right child as the node. 
- If the value is smaller than the current_node value, look left!
  - Start a recursive call to the function by passing the left child as the node.

---

## rBST: Insert

Implement a recursive method called `r_insert` to insert a value into a binary search tree (BST). The method should maintain the BST property, where the left subtree contains only nodes with values less than the parent node's value, and the right subtree contains only nodes with values greater than the parent node's value. **No duplicate values are allowed in the BST.**

The `__r_insert` method should take the current node and the value to be inserted as arguments. The method should perform the following tasks:
- If the current node is `None`, create a new node with the given value and return it.
- If the value is less than the current node's value, call the `__r_insert` method recursively on the left child of the current node.
- If the value is greater than the current node's value, call the `__r_insert` method recursively on the right child of the current node.
- Return the current node.

The `r_insert` method should perform the following tasks:
- If the root of the BST is `None`, create a new node with the given value and set it as the root.
- Call the `__r_insert` helper method with the root and the value as arguments.

### Code Implementation
```
def __r_insert(self, current_node, value):
    if current_node == None:
        return Node(value)
    
    if value > current_node.value: # go right
        current_node.right = self.__r_insert(current_node.right, value)
    
    if value < current_node.value: # go left
        current_node.left = self.__r_insert(current_node.left, value)
        
    return current_node
    
def r_insert(self, value): 
    if self.root == None: # BST is empty
        self.root = Node(value)
    return self.__r_insert(self.root, value)
```

---

## BST: Minimum Value

Implement a method called `min_value` that finds and returns the minimum value in a binary search tree (BST) starting from a given node.

The method should take one argument, `current_node`, which is the node from where the search for the minimum value begins. The method should follow these steps:
- Traverse the left subtree of the BST from the `current_node`, moving to the left child of each node until there is no left child available.
- Once the leftmost node is found, return its value as the minimum value in the BST starting from the given node.

### Code Implementation
```
def min_value (self, current_node): 
    while (current_node.left is not None):
        current_node = current_node.left
    
    return current_node.value
```

---

## rBST: Delete

Write two Python functions for the BinarySearchTree class: `delete_node` and `__delete_node`.

These functions should work together to delete a node with a given integer value from the binary search tree while maintaining its structure and ordering after deletion.

- `delete_node(value)`: This function should take an integer value as input and call the `__delete_node` function with the root node of the binary search tree and the input value. It should then update the root of the binary search tree with the returned value from the `__delete_node` function.
- `__delete_node(current_node, value)`: This function should take a Node object (`current_node`) and an integer value as input. It should be a recursive helper function that facilitates the node deletion process for the delete_node function.

### Code Implementation
```
def __delete_node(self, current_node, value): 
    if current_node == None:
        return None
    
    if value > current_node.value: # go right
        current_node.right = self.__delete_node(current_node.right, value)
    elif value < current_node.value: # go left
        current_node.left = self.__delete_node(current_node.left, value)
    else: 
        if current_node.left == None and current_node.right == None: # no children 
            return None
        elif current_node.right == None: # only left child exists
            return current_node.left
        elif current_node.left == None: # only right child exists
            return current_node.right
        else: # both child exists
            sub_tree_min = self.min_value(current_node.right)
            current_node.value = sub_tree_min
            current_node.right = self.__delete_node(current_node.right, sub_tree_min)
    return current_node
            
    
    
def delete_node(self, value): 
    self.root = self.__delete_node(self.root, value)
```

### Explanation

**`delete_node` Function:**
- Sets the root of the BST to the value returned from the recursive function.

**`__delete_node` Function:**
- If the current_node is None, return None.
- If the input value is **larger** than the value of the current_node.
  - Set the right child of the current_node to the result of recursive function with the right child.
- If the input value is **smaller** than the value of the current_node. 
  - Set the left child to the result of recursive function with the left child.
- Otherwise, (value is equal to the current node! Delete this node)
  - If the current_node has no children, return None.
  - If the current_node has only a left child, return the left child.
  - If the current_node has only a right child, return the right child.
  - Otherwise, (it has both of the children)
    - Find the minimum value in the right subtree of the current_node.
    - Delete the node with the minimum value in the right subtree using a recursive call. 
- Return the current_node after making the necessary updates.

---
