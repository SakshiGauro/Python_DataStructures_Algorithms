import unittest

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self, value):
        # make sure stack1 is empty
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
            
        self.stack1.append(value)
        
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.is_empty():
            return None
        return self.stack1.pop()
    
    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0

# Enqueue
class Test_Sort_Stack(unittest.TestCase): 
    def test_non_empty_queue(self):    
        queue = MyQueue()
        queue.enqueue(5)

        self.assertEqual(queue.stack1, [5])
    
    def test_multi_values(self):    
        queue = MyQueue()
        queue.enqueue(5)
        queue.enqueue(4)
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)

        self.assertEqual(queue.stack1, [1, 2, 3, 4, 5])
    
    def test_not_empty(self):    
        queue = MyQueue()
        queue.enqueue(5)

        self.assertFalse(queue.is_empty())

# Dequeue
class Test_Dequeue(unittest.TestCase): 
    def test_empty_queue(self):    
        queue = MyQueue()
        result = queue.dequeue()

        self.assertIsNone(result)

    def test_first_change(self):    
        queue = MyQueue()
        queue.enqueue(5)

        result = queue.dequeue()

        self.assertEqual(result, 5)

    def test_length_change(self):    
        queue = MyQueue()
        queue.enqueue(5)
        queue.enqueue(3)

        queue.dequeue()

        self.assertEqual(len(queue.stack1), 1)

    def test_multi_items(self):    
        queue = MyQueue()
        
        queue.enqueue(5)
        queue.enqueue(3)
        queue.enqueue(2)
        queue.enqueue(1)

        queue.dequeue()
        queue.dequeue()

        self.assertEqual(queue.stack1, [1, 2])

    def test_dequeue_until_empty(self):    
        queue = MyQueue()
        queue.enqueue(5)
        queue.enqueue(4)

        queue.dequeue()
        queue.dequeue()

        self.assertTrue(queue.is_empty())

if __name__ == '__main__':
    unittest.main()     
        
