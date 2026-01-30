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
    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        
        if value > current_node.value: # go right
            current_node.right = self.__r_insert(current_node.right, value)
        
        if value < current_node.value: # go left
            current_node.left = self.__r_insert(current_node.left, value)

        if value == current_node.value: # duplicate
            pass  
        return current_node
        
    def r_insert(self, value): 
        if self.root == None:
            self.root = Node(value)
        return self.__r_insert(self.root, value)

    def min_value (self, current_node): 
        while (current_node.left is not None):
            current_node = current_node.left
        
        return current_node.value 
    
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
#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+


# rInsert
class Test_rInsert(unittest.TestCase): 
    def test_insert_empty_tree(self):    
        bst = BinarySearchTree()
        bst.r_insert(10)

        self.assertEqual(bst.root.value, 10)
    
    def test_check_root_value(self):    
        bst = BinarySearchTree()
        bst.r_insert(5)

        self.assertEqual(bst.root.value, 5)
    
    def test_r_insert_duplicate(self):
        bst = BinarySearchTree()
        bst.r_insert(5)
        bst.r_insert(5)

        self.assertEqual(bst.root.value, 5)
        self.assertIsNone(bst.root.left)
        self.assertIsNone(bst.root.right)

    def test_r_insert_greater_than_root(self):    
        bst = BinarySearchTree()
        bst.r_insert(5)
        bst.r_insert(10)

        self.assertEqual(bst.root.right.value, 10)
    
    def test_r_insert_less_than_root(self):    
        bst = BinarySearchTree()
        bst.r_insert(5)
        bst.r_insert(2)

        self.assertEqual(bst.root.left.value, 2)

    def test_r_insert_existing_tree(self):    
        bst = BinarySearchTree()
        bst.r_insert(5)
        bst.r_insert(6)
        bst.r_insert(2)
        bst.r_insert(3)
        bst.r_insert(10)

        self.assertEqual(bst.root.value, 5)

# rContains
class Test_rContains(unittest.TestCase): 
    def test_empty_tree(self):    
        bst = BinarySearchTree()

        self.assertFalse(bst.r_contains(10))
    
    def test_value_exists(self):    
        bst = BinarySearchTree()
        bst.insert(5)

        self.assertTrue(bst.r_contains(5))
    
    def test_value_doesnt_exist(self):    
        bst = BinarySearchTree()
        bst.insert(5)

        self.assertFalse(bst.r_contains(10))

    def test_contains_leaf_node(self):    
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(10)
        bst.insert(2)
        bst.insert(1)

        self.assertTrue(bst.r_contains(1))

# min value
class Test_MinVal(unittest.TestCase): 
    def test_one_item(self):    
        bst = BinarySearchTree()
        bst.r_insert(5)

        self.assertEqual(bst.min_value(bst.root), 5)

    def test_existing_tree(self):    
        bst = BinarySearchTree()
        bst.r_insert(5)
        bst.r_insert(6)
        bst.r_insert(2)
        bst.r_insert(3)
        bst.r_insert(10)

        self.assertEqual(bst.min_value(bst.root), 2)
    
    def test_sub_tree(self):    
        bst = BinarySearchTree()
        bst.r_insert(5)
        bst.r_insert(6)
        bst.r_insert(2)
        bst.r_insert(1)
        bst.r_insert(10)

        self.assertEqual(bst.min_value(bst.root.left), 1)

# rDelete
class Test_rDelete(unittest.TestCase): 
    def test_empty_tree(self):    
        bst = BinarySearchTree()
        bst.delete_node(10)

        self.assertFalse(bst.r_contains(10))
    
    def test_no_children(self):    
        bst = BinarySearchTree()
        bst.r_insert(5)
        bst.r_insert(6)
        bst.r_insert(2)
        bst.r_insert(1)
        bst.r_insert(10)

        bst.delete_node(1)

        self.assertFalse(bst.r_contains(1))
    
    def test_only_left_child(self):    
        bst = BinarySearchTree()
        bst.r_insert(5)
        bst.r_insert(6)
        bst.r_insert(2)
        bst.r_insert(1)
        bst.r_insert(10)

        bst.delete_node(2)

        self.assertFalse(bst.r_contains(2))

    def test_only_right_child(self):    
        bst = BinarySearchTree()
        bst.r_insert(5)
        bst.r_insert(6)
        bst.r_insert(2)
        bst.r_insert(1)
        bst.r_insert(10)

        bst.delete_node(6)

        self.assertFalse(bst.r_contains(6))

    def test_two_children(self):    
        bst = BinarySearchTree()
        bst.r_insert(5)
        bst.r_insert(6)
        bst.r_insert(2)
        bst.r_insert(1)
        bst.r_insert(3)
        bst.r_insert(10)

        bst.delete_node(2)

        self.assertFalse(bst.r_contains(2))
    
    def test_non_existent_node(self):    
        bst = BinarySearchTree()
        bst.r_insert(5)
        bst.r_insert(6)
        bst.r_insert(2)
        bst.r_insert(1)
        bst.r_insert(3)
        bst.r_insert(10)

        bst.delete_node(20)

        self.assertFalse(bst.r_contains(20))

    def test_delete_root(self):    
        bst = BinarySearchTree()
        bst.r_insert(5)
        bst.r_insert(6)
        bst.r_insert(2)
        bst.r_insert(1)
        bst.r_insert(3)
        bst.r_insert(10)

        bst.delete_node(5)

        self.assertFalse(bst.r_contains(5))
        
if __name__ == '__main__':
    unittest.main()     
        
