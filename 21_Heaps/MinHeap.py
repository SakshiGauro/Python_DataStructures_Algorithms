import unittest

class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value): 
        self.heap.append(value)
        current = len(self.heap) - 1 
        
        while (current > 0 and self.heap[current] < self.heap[self._parent(current)]):
            self._swap(current, self._parent(current))
            current = self._parent(current)
    
    def remove(self): 
        if len(self.heap) == 0: # empty
            return None
        elif len(self.heap) == 1: # only one item
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return min_val
    
    def _sink_down(self, index):
        min_index = index
        
        while (True):
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            
            if (left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]):
                min_index = left_index
            
            if (right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]): 
                min_index = right_index
                
            if min_index != index:
                self._swap(index, min_index)
                index = min_index
            else:
                return
            
            
#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+


# Constructor
class Test_Constructor(unittest.TestCase):    
    def test_init(self):    
        my_heap = MinHeap()

        self.assertIsNotNone(my_heap)

# Insert
class Test_Insert(unittest.TestCase): 
    def test_insert_empty(self):    
        my_heap = MinHeap()
        my_heap.insert(10)

        self.assertEqual(my_heap.heap[0], 10)
    
    def test_insert_duplicate(self):    
        my_heap = MinHeap()
        my_heap.insert(5)
        my_heap.insert(5)

        self.assertEqual(my_heap.heap[1], 5)

    def test_insert_greater_than_root(self):    
        my_heap = MinHeap()
        my_heap.insert(5)
        my_heap.insert(10)

        self.assertEqual(my_heap.heap[0], 5)
    
    def test_insert_less_than_root(self):    
        my_heap = MinHeap()
        my_heap.insert(5)
        my_heap.insert(2)

        self.assertEqual(my_heap.heap[0], 2)

# Remove
class Test_Remove(unittest.TestCase): 
    def test_remove_empty(self):    
        my_heap = MinHeap()
        
        self.assertIsNone(my_heap.remove())
    
    def test_remove_one_item(self):    
        my_heap = MinHeap()
        my_heap.insert(5)

        self.assertEqual(my_heap.remove(), 5)

    def test_remove_until_empty(self):    
        my_heap = MinHeap()
        my_heap.insert(5)
        my_heap.insert(10)
        my_heap.insert(15)

        my_heap.remove()
        my_heap.remove()

        self.assertEqual(my_heap.remove(), 15)
    
    def test_remove_maintains_heap_property(self):    
        my_heap = MinHeap()
        my_heap.insert(5)
        my_heap.insert(10)
        my_heap.insert(15)

        my_heap.remove()

        self.assertEqual(my_heap.heap[0], 10)


if __name__ == '__main__':
    unittest.main()     