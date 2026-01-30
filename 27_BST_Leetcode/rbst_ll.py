import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:  # Changed to elif to avoid comparing twice if equal
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node  
    
    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)

    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

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
    

    def invert(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self, node):
        if node == None:
            return None
        
        temp = node.left
        node.left = self.__invert_tree(node.right)
        node.right = self.__invert_tree(temp)
        
        return node
    
    # The 'is_balanced' and 'inorder_traversal' methods will 
    # be used to test your code
    def is_balanced(self, node=None):
        def check_balance(node):
            if node is None:
                return True, -1
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0
            balanced = abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return balanced, height

        balanced, _ = check_balance(self.root if node is None else node)
        return balanced
        
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        result = []
        self._inorder_helper(node, result)
        return result

    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)
                

def check_balanced_and_correct_traversal(bst, expected_traversal):
    is_balanced = bst.is_balanced()
    inorder = bst.inorder_traversal()
    # print("Is balanced:", is_balanced)
    # print("Inorder traversal:", inorder)
    # print("Expected traversal:", expected_traversal)
    if is_balanced and inorder == expected_traversal:
        # print("PASS: Tree is balanced and inorder traversal is correct.\n")
        return True
    else:
        # print("FAIL: Tree is either not balanced or inorder traversal is incorrect.\n")
        return False


#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+



def tree_to_list(node):
    """Helper function to convert tree to list level-wise for easy comparison"""
    if not node:
        return []
    queue = [node]
    result = []
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.value)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    while result and result[-1] is None:  # Clean up trailing None values
        result.pop()
    return result

# Convert Sorted List to Balanced BST 
class Test_BalancedBST(unittest.TestCase):    
    def test_BST_empty(self):    
        bst = BinarySearchTree()
        bst.sorted_list_to_bst([])
        self.assertTrue(check_balanced_and_correct_traversal(bst, []))

    def test_one_item(self):    
        bst = BinarySearchTree()
        bst.sorted_list_to_bst([10])
        
        self.assertTrue(check_balanced_and_correct_traversal(bst, [10]))

    def test_odd_num(self):    
        bst = BinarySearchTree()
        bst.sorted_list_to_bst([1, 2, 3, 4, 5])
        
        self.assertTrue(check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5]))

    def test_even_num(self):    
        bst = BinarySearchTree()
        bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6])
        
        self.assertTrue(check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5, 6]))

    def test_large_list(self):    
        bst = BinarySearchTree()
        large_sorted_list = list(range(1, 16))  # A list from 1 to 15
        bst.sorted_list_to_bst(large_sorted_list)
        
        self.assertTrue(check_balanced_and_correct_traversal(bst, large_sorted_list))

# Invert Binary Tree
class Test_invertBST(unittest.TestCase):    
    def test_BST_empty(self):
        setup, expected = [], []    

        bst = BinarySearchTree()
        for num in setup:
            bst.r_insert(num)

        bst.invert()  # Perform inversion (or second inversion for the specific case)
        result = tree_to_list(bst.root)

        self.assertEqual(result, expected)
        
    def test_BST_one_item(self):
        setup, expected = [1], [1]   

        bst = BinarySearchTree()
        for num in setup:
            bst.r_insert(num)

        bst.invert()  # Perform inversion (or second inversion for the specific case)
        result = tree_to_list(bst.root)

        self.assertEqual(result, expected)
    
    def test_BST_left_child(self):
        setup, expected = [2, 1], [2, None, 1]  

        bst = BinarySearchTree()
        for num in setup:
            bst.r_insert(num)

        bst.invert()  # Perform inversion (or second inversion for the specific case)
        result = tree_to_list(bst.root)

        self.assertEqual(result, expected)

    def test_BST_right_child(self):
        setup, expected = [1, 2], [1, 2]   

        bst = BinarySearchTree()
        for num in setup:
            bst.r_insert(num)

        bst.invert()  # Perform inversion (or second inversion for the specific case)
        result = tree_to_list(bst.root)

        self.assertEqual(result, expected)
    
    def test_multi(self):
        setup, expected = [3, 1, 5, 2], [3, 5, 1, None, None, 2]   

        bst = BinarySearchTree()
        for num in setup:
            bst.r_insert(num)

        bst.invert()  # Perform inversion (or second inversion for the specific case)
        result = tree_to_list(bst.root)

        self.assertEqual(result, expected)

    def test_invert_twice(self):
        setup, expected = [4, 2, 6, 1, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7]   

        bst = BinarySearchTree()
        for num in setup:
            bst.r_insert(num)

        bst.invert()  # Perform inversion (or second inversion for the specific case)
        bst.invert()
        result = tree_to_list(bst.root)

        self.assertEqual(result, expected)

        
if __name__ == '__main__':
    unittest.main()     
        