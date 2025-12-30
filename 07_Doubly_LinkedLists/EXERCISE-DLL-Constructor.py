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

    def pop(self):
        if (self.length == 0): 
            return None
        elif (self.length == 1): 
            node = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return node
            
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if (self.length == 0): # list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if (self.length == 0): # list is empty
            return None
        elif (self.length == 1): # only 1 Item
            node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return node
        node = self.head
        self.head = self.head.next
        self.head.prev = None
        node.next = None
        self.length -= 1
        return node

    def get(self, index):
        if (index < 0 or index >= self.length): # Out of Bounds
            return None
            
        if index < (0.5 * self.length):
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value (self, index, value):
        temp = self.get(index)
        if (temp is not None):
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index == 0: # prepend
            return self.prepend(value)
        elif index == self.length: # append
            return self.append(value)
        
        if index >= 1 and index <= self.length:
            new_node = Node(value)
            node = self.get(index)
            
            before = node.prev
            node.prev = new_node
            before.next = new_node
            self.length += 1 
            return True
        return False

    def remove(self, index):
        if index < 0 or index >= self.length: # OOB
            return None
        elif index == 0: 
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp = self.get(index)
            temp.next.prev = temp.prev
            temp.prev = temp.next
            
            temp.prev = None
            temp.next = None
            
            self.length -= 1
            return temp
        
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


# Constructor
class Test_Constructor(unittest.TestCase):    
    def test_DLL_init(self):    
        DLL = DoublyLinkedList(7)

        self.assertIsNotNone(DLL)

    def test_head(self):    
        DLL = DoublyLinkedList(7)

        self.assertEqual(DLL.head.value, 7)

    def test_length(self):    
        DLL = DoublyLinkedList(7)

        self.assertEqual(DLL.length, 1)

    def test_tail(self):    
        DLL = DoublyLinkedList(7)

        self.assertEqual(DLL.tail.value, 7)

    def test_node_next(self):    
        DLL = DoublyLinkedList(7)

        self.assertIsNone(DLL.head.next)

    def test_node_prev(self):    
        DLL = DoublyLinkedList(7)

        self.assertIsNone(DLL.head.prev)

    def test_value(self):    
        DLL = DoublyLinkedList(7)

        self.assertEqual(DLL.head.value, 7)

# Append
class Test_Append(unittest.TestCase): 
    def test_non_empty_list(self):    
        DLL = DoublyLinkedList(7)
        DLL.append(5)

        self.assertEqual(DLL.to_list(), [7, 5])
    
    def test_empty_list(self):    
        DLL = DoublyLinkedList()
        DLL.append(5)

        self.assertEqual(DLL.to_list(), [5])

# Pop
class Test_Pop(unittest.TestCase): 
    def test_empty_list(self):    
        DLL = DoublyLinkedList()
        result = DLL.pop()

        self.assertIsNone(result)

    def test_single_item(self):    
        DLL = DoublyLinkedList(7)
        result = DLL.pop()

        self.assertEqual(result.value, 7)

    def test_multiple_items(self):    
        DLL = DoublyLinkedList(7)
        DLL.append(5)
        DLL.append(4)

        result = DLL.pop()

        self.assertEqual(result.value, 4)

