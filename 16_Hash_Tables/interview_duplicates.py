import unittest

def item_in_common_nested(list1, list2):
    for i in list1:
        for j in list2: 
            if i == j:
                return True
    return False

def item_in_common_dict(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    
    for j in list2:
        if j in my_dict:
            return True
    return False

 
#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+


# Nested_Loop
class Test_Nested_Loop(unittest.TestCase):    
    def test_empty(self):    
        list1 = [1]
        list2 = []

        self.assertFalse(item_in_common_nested(list1, list2))

    def test_with_duplicates(self):    
        list1 = [1]
        list2 = [1, 2]

        self.assertTrue(item_in_common_nested(list1, list2))

    def test_with_no_duplicates(self):    
        list1 = [1]
        list2 = [3, 2]

        self.assertFalse(item_in_common_nested(list1, list2))

# Dictionary
class Test_Dictionary(unittest.TestCase):    
    def test_empty(self):    
        list1 = [1]
        list2 = []

        self.assertFalse(item_in_common_dict(list1, list2))

    def test_with_duplicates(self):    
        list1 = [1]
        list2 = [1, 2]

        self.assertTrue(item_in_common_dict(list1, list2))

    def test_with_no_duplicates(self):    
        list1 = [1]
        list2 = [3, 2]

        self.assertFalse(item_in_common_dict(list1, list2))


if __name__ == '__main__':
    unittest.main()    