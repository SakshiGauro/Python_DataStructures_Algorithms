import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
  
    def BFS(self): 
        if self.root is None: 
            return[]
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
    
    def dfs_pre_order(self): 
        results = []
        
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None: 
                traverse(current_node.right)
        
        if self.root is not None: 
            traverse(self.root)

        return results

    def dfs_post_order(self): 
        results = []
        
        def traverse(current_node):
            if current_node.left is not None: 
                traverse(current_node.left)
                
            if current_node.right is not None:
                traverse(current_node.right)
            
            results.append(current_node.value)
            
        if self.root is not None: 
            traverse(self.root)
        return results

    def dfs_in_order(self):
        results = []
        
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            
            results.append(current_node.value)
            
            if current_node.right is not None: 
                traverse(current_node.right)
            
        if self.root is not None: 
            traverse(self.root)
        return results

#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+


# BFS
class Test_BFSt(unittest.TestCase): 
    def test_insert_empty_tree(self):    
        bst = BinarySearchTree()

        self.assertEqual(bst.BFS(), [])
    
    def test_one_item(self):    
        bst = BinarySearchTree()
        bst.insert(1)

        self.assertEqual(bst.BFS(), [1])
    
    def test_two_items(self):    
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)

        self.assertEqual(bst.BFS(), [1, 2])

    def test_three_items(self):    
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)

        self.assertEqual(bst.BFS(), [2, 1, 3])
    
    def test_multi_items(self):    
        bst = BinarySearchTree()
        bst.insert(47)
        bst.insert(21)
        bst.insert(76)
        bst.insert(18)
        bst.insert(27)
        bst.insert(52)
        bst.insert(82)

        self.assertEqual(bst.BFS(), [47, 21, 76, 18, 27, 52, 82])

# DFS PreOrder
class Test_DFS_PreOrder(unittest.TestCase): 
    def test_insert_empty_tree(self):    
        bst = BinarySearchTree()

        self.assertEqual(bst.dfs_pre_order(), [])
    
    def test_one_item(self):    
        bst = BinarySearchTree()
        bst.insert(1)

        self.assertEqual(bst.dfs_pre_order(), [1])
    
    def test_two_items(self):    
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)

        self.assertEqual(bst.dfs_pre_order(), [1, 2])

    def test_three_items(self):    
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)

        self.assertEqual(bst.dfs_pre_order(), [2, 1, 3])
    
    def test_multi_items(self):    
        bst = BinarySearchTree()
        bst.insert(47)
        bst.insert(21)
        bst.insert(76)
        bst.insert(18)
        bst.insert(27)
        bst.insert(52)
        bst.insert(82)

        self.assertEqual(bst.dfs_pre_order(), [47, 21, 18, 27, 76, 52, 82])

# DFS PostOrder
class Test_DFS_PostOrder(unittest.TestCase): 
    def test_insert_empty_tree(self):    
        bst = BinarySearchTree()

        self.assertEqual(bst.dfs_post_order(), [])
    
    def test_one_item(self):    
        bst = BinarySearchTree()
        bst.insert(1)

        self.assertEqual(bst.dfs_post_order(), [1])
    
    def test_two_items(self):    
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)

        self.assertEqual(bst.dfs_post_order(), [2, 1])

    def test_three_items(self):    
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)

        self.assertEqual(bst.dfs_post_order(), [1, 3, 2])
    
    def test_multi_items(self):    
        bst = BinarySearchTree()
        bst.insert(47)
        bst.insert(21)
        bst.insert(76)
        bst.insert(18)
        bst.insert(27)
        bst.insert(52)
        bst.insert(82)

        self.assertEqual(bst.dfs_post_order(), [18, 27, 21, 52, 82, 76, 47])

# DFS InOrder
class Test_DFS_InOrder(unittest.TestCase): 
    def test_insert_empty_tree(self):    
        bst = BinarySearchTree()

        self.assertEqual(bst.dfs_in_order(), [])
    
    def test_one_item(self):    
        bst = BinarySearchTree()
        bst.insert(1)

        self.assertEqual(bst.dfs_in_order(), [1])
    
    def test_two_items(self):    
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)

        self.assertEqual(bst.dfs_in_order(), [1, 2])

    def test_three_items(self):    
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)

        self.assertEqual(bst.dfs_in_order(), [1, 2, 3])
    
    def test_multi_items(self):    
        bst = BinarySearchTree()
        bst.insert(47)
        bst.insert(21)
        bst.insert(76)
        bst.insert(18)
        bst.insert(27)
        bst.insert(52)
        bst.insert(82)

        self.assertEqual(bst.dfs_in_order(), [18, 21, 27, 47, 52, 76, 82])

if __name__ == '__main__':
    unittest.main()     
        