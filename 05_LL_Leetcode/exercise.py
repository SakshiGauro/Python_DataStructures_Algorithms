import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        

    def find_middle_node (self):
        slow = self.head
        fast = self.head
        
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            
        return slow


    def has_loop (self):
        slow = self.head
        fast = self.head
        
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            
            if (slow == fast): # it is a loop!
                return True
                
        return False
    
    def remove_duplicates(self):
        if (self.length > 1):
            current = self.head
            
            while(current):
                runner = current
                while(runner.next):
                    if (current.value == runner.next.value):
                        runner.next = runner.next.next
                        self.length -= 1
                    else:
                        runner = runner.next
                
                current = current.next    

    def binary_to_decimal (self):
        if (self.head is not None): # not an empty list
            decimal_node = self.head
            decimal = decimal_node.value
            
            while(decimal_node.next):
                decimal = (decimal * 2) + (decimal_node.next.value)
                decimal_node = decimal_node.next
                
            return decimal
    
    def partition_list (self, x):
        if (self.length > 1): # LL has more than one node
            D1 = Node(0) # less than x
            D2 = Node(0) # greater than or equal to x
            prev1 = D1
            prev2 = D2
            
            current = self.head
            while(current):
                # less than x
                if (current.value < x):
                    prev1.next = current
                    prev1 = prev1.next
                else:
                    prev2.next = current
                    prev2 = prev2.next
                
                current = current.next
            
            prev2.next = None
            prev1.next = D2.next
            self.head = D1.next
        
    def reverse_between (self, start_index, end_index):
        if self.length <= 1: 
            return None
        
        dummy = Node(0)
        dummy.next = self.head
        prev_node = dummy
        
        for i in range(start_index):
            prev_node = prev_node.next
            
        current = prev_node.next
        for _ in range (end_index - start_index):
            node_to_move = current.next
            current.next = node_to_move.next
            node_to_move.next = prev_node.next
            prev_node.next = node_to_move
        
        self.head = dummy.next

    def swap_pairs(self):
        if (self.length > 1): # List has more than one nodes
            
            dummy = Node(0)
            dummy.next = self.head
            
            prev = dummy
            current = self.head
            
            while(current and current.next):
                after = current.next
                
                prev.next = after
                current.next  = after.next
                after.next = current
                
                prev = current
                current = current.next
                    
            
            self.head = dummy.next

    def to_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

def find_kth_from_end(ll, k):       
    slow = ll.head
    fast = ll.head
    
    for _ in range(k): # move k nodes
        if (fast is None): # list is shorter than k nodes
            return None
        fast = fast.next
            
    while(fast is not None):
        slow = slow.next # move one node 
        fast = fast.next
        
    return slow
    

#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+


# Find Middle Node

class Test_Middle_Node(unittest.TestCase):    
    def test_odd_num_list(self):    
        middle_node_list = LinkedList(1)
        middle_node_list.append(2)
        middle_node_list.append(3)
        middle_node_list.append(4)
        middle_node_list.append(5)

        self.assertEqual(middle_node_list.find_middle_node().value, 3)

    def test_even_num_list(self):    
        middle_node_list = LinkedList(1)
        middle_node_list.append(2)
        middle_node_list.append(3)
        middle_node_list.append(4)

        self.assertEqual(middle_node_list.find_middle_node().value, 3)

    def test_one_num_list(self):    
        middle_node_list = LinkedList(1)

        self.assertEqual(middle_node_list.find_middle_node().value, 1)

    def test_empty_list(self):    
        middle_node_list = LinkedList(None)

        self.assertEqual(middle_node_list.find_middle_node().value, None)

# Has Loop
class Test_Has_Loop(unittest.TestCase):    
    def test_has_loop_list(self):    
        has_loop_list = LinkedList(1)
        has_loop_list.append(2)
        has_loop_list.append(3)
        has_loop_list.append(4)
        has_loop_list.tail.next = has_loop_list.head

        self.assertTrue(has_loop_list.has_loop())

    def test_no_loop_list(self):    
        no_loop_list = LinkedList(1)
        no_loop_list.append(2)
        no_loop_list.append(3)
        no_loop_list.append(4)

        self.assertFalse(no_loop_list.has_loop())

    def test_empty_list(self):    
        empty_list = LinkedList(None)

        self.assertFalse(empty_list.has_loop())

