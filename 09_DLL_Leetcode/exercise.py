import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        
        if self.head is None: # Empty List
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True
    
    def is_palindrome(self):
        if (self.length == 0 or self.length == 1): # empty list and one item 
            return True
        
        forward = self.head
        backward = self.tail
        for _ in range(int(self.length/2)): 
            if (forward.value != backward.value):
                return False
            forward = forward.next
            backward = backward.prev
        return True
    
    def reverse(self):
        if (self.length > 1): # only run this for more than one item
            current = self.head
            temp = None
            
            while(current):
                temp = current.prev
                current.prev = current.next
                current.next = temp
                current = current.prev
            
            temp = self.head
            self.head = self.tail
            self.tail = temp

    def partition_list(self, x):
        if (self.length > 1):
            D1 = Node(0)
            D2 = Node(0)
            dummy1 = D1
            dummy2 = D2
            
            current = self.head
            while(current):
                if(current.value < x):
                    dummy1.next = current
                    current.prev = dummy1
                    dummy1 = dummy1.next
                    
                else:
                    dummy2.next = current
                    current.prev = dummy2
                    dummy2 = dummy2.next
                
                current = current.next
            
            dummy1.next = D2.next
            if (D2.next):   
                D2.next.prev = dummy1
            dummy2.next = None
            self.head = D1.next
            self.head.prev = None

    def reverse_between(self, start_index, end_index):
        if (start_index < 0 or end_index > self.length or self.length <= 1): # IOOB and only one item in list
            return
        
        dummy = Node(0)
        dummy.next = self.head
        prev_node = dummy
        
        for _ in range (start_index):
            prev_node = prev_node.next
        
        current = prev_node.next
        
        for _ in range (end_index - start_index):
            node_to_move = current.next
            
            current.next = node_to_move.next
            if node_to_move.next:
                node_to_move.next.prev = current
            
            node_to_move.next = prev_node.next
            prev_node.next.prev = node_to_move
            
            prev_node.next = node_to_move
            node_to_move.prev = prev_node
            
        self.head = dummy.next
        self.head.prev = None

    def swap_pairs (self):
        if (self.length > 1): # list has more than 1 Node
            dummy = Node(0)
            dummy.next = self.head
            
            prev = dummy
            current = self.head
            
            while(current and current.next): 
                after = current.next
                
                prev.next = after
                after.prev = prev
                
                current.next = after.next
                after.prev = current
                
                after.next = current
                current.prev = after
                
                prev = current
                current = current.next
            
            self.head = dummy.next
            dummy.next = None
            self.head.prev = None

    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values
    
#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+


# Palindrome
class Test_Palindrome(unittest.TestCase):    
    def test_even_palindrome_long(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(2)
        DLL.append(3)
        DLL.append(3)
        DLL.append(2)
        DLL.append(1)

        self.assertTrue(DLL.is_palindrome())

    def test_odd_palindrome_long(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(2)
        DLL.append(3)
        DLL.append(2)
        DLL.append(1)

        self.assertTrue(DLL.is_palindrome())

    def test_odd_not_palindrome(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(2)
        DLL.append(3)
        DLL.append(5)
        DLL.append(1)

        self.assertFalse(DLL.is_palindrome())

    def test_even_not_palindrome(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(2)
        DLL.append(3)
        DLL.append(1)
        DLL.append(5)
        DLL.append(1)

        self.assertFalse(DLL.is_palindrome())

    def test_palindrome_short(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(1)

        self.assertTrue(DLL.is_palindrome())

    def test_not_palindrome_short(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(2)

        self.assertFalse(DLL.is_palindrome())

    def test_palindrome_single(self):    
        DLL = DoublyLinkedList(1)

        self.assertTrue(DLL.is_palindrome())

    def test_empty(self):    
        DLL = DoublyLinkedList()

        self.assertTrue(DLL.is_palindrome())


# Reverse
class Test_Reverse(unittest.TestCase):    
    def test_multiple(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(2)
        DLL.append(3)
        DLL.append(4)
        DLL.reverse()

        self.assertEqual(DLL.to_list(), [4, 3, 2, 1])
    
    def test_same_item(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(1)
        DLL.append(1)
        DLL.reverse()

        self.assertEqual(DLL.to_list(), [1, 1, 1])
    
    def test_single(self):    
        DLL = DoublyLinkedList(1)
        DLL.reverse()

        self.assertEqual(DLL.to_list(), [1])

    def test_empty(self):    
        DLL = DoublyLinkedList()
        DLL.reverse()

        self.assertEqual(DLL.to_list(), [])


# Partition List
class Partition_List(unittest.TestCase):    
    def test_normal_case(self):    
        dll = DoublyLinkedList(3)
        dll.append(1)
        dll.append(4)
        dll.append(2)
        dll.append(5)
        x = 3

        dll.partition_list(x)
        self.assertEqual(dll.to_list(), [1, 2, 3, 4, 5])

    def test_all_equal(self):    
        dll = DoublyLinkedList(3)
        dll.append(3)
        dll.append(3)
        x = 3

        dll.partition_list(x)
        self.assertEqual(dll.to_list(), [3, 3, 3])

    def test_one_element(self):    
        dll = DoublyLinkedList(1)
        x = 3

        dll.partition_list(x)
        self.assertEqual(dll.to_list(), [1])

    def test_already_sorted(self):    
        dll = DoublyLinkedList(1)
        dll.append(2)
        dll.append(3)
        x = 2

        dll.partition_list(x)
        self.assertEqual(dll.to_list(), [1, 2, 3])

    def test_reverse_sorted(self):    
        dll = DoublyLinkedList(3)
        dll.append(2)
        dll.append(1)
        x = 2

        dll.partition_list(x)
        self.assertEqual(dll.to_list(), [1, 3, 2])

    def test_all_smaller(self):    
        dll = DoublyLinkedList(1)
        dll.append(1)
        dll.append(1)
        x = 2

        dll.partition_list(x)
        self.assertEqual(dll.to_list(), [1, 1, 1])

    def test_all_larger(self):    
        dll = DoublyLinkedList(3)
        dll.append(3)
        dll.append(3)
        x = 2

        dll.partition_list(x)
        self.assertEqual(dll.to_list(), [3, 3, 3])

    def test_single_equal_to_x(self):    
        dll = DoublyLinkedList(2)
        x = 2

        dll.partition_list(x)
        self.assertEqual(dll.to_list(), [2])

    def test_empty_list(self):    
        dll = DoublyLinkedList()
        x = 0 

        dll.partition_list(x)
        self.assertEqual(dll.to_list(), [])


# Reverse Between
class Reverse_Between(unittest.TestCase):    
    def test_middle_elements(self):    
        dll = DoublyLinkedList(1)
        dll.append(2)
        dll.append(3)
        dll.append(4)
        dll.append(5)

        dll.reverse_between(2, 4)
        self.assertEqual(dll.to_list(), [1, 2, 5, 4, 3])

    def test_entire_list(self):    
        dll = DoublyLinkedList(1)
        dll.append(2)
        dll.append(3)
        dll.append(4)
        dll.append(5)

        dll.reverse_between(0, 4)
        self.assertEqual(dll.to_list(), [5, 4, 3, 2, 1])

    def test_one_element(self):    
        dll = DoublyLinkedList(1)

        dll.reverse_between(0, 0)
        self.assertEqual(dll.to_list(), [1])

    def test_only_one_element(self):    
        dll = DoublyLinkedList(1)
        dll.append(2)
        dll.append(3)
        dll.append(4)
        dll.append(5)

        dll.reverse_between(3, 3)
        self.assertEqual(dll.to_list(), [1, 2, 3, 4, 5])

    def test_empty_list(self):    
        dll = DoublyLinkedList()

        dll.reverse_between(0, 0)
        self.assertEqual(dll.to_list(), [])

# Swap Nodes
class Swap_Nodes(unittest.TestCase):    
    def test_even_nodes(self):    
        dll1 = DoublyLinkedList(1)
        dll1.append(2)
        dll1.append(3)
        dll1.append(4)

        dll1.swap_pairs()
        self.assertEqual(dll1.to_list(), [2, 1, 4, 3])

    def test_odd_nodes(self):    
        dll1 = DoublyLinkedList(1)
        dll1.append(2)
        dll1.append(3)
        dll1.append(4)
        dll1.append(5)

        dll1.swap_pairs()
        self.assertEqual(dll1.to_list(), [2, 1, 4, 3, 5])

    def test_one_element(self):    
        dll = DoublyLinkedList(1)

        dll.swap_pairs()
        self.assertEqual(dll.to_list(), [1])

    def test_only_two_elements(self):    
        dll = DoublyLinkedList(1)
        dll.append(2)

        dll.swap_pairs()
        self.assertEqual(dll.to_list(), [2, 1])

    def test_empty_list(self):    
        dll = DoublyLinkedList()

        dll.swap_pairs()
        self.assertEqual(dll.to_list(), [])


if __name__ == '__main__':
    unittest.main()