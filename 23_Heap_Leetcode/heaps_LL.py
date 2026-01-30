import unittest

class MaxHeap:
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

    def insert (self, value):
        self.heap.append(value)
        current = len(self.heap) - 1 
        
        while(current > 0 and self.heap[current] > self.heap[self._parent(current)]):
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0: # empty
            return None
        elif len(self.heap) == 1: # only one item
            return self.heap.pop()
        max_value = self.heap[0]    
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value
    
    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and 
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and 
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

def find_kth_smallest(nums, k):
    my_heap = MaxHeap()
    
    for num in nums: 
        my_heap.insert(num)
        if len(my_heap.heap) > k: 
            my_heap.remove()
            
    return my_heap.remove()

def stream_max(nums):
    my_heap = MaxHeap()
    max_stream = []
    
    for num in nums:
        my_heap.insert(num)
        max_stream.append(my_heap.heap[0])

    return max_stream

#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+

# Kth Smallest Element 
class Test_Kth_Smallest_Element (unittest.TestCase): 
    def test_empty(self):    
        nums = []
        k = 0

        self.assertIsNone(find_kth_smallest(nums, k))
    
    def test_random(self):    
        nums = [3, 1, 2, 5, 4]

        k = 2

        self.assertEqual(find_kth_smallest(nums, k), 2)

    def test_ascending(self):    
        nums = [0, 1, 2, 3, 4]
        
        k = 3

        self.assertEqual(find_kth_smallest(nums, k), 2)
    
    def test_descending(self):    
        nums = [10, 9, 8, 7, 6]
        
        k = 3

        self.assertEqual(find_kth_smallest(nums, k), 8)

    def test_duplicates(self):    
        nums = [9, 9, 8, 7, 6, 6]

        k = 3

        self.assertEqual(find_kth_smallest(nums, k), 7)

# Maximum Element in a Stream
class Test_Max_Element (unittest.TestCase): 
    def test_empty(self):    
        nums = []

        self.assertEqual(stream_max(nums), [])
    
    def test_single_item(self):    
        nums = [3]

        self.assertEqual(stream_max(nums), nums)
    
    def test_random(self):    
        nums = [3, 1, 2, 5, 4]

        self.assertEqual(stream_max(nums), [3, 3, 3, 5, 5])

    def test_ascending(self):    
        nums = [0, 1, 2, 3, 4]
        
        self.assertEqual(stream_max(nums), nums)
    
    def test_descending(self):    
        nums = [10, 9, 8, 7, 6]
        
        self.assertEqual(stream_max(nums), [10, 10, 10, 10, 10])

    def test_duplicates(self):    
        nums = [6, 2, 7, 7, 8, 6]

        self.assertEqual(stream_max(nums), [6, 6, 7, 7, 8, 8])


if __name__ == '__main__':
    unittest.main()     