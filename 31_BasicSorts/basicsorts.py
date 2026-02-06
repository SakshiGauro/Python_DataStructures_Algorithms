import unittest

def bubble_sort (my_list): 
    for i in range(len(my_list), 1, -1):
        for j in range(i - 1):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
                
    return my_list

def selection_sort(my_list):
    for i in range(0, len(my_list)):
        min_index = i
        for j in range(i+1, len(my_list)): 
            if my_list[j] < my_list[min_index]:
                min_index = j 
                
        if i != min_index: 
            # swap 
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp

    return my_list

def insertion_sort(my_list): 
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
            
    return my_list
#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+

# Bubble Sort
class Test_bubble_sort(unittest.TestCase): 
    def test_empty_stack(self):    
        my_list = []

        self.assertEqual(bubble_sort(my_list), my_list)
    
    def test_sorted(self):    
        my_list = [1, 2, 3, 4, 5, 7]

        self.assertEqual(bubble_sort(my_list), my_list)

    def test_unsorted(self):    
        my_list = [1, 3, 9, 4, 2, 7]
        result = [1, 2, 3, 4, 7, 9]

        self.assertEqual(bubble_sort(my_list), result)

    def test_reverse_sorted(self):    
        my_list = [7, 5, 4, 3, 2, 1]
        result = [1, 2, 3, 4, 5, 7]

        self.assertEqual(bubble_sort(my_list), result)

# Selection Sort
class Test_Selection_Sort(unittest.TestCase): 
    def test_empty_stack(self):    
        my_list = []

        self.assertEqual(selection_sort(my_list), my_list)
    
    def test_sorted(self):    
        my_list = [1, 2, 3, 4, 5, 7]

        self.assertEqual(selection_sort(my_list), my_list)

    def test_unsorted(self):    
        my_list = [1, 3, 9, 4, 2, 7]
        result = [1, 2, 3, 4, 7, 9]

        self.assertEqual(selection_sort(my_list), result)

    def test_reverse_sorted(self):    
        my_list = [7, 5, 4, 3, 2, 1]
        result = [1, 2, 3, 4, 5, 7]

        self.assertEqual(selection_sort(my_list), result)

# Insertion Sort
class Test_Insertion_Sort(unittest.TestCase): 
    def test_empty_stack(self):    
        my_list = []

        self.assertEqual(insertion_sort(my_list), my_list)
    
    def test_sorted(self):    
        my_list = [1, 2, 3, 4, 5, 7]

        self.assertEqual(insertion_sort(my_list), my_list)

    def test_unsorted(self):    
        my_list = [1, 3, 9, 4, 2, 7]
        result = [1, 2, 3, 4, 7, 9]

        self.assertEqual(insertion_sort(my_list), result)

    def test_reverse_sorted(self):    
        my_list = [7, 5, 4, 3, 2, 1]
        result = [1, 2, 3, 4, 5, 7]

        self.assertEqual(insertion_sort(my_list), result)


if __name__ == '__main__':
    unittest.main()     