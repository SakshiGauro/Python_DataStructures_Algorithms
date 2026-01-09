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
        if (self.root is None):
            self.root = new_node
            return True
            
        temp = self.root
        while(temp):
            if (temp.value == value): # Duplicate
                return False
            elif (new_node.value < temp.value): # Less than (left)
                if(temp.left is None): 
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else: # Greater than (right)
                if(temp.right is None): 
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right

    def contains(self, value):
        temp = self.root
        while(temp):
            if (temp.value == value): # Value exists
                return True
            elif (value < temp.value): # go left
                temp = temp.left
            else: # go right
                temp = temp.right
        
        return False
#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+


# Constructor
class Test_Constructor(unittest.TestCase):    
    def test_BST_init(self):    
        BST = BinarySearchTree()

        self.assertIsNotNone(BST)

    def test_root(self):    
        BST = BinarySearchTree()

        self.assertIsNone(BST.root)

    def test_node_left(self):    
        node = Node(5)

        self.assertIsNone(node.left)

    def test_node_right(self):    
        node = Node(3)

        self.assertIsNone(node.right)

    def test_node_value(self):    
        node = Node(1)

        self.assertEqual(node.value, 1)

# Insert
class Test_Insert(unittest.TestCase): 
    def test_insert_empty_tree(self):    
        bst = BinarySearchTree()
        bst.insert(10)

        self.assertEqual(bst.root.value, 10)
    
    def test_check_root_value(self):    
        bst = BinarySearchTree()

        self.assertTrue(bst.insert(5))
    
    def test_insert_duplicate(self):    
        bst = BinarySearchTree()
        bst.insert(5)

        self.assertFalse(bst.insert(5))

    def test_insert_greater_than_root(self):    
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(10)

        self.assertEqual(bst.root.right.value, 10)
    
    def test_insert_less_than_root(self):    
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(2)

        self.assertEqual(bst.root.left.value, 2)
    
    def test_insert_duplicate(self):    
        bst = BinarySearchTree()
        bst.insert(5)

        self.assertFalse(bst.insert(5))

    def test_insert_existing_tree(self):    
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(6)
        bst.insert(2)
        bst.insert(3)

        self.assertTrue(bst.insert(10))

# Contains
class Test_Contains(unittest.TestCase): 
    def test_empty_tree(self):    
        bst = BinarySearchTree()

        self.assertFalse(bst.contains(10))
    
    def test_value_exists(self):    
        bst = BinarySearchTree()
        bst.insert(5)

        self.assertTrue(bst.contains(5))
    
    def test_value_doesnt_exist(self):    
        bst = BinarySearchTree()
        bst.insert(5)

        self.assertFalse(bst.contains(10))

    def test_contains_leaf_node(self):    
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(10)
        bst.insert(2)
        bst.insert(1)

        self.assertTrue(bst.contains(1))


if __name__ == '__main__':
    unittest.main()     
        
