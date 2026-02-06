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

    def is_valid_bst(self):
        if self.root is None: 
            return True
        in_order_list = self.dfs_in_order()

        for i in range(1, len(in_order_list)):
            if in_order_list[i] <= in_order_list[i-1]:
                return False

        return True


#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+


# Validate BST
class Test_Validate_BFS(unittest.TestCase): 
    def test_insert_empty_tree(self):    
        bst = BinarySearchTree()

        self.assertTrue(bst.is_valid_bst())
    
    def test_one_item(self):    
        bst = BinarySearchTree()
        bst.insert(1)

        self.assertTrue(bst.is_valid_bst())
    
    def test_two_items(self):    
        bst = BinarySearchTree()
        bst.insert(1)
        bst.insert(2)

        self.assertTrue(bst.is_valid_bst())

    def test_three_items(self):    
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)

        self.assertTrue(bst.is_valid_bst())

    def test_two_items_invalid(self):    
        bst = BinarySearchTree()
        bst.insert(5)
        invalid_node = Node(3)
        bst.root.right = invalid_node # manually changing the value

        self.assertFalse(bst.is_valid_bst())

    def test_three_items_invalid(self):    
        bst = BinarySearchTree()
        bst.insert(5)
        invalid_node = Node(3)
        invalid_node2 = Node(10)
        bst.root.right = invalid_node # manually changing the value
        bst.root.left = invalid_node2 # manually changing the value

        self.assertFalse(bst.is_valid_bst())
    
    def test_multi_items(self):    
        bst = BinarySearchTree()
        bst.insert(47)
        bst.insert(21)
        bst.insert(76)
        bst.insert(18)
        bst.insert(27)
        bst.insert(52)
        bst.insert(82)

        self.assertTrue(bst.is_valid_bst())

if __name__ == '__main__':
    unittest.main()     
        