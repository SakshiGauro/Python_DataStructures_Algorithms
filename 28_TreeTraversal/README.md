# Tree Traversal 

## BFS (Breadth First Search)

Breadth First Search (BFS) is a fundamental graph traversal algorithm. It begins with a node, then first traverses all its adjacent nodes. Once all adjacent are visited, then their adjacent are traversed.

### Code Implementation
```
def BFS(self): 
    current_node = self.root
    queue = []
    result = []
    
    queue.append(current_node)
    
    while len(queue) > 0: 
        current_node = queue.pop(0)
        result.append(current_node.value)
        if (current_node.left is not None): 
            queue.append(current_node.left)
        if (current_node.right is not None):
            queue.append(current_node.right)
            
    return result
```

### Explanation

- Initialize the `current_node` variable with the root of the binary tree.
- Create an empty list called `queue` to store nodes for processing, and another empty list called `results` to store the visited nodes in order.
- Append the `current_node` to the queue.
- Implement a loop that continues until the queue is empty:
  - Set `current_node` to the first element in the queue, and remove this element from the queue.
  - Append the value of `current_node` to the results list.
  - If the current_node has a left child, append it to the queue.
  - If the current_node has a right child, append it to the queue.
- Return the results list, containing the values of the nodes in the order they were visited during the Breadth-First Search traversal.

---

## DFS PreOrder

### Code Implementation
```
def dfs_pre_order(self): 
    results = []
    
    def traverse(current_node):
        results.append(current_node.value)
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None: 
            traverse(current_node.right)
    
    traverse(self.root)
    return results
```

### Explanation

- Create an empty list called `results` to store the visited nodes in order.
- Define a nested function called `traverse` that takes a current_node as an argument.
- In the `traverse` function, perform the following tasks:
  - Append the value of the `current_node` to the `results` list.
  - If the `current_node` has a left child, recursively call the `traverse` function with the left child as an argument.
  - If the `current_node` has a right child, recursively call the `traverse` function with the right child as an argument.
- Call the `traverse` function with the root of the binary tree as the initial argument.
- Return the `results` list, containing the values of the nodes in the order they were visited during the Pre-Order Depth-First Search traversal.

---

## DFS PostOrder

### Code Implementation
```
def min_value (self, current_node): 
    while (current_node.left is not None):
        current_node = current_node.left
    
    return current_node.value
```

### Explanation
- Create an empty list called `results` to store the visited nodes in order.
- Define a nested function called `traverse` that takes a current_node as an argument.
- In the `traverse` function, perform the following tasks:
  - If the `current_node` has a left child, recursively call the `traverse` function with the left child as an argument.
  - If the `current_node` has a right child, recursively call the `traverse` function with the right child as an argument.
  - Append the value of the `current_node` to the `results` list.
- Call the `traverse` function with the root of the binary tree as the initial argument.
- Return the `results` list, containing the values of the nodes in the order they were visited during the Post-Order Depth-First Search traversal.

---

## DFS InOrder

### Code Implementation
```
def dfs_in_order(self):
    results = []
    
    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        
        results.append(current_node.value)
        
        if current_node.right is not None: 
            traverse(current_node.right)
        
    traverse(self.root)
    return results
```

### Explanation

- Create an empty list called `results` to store the visited nodes in order.
- Define a nested function called `traverse` that takes a `current_node` as an argument.
- In the `traverse` function, perform the following tasks:
  - If the `current_node` has a left child, recursively call the `traverse` function with the left child as an argument.
  - Append the value of the `current_node` to the results list.
  - If the `current_node` has a right child, recursively call the traverse function with the right child as an argument.
- Call the `traverse` function with the root of the binary tree as the initial argument.
- Return the `results` list, containing the values of the nodes in the order they were visited during the In-Order Depth-First Search traversal.

---

_source: https://www.geeksforgeeks.org/python/python-program-for-breadth-first-search-or-bfs-for-a-graph/_

---