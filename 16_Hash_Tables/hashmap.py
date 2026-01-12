import unittest

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if (self.data_map[index] is None):
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if (self.data_map[index] is not None): 
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
                    
        return all_keys
    
#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+


# Constructor
class Test_Constructor(unittest.TestCase):    
    def test_HT_init(self):    
        ht = HashTable()

        self.assertIsNotNone(ht)

    def test_map_size(self):    
        ht = HashTable(5)

        self.assertEqual(len(ht.data_map), 5)


# Set Item
class Test_Set_Item(unittest.TestCase): 
    def test_set_empty_table(self):    
        ht = HashTable()
        ht.set_item('bolts', 1400)

        index = ht._HashTable__hash('bolts')
        self.assertEqual(ht.data_map[index], [['bolts', 1400]])
    
    def test_set_multiple_items(self):
        ht = HashTable()
        ht.set_item('bolts', 1400)
        ht.set_item('washers', 50)
        ht.set_item('lumber', 70)

        index1 = ht._HashTable__hash('bolts')
        index2 = ht._HashTable__hash('washers')
        index3 = ht._HashTable__hash('lumber')

        self.assertIn(['bolts', 1400], ht.data_map[index1])
        self.assertIn(['washers', 50], ht.data_map[index2])
        self.assertIn(['lumber', 70], ht.data_map[index3])

    def test_collision_handling(self):
        ht = HashTable(1)  # forceful collision
        ht.set_item('a', 1)
        ht.set_item('b', 2)

        index_a = ht._HashTable__hash('a')
        index_b = ht._HashTable__hash('b')

        # If they collide, both should exist in same bucket
        if index_a == index_b:
            self.assertEqual(len(ht.data_map[index_a]), 2)
            self.assertIn(['a', 1], ht.data_map[index_a])
            self.assertIn(['b', 2], ht.data_map[index_a])
        else:
            self.assertIn(['a', 1], ht.data_map[index_a])
            self.assertIn(['b', 2], ht.data_map[index_b])

# Get
class Test_Get(unittest.TestCase): 
    def test_empty(self):    
        ht = HashTable()

        self.assertIsNone(ht.get_item('not'))
    
    def test_value_exists(self):    
        ht = HashTable()
        ht.set_item('bolts', 1400)
        ht.set_item('washers', 50)
        ht.set_item('lumber', 70)

        self.assertEqual(ht.get_item('bolts'), 1400)
    
    def test_value_doesnt_exist(self):    
        ht = HashTable()
        ht.set_item('bolts', 1400)
        ht.set_item('washers', 50)
        ht.set_item('lumber', 70)

        self.assertIsNone(ht.get_item('nuts'))

    def test_get_item_collision(self):    
        ht = HashTable(1)  # forceful collision
        ht.set_item('a', 1)
        ht.set_item('b', 2)

        self.assertEqual(ht.get_item('a'), 1)

# keys 
class Test_keys(unittest.TestCase): 
    def test_empty(self):    
        ht = HashTable()

        self.assertEqual(ht.keys(), [])

    def test_single(self):    
        ht = HashTable()
        ht.set_item('bolts', 1400)

        self.assertEqual(ht.keys(), ['bolts'])
    
    def test_multiple(self):    
        ht = HashTable()
        ht.set_item('bolts', 1400)
        ht.set_item('washers', 50)
        ht.set_item('lumber', 70)

        self.assertEqual(ht.keys(), ['bolts', 'washers', 'lumber'])
    
    def test_collision(self):    
        ht = HashTable(1)
        ht.set_item('a', 1)
        ht.set_item('b', 2)

        self.assertEqual(ht.keys(), ['a', 'b'])

if __name__ == '__main__':
    unittest.main()     