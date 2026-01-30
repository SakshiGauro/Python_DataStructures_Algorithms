# Recursive BST: Interview/LeetCode Exercise

## Convert Sorted List to Balanced BST

The task is to develop a method that takes a sorted list of integers as input and constructs a height-balanced BST.

This involves creating a BST where the depth of the two subtrees of any node does not differ by more than one.

Achieving a height-balanced tree is crucial for optimizing the efficiency of tree operations, ensuring that the BST remains efficient for search, insertion, and deletion across all levels of the tree.

### Code Implementation

```
def __sorted_list_to_bst(self, nums, left, right):
    if left > right:
        return None
    
    mid = (left + right) // 2
    current = Node(nums[mid])
    
    # left side
    current.left = self.__sorted_list_to_bst(nums, left, mid-1)
    
    # right side
    current.right = self.__sorted_list_to_bst(nums, mid+1, right)
    
    return current
```

### Explanation

- Check if sub-list is empty, i.e. `left > right`, return None.
- Find middle element index `(left + right) // 2`.
- Create node with middle element. 
- Construct left subtree by recursively calling the function for left part of list `(left, mid - 1)` and assign to `current.left`.
- Construct right subtree by recursively calling the function for right part of list `(mid + 1, right)` and assign to `current.right`.
- Return current node

The current node becomes root of BST subtree for given sub-list.

---

## Invert Binary Tree

Write a method to invert (or mirror) a binary tree. This means that for every node in the binary tree, you will swap its left and right children.

![img.png](img.png)

### Code Implementation

```
def __invert_tree(self, node):
    if node == None:
        return None
    
    temp = node.left
    node.left = self.__invert_tree(node.right)
    node.right = self.__invert_tree(temp)
    
    return node
```

### Explanation

- Check for Base Case. If node is None (indicating an empty tree or the end of a branch), Return None. 
- Swap Left and Right Children. 
  - Save the current node's left child in a temporary variable (temp). 
  - Assign the result of recursively inverting the right child to the current node's left child.
  - Assign the result of recursively inverting the saved left child (now in temp) to the current node's right child. 
- Return the Current Node

After the left and right children have been swapped, return the current node to ensure the inverted structure is maintained up the tree.

---
