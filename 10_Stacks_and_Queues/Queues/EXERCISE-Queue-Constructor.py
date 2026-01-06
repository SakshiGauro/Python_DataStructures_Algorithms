import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self, value=None):
        if value is None:
            self.first = None
            self.last = None
            self.length = 0
        else:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0: # empty
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0: # empty
            return None
        temp = self.first
        if self.length == 1: # only 1 Item
            self.first = None
            self.last = None
        else: 
            self.first = self.first.next
            temp.next = None
        self.length -= 1 
        return temp

    def to_queue(self):
        values = []
        current = self.first
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
    def test_queue_init(self):    
        queue = Queue(7)

        self.assertIsNotNone(queue)

    def test_first(self):    
        queue = Queue(7)

        self.assertEqual(queue.first.value, 7)\
    
    def test_tail(self):    
        queue = Queue(7)

        self.assertEqual(queue.last.value, 7)

    def test_length(self):    
        queue = Queue(7)

        self.assertEqual(queue.length, 1)

    def test_node_next(self):    
        queue = Queue(7)

        self.assertIsNone(queue.first.next)

    def test_value(self):    
        queue = Queue(7)

        self.assertEqual(queue.first.value, 7)

# Enqueue
class Test_Enqueue(unittest.TestCase): 
    def test_non_empty_queue(self):    
        queue = Queue(7)
        queue.enqueue(5)

        self.assertEqual(queue.to_queue(), [7, 5])
    
    def test_multi_values(self):    
        queue = Queue(7)
        queue.enqueue(5)
        queue.enqueue(4)
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)

        self.assertEqual(queue.to_queue(), [7, 5, 4, 3, 2, 1])
    
    def test_first_change(self):    
        queue = Queue(7)
        queue.enqueue(5)

        self.assertEqual(queue.first.value, 7)
    
    def test_last_change(self):    
        queue = Queue(7)
        queue.enqueue(5)

        self.assertEqual(queue.last.value, 5)
    
    def test_length_change(self):    
        queue = Queue(7)
        queue.enqueue(5)

        self.assertEqual(queue.length, 2)

    def test_empty_queue(self):    
        queue = Queue()
        queue.enqueue(5)

        self.assertEqual(queue.to_queue(), [5])

# Dequeue
class Test_Dequeue(unittest.TestCase): 
    def test_empty_queue(self):    
        queue = Queue()
        result = queue.dequeue()

        self.assertIsNone(result)

    def test_first_change(self):    
        queue = Queue(7)
        queue.enqueue(5)

        queue.dequeue()

        self.assertEqual(queue.first.value, 5)

    def test_length_change(self):    
        queue = Queue(7)
        queue.enqueue(5)
        queue.enqueue(3)

        queue.dequeue()

        self.assertEqual(queue.length, 2)

    def test_single_item(self):    
        queue = Queue(7)
        result = queue.dequeue()

        self.assertEqual(result.value, 7)

    def test_dequeue_until_empty(self):    
        queue = Queue(7)
        queue.enqueue(5)
        queue.enqueue(4)

        queue.dequeue()
        queue.dequeue()
        queue.dequeue()

        self.assertEqual(queue.to_queue(), [])


if __name__ == '__main__':
    unittest.main()