# Kth Node from End
class Kth_Node_End(unittest.TestCase):    
    def test_k_equal_to_length(self):    
        kth_node_list = LinkedList(1)
        kth_node_list.append(2)
        kth_node_list.append(3)
        kth_node_list.append(4)
        kth_node_list.append(5)

        k = 5
        result = find_kth_from_end(kth_node_list, k)

        self.assertEqual(result.value, 1)

    def test_k_less_than_length(self):    
        kth_node_list = LinkedList(1)
        kth_node_list.append(2)
        kth_node_list.append(3)
        kth_node_list.append(4)
        kth_node_list.append(5)

        k = 2
        result = find_kth_from_end(kth_node_list, k)

        self.assertEqual(result.value, 4)

    def test_k_more_than_length(self):    
        kth_node_list = LinkedList(1)
        kth_node_list.append(2)
        kth_node_list.append(3)
        kth_node_list.append(4)
        kth_node_list.append(5)

        k = 6
        result = find_kth_from_end(kth_node_list, k)

        self.assertEqual(result, None)

    def test_empty_list(self):    
        empty = LinkedList(None)
        result = find_kth_from_end(empty, k=0)

        self.assertEqual(result, None)    

# Remove Duplicates
class Remove_Duplicates(unittest.TestCase):    
    def test_no_duplicates(self):    
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        
        ll.remove_duplicates()
        self.assertEqual(ll.to_list(), [1, 2, 3])

    def test_some_duplicates(self):    
        ll = LinkedList(1)
        ll.append(2)
        ll.append(1)
        ll.append(3)
        ll.append(2)

        ll.remove_duplicates()
        self.assertEqual(ll.to_list(), [1, 2, 3])

    def test_all_duplicates(self):    
        ll = LinkedList(1)
        ll.append(1)
        ll.append(1)

        ll.remove_duplicates()
        self.assertEqual(ll.to_list(), [1])
    
    def test_consecutive_duplicates(self):    
        ll = LinkedList(1)
        ll.append(1)
        ll.append(2)
        ll.append(2)
        ll.append(3)

        ll.remove_duplicates()
        self.assertEqual(ll.to_list(), [1, 2, 3])
    
    def test_non_consecutive_duplicates(self):    
        ll = LinkedList(1)
        ll.append(2)
        ll.append(1)
        ll.append(3)
        ll.append(2)
        ll.append(4)

        ll.remove_duplicates()
        self.assertEqual(ll.to_list(), [1, 2, 3, 4])

    def test_end_duplicates(self):    
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        ll.append(3)

        ll.remove_duplicates()
        self.assertEqual(ll.to_list(), [1, 2, 3])

    def test_empty_list(self):    
        ll = LinkedList(None)
        ll.head = None  # Directly setting the head to None
        ll.length = 0   # Adjusting the length to reflect an empty list

        ll.remove_duplicates()
        self.assertEqual(ll.to_list(), [])


# Binary To Decimal Duplicates
class Binary_To_Decimal(unittest.TestCase):    
    def test_binary_0(self):    
        # Binary number 0 = Decimal number 0
        linked_list = LinkedList(0)
        self.assertEqual(linked_list.binary_to_decimal(), 0)

    def test_binary_1(self):    
        # Binary number 1 = Decimal number 1
        linked_list = LinkedList(1)
        self.assertEqual(linked_list.binary_to_decimal(), 1)

    def test_binary_110(self):    
        # Binary number 110 = Decimal number 6
        linked_list = LinkedList(1)
        linked_list.append(1)
        linked_list.append(0)
        self.assertEqual(linked_list.binary_to_decimal(), 6)
  
    def test_binary_1000(self):    
        # Binary number 1000 = Decimal number 8
        linked_list = LinkedList(1)
        linked_list.append(0)
        linked_list.append(0)
        linked_list.append(0)

        self.assertEqual(linked_list.binary_to_decimal(), 8)
    
    def test_binary_1101(self):    
        # Binary number 1101 = Decimal number 13
        linked_list = LinkedList(1)
        linked_list.append(1)
        linked_list.append(0)
        linked_list.append(1)

        self.assertEqual(linked_list.binary_to_decimal(), 13)

    def test_empty_list(self):    
        ll = LinkedList(None)
        ll.head = None  # Directly setting the head to None
        ll.length = 0   # Adjusting the length to reflect an empty list

        self.assertEqual(ll.binary_to_decimal(), None)