# Prepend
class Test_Prepend(unittest.TestCase): 
    def test_empty_list(self):    
        DLL = DoublyLinkedList()
        DLL.prepend(5)

        self.assertEqual(DLL.to_list(), [5])
    
    def test_one_item(self):    
        DLL = DoublyLinkedList(1)
        DLL.prepend(5)

        self.assertEqual(DLL.to_list(), [5, 1])
    
    def test_multi_items(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(3)
        DLL.prepend(5)

        self.assertEqual(DLL.to_list(), [5, 1, 3])

# Pop First
class Test_Pop_First(unittest.TestCase): 
    def test_empty_list(self):    
        DLL = DoublyLinkedList()
        result = DLL.pop_first()

        self.assertIsNone(result)

    def test_single_item(self):    
        DLL = DoublyLinkedList(7)
        result = DLL.pop_first()

        self.assertEqual(result.value, 7)

    def test_multiple_items(self):    
        DLL = DoublyLinkedList(7)
        DLL.append(5)
        DLL.append(4)

        result = DLL.pop_first()

        self.assertEqual(result.value, 7)

# Get
class Test_Get(unittest.TestCase):    
    def test_out_of_range(self):    
        DLL = DoublyLinkedList(7)

        self.assertIsNone(DLL.get(3))

    def test_head(self):    
        DLL = DoublyLinkedList(7)

        self.assertEqual(DLL.get(0).value, 7)

    def test_neg_index(self):    
        DLL = DoublyLinkedList(7)

        self.assertIsNone(DLL.get(-1))

    def test_first_half(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(2)
        DLL.append(3)
        DLL.append(4)

        self.assertEqual(DLL.get(1).value, 2)

    def test_second_half(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(2)
        DLL.append(3)
        DLL.append(4)

        self.assertEqual(DLL.get(2).value, 3)

    def test_tail(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(2)
        DLL.append(3)
        DLL.append(4)

        self.assertEqual(DLL.get(3).value, 4)

    def test_empty(self):    
        DLL = DoublyLinkedList(None)

        self.assertIsNone(DLL.get(0))

# Set
class Test_Set(unittest.TestCase):    
    def test_at_head(self):    
        DLL = DoublyLinkedList(7)

        self.assertTrue(DLL.set_value(0, 2))

    def test_at_tail(self):    
        DLL = DoublyLinkedList(7)
        DLL.append(5)

        self.assertTrue(DLL.set_value(1, 4))

    def test_middle(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(2)
        DLL.append(3)
        DLL.append(4)

        self.assertTrue(DLL.set_value(3, 7))

    def test_invalid_index(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(2)
        DLL.append(3)
        DLL.append(4)

        self.assertFalse(DLL.set_value(7, 7))

# Insert
class Test_Insert(unittest.TestCase):    
    def test_at_beginning(self):    
        DLL = DoublyLinkedList(7)

        self.assertTrue(DLL.insert(0, 2))

    def test_at_end(self):    
        DLL = DoublyLinkedList(7)
        DLL.append(5)

        self.assertTrue(DLL.insert(1, 4))

    def test_middle(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(2)
        DLL.append(3)
        DLL.append(4)

        self.assertTrue(DLL.insert(3, 7))

    def test_invalid_oob(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(2)
        DLL.append(3)
        DLL.append(4)

        self.assertFalse(DLL.insert(7, 7))

    def test_invalid_neg(self):    
        DLL = DoublyLinkedList(1)
        DLL.append(2)
        DLL.append(3)
        DLL.append(4)

        self.assertFalse(DLL.insert(-1, 7))

# Remove
class Test_Remove(unittest.TestCase): 
    def test_empty_list(self):    
        DLL = DoublyLinkedList()
        result = DLL.remove(0)

        self.assertIsNone(result)

    def test_beginning(self):    
        DLL = DoublyLinkedList(7)
        DLL.append(5)
        DLL.append(4)
        result = DLL.remove(0)

        self.assertEqual(result.value, 7)

    def test_end(self):    
        DLL = DoublyLinkedList(7)
        DLL.append(5)
        DLL.append(4)
        result = DLL.remove(2)

        self.assertEqual(result.value, 4)

    def test_middle(self):    
        DLL = DoublyLinkedList(7)
        DLL.append(5)
        DLL.append(4)
        result = DLL.remove(1)

        self.assertEqual(result.value, 5)

    def test_OOB(self):    
        DLL = DoublyLinkedList(7)
        DLL.append(5)
        DLL.append(4)
        result = DLL.remove(4)

        self.assertIsNone(result)

    def test_neg(self):    
        DLL = DoublyLinkedList(7)
        DLL.append(5)
        DLL.append(4)
        result = DLL.remove(-1)

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
