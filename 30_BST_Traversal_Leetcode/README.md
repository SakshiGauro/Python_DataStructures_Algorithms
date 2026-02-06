# BST: Interview/LeetCode Exercise

## Validate BST

You are tasked with writing a method called `is_valid_bst` in the `BinarySearchTree` class that checks whether a binary search tree is a valid binary search tree.

Your method should use the `dfs_in_order` method to get the node values of the binary search tree in ascending order, and then check whether each node value is greater than the previous node value.

If the node values are not sorted in ascending order, the method should return `False`, indicating that the binary search tree is not valid.

If all node values are sorted in ascending order, the method should return `True`, indicating that the binary search tree is a valid binary search tree.

### Code Implementation

```
def is_valid_bst(self): 
    in_order_list = self.dfs_in_order()
    
    for i in range(1, len(in_order_list)):
        if in_order_list[i] <= in_order_list[i-1]: 
            return False
    
    return True
```

---

## Kth Smallest Node

Given a binary search tree, find the kth smallest element in the tree. For example, if the tree contains the elements `[1, 2, 3, 4, 5]`, the 3rd smallest element would be `3`.

### Code Implementation

```
def kth_smallest(self, k):
    stack = []
    node = self.root
    
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.value
        
        node = node.right
        
    return None
```

### Explanation

- Initialize a stack to hold nodes and sets a temporary node to the root of the tree.
- Use a while loop to traverse the tree in-order (left, root, right) and add each node to the stack.
- Pop a node from the stack and decrements the `k` counter.
- If k is equal to 0, it returns the value of the node, which is the kth smallest element.
  - If k is not equal to 0, it moves to the right child of the node and continues traversing the tree.
- If it reaches the end of the tree without finding the kth smallest element, it returns None.

---