# Partition List
class Partition_List(unittest.TestCase):    
    def test_normal_case(self):    
        ll = LinkedList(3)
        ll.append(1)
        ll.append(4)
        ll.append(2)
        ll.append(5)
        x = 3

        ll.partition_list(x)
        self.assertEqual(ll.to_list(), [1, 2, 3, 4, 5])

    def test_all_equal(self):    
        ll = LinkedList(3)
        ll.append(3)
        ll.append(3)
        x = 3

        ll.partition_list(x)
        self.assertEqual(ll.to_list(), [3, 3, 3])

    def test_one_element(self):    
        ll = LinkedList(1)
        x = 3

        ll.partition_list(x)
        self.assertEqual(ll.to_list(), [1])

    def test_already_sorted(self):    
        ll = LinkedList(1)
        ll.append(2)
        ll.append(3)
        x = 2

        ll.partition_list(x)
        self.assertEqual(ll.to_list(), [1, 2, 3])

    def test_reverse_sorted(self):    
        ll = LinkedList(3)
        ll.append(2)
        ll.append(1)
        x = 2

        ll.partition_list(x)
        self.assertEqual(ll.to_list(), [1, 3, 2])

    def test_all_smaller(self):    
        ll = LinkedList(1)
        ll.append(1)
        ll.append(1)
        x = 2

        ll.partition_list(x)
        self.assertEqual(ll.to_list(), [1, 1, 1])

    def test_all_larger(self):    
        ll = LinkedList(3)
        ll.append(3)
        ll.append(3)
        x = 2

        ll.partition_list(x)
        self.assertEqual(ll.to_list(), [3, 3, 3])

    def test_single_equal_to_x(self):    
        ll = LinkedList(2)
        x = 2

        ll.partition_list(x)
        self.assertEqual(ll.to_list(), [2])

    def test_empty_list(self):    
        ll = LinkedList(None)
        ll.head = None  # Directly setting the head to None
        ll.length = 0   # Adjusting the length to reflect an empty list
        x = 0 

        ll.partition_list(x)
        self.assertEqual(ll.to_list(), [])

# Reverse Between
class Reverse_Between(unittest.TestCase):    
    def test_middle_elements(self):    
        linked_list = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)

        linked_list.reverse_between(2, 4)
        self.assertEqual(linked_list.to_list(), [1, 2, 5, 4, 3])

    def test_entire_list(self):    
        linked_list = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)

        linked_list.reverse_between(0, 4)
        self.assertEqual(linked_list.to_list(), [5, 4, 3, 2, 1])

    def test_one_element(self):    
        linked_list = LinkedList(1)

        linked_list.reverse_between(0, 0)
        self.assertEqual(linked_list.to_list(), [1])

    def test_only_one_element(self):    
        linked_list = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)

        linked_list.reverse_between(3, 3)
        self.assertEqual(linked_list.to_list(), [1, 2, 3, 4, 5])

    def test_empty_list(self):    
        ll = LinkedList(None)
        ll.head = None  # Directly setting the head to None
        ll.length = 0   # Adjusting the length to reflect an empty list

        ll.reverse_between(0, 0)
        self.assertEqual(ll.to_list(), [])

# Swap Nodes
class Swap_Nodes(unittest.TestCase):    
    def test_even_nodes(self):    
        ll1 = LinkedList(1)
        ll1.append(2)
        ll1.append(3)
        ll1.append(4)

        ll1.swap_pairs()
        self.assertEqual(ll1.to_list(), [2, 1, 4, 3])

    def test_odd_nodes(self):    
        ll1 = LinkedList(1)
        ll1.append(2)
        ll1.append(3)
        ll1.append(4)
        ll1.append(5)

        ll1.swap_pairs()
        self.assertEqual(ll1.to_list(), [2, 1, 4, 3, 5])

    def test_one_element(self):    
        linked_list = LinkedList(1)

        linked_list.swap_pairs()
        self.assertEqual(linked_list.to_list(), [1])

    def test_only_two_elements(self):    
        linked_list = LinkedList(1)
        linked_list.append(2)

        linked_list.swap_pairs()
        self.assertEqual(linked_list.to_list(), [2, 1])

    def test_empty_list(self):    
        ll = LinkedList(None)
        ll.head = None  # Directly setting the head to None
        ll.length = 0   # Adjusting the length to reflect an empty list

        ll.swap_pairs()
        self.assertEqual(ll.to_list(), [])


if __name__ == '__main__':
    unittest.main()
