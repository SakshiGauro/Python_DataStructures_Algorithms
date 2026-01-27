import unittest

def item_in_common(list1, list2): 
    my_dict = {}
    for i in list1:
        my_dict[i] = True
        
    for j in list2: 
        if j in my_dict: 
            return True
    
    return False

def find_duplicates(nums):
    duplicates = []
    my_dict = {}
    
    for i in nums: 
        if i in my_dict and i not in duplicates:
            duplicates.append(i)
        else:
            my_dict[i] = True
            
    return duplicates

def first_non_repeating_char(string):
    my_dict = {}
    
    for char in string:
        my_dict[char] = my_dict.get(char, 0) + 1
    
    for char in string:
        if my_dict[char] == 1:
            return char
    return None

def group_anagrams(strings):
    anagram_groups = {}
    
    for word in strings:
        canonical = ''.join(sorted(word))
        if canonical in anagram_groups:
            anagram_groups[canonical].append(word)
        else:
            anagram_groups[canonical] = [word]
            
    return list(anagram_groups.values())

def two_sum(nums, target):
    num_list = {}
    
    for index, num in enumerate (nums):
        complement = target - num
        if complement in num_list:
            return [num_list[complement], index]
        else:
            num_list[num] = index
            
    return []

def subarray_sum (nums, target):
    subarray = {0: -1}
    sum = 0
    
    for index, num in enumerate(nums):
        sum += num
        if (sum - target) in subarray:
            return [subarray[sum - target]+1,index]
        else:
            subarray[sum] = index
            
    return []

### SETS
def remove_duplicates(my_list):
    updated_list = set()
    for num in my_list:
        if not num in updated_list:
            updated_list.add(num)
            
    return list(updated_list)

def has_unique_chars(string):
    unique_chars = set()
    
    for char in string:
        if char in unique_chars:
            return False
        else:
            unique_chars.add(char)
    
    return True

def find_pairs(arr1, arr2, target):
    array1 = set(arr1)
    pairs_array = []
    
    for num in arr2: 
        if (target - num) in array1:
            pairs_array.append((target - num, num))
    
    return pairs_array

def longest_consecutive_sequence (nums):
    if (len(nums) == 0):
        return 0
        
    nums.sort()
    nums = list(dict.fromkeys(nums))
    
    set_array = set()
    long_seq = 0
    current_seq = 1
    
    for num in nums:
        if (num-1) in set_array: 
            current_seq += 1
        
        if not (num -1) in set_array:
            long_seq = max(long_seq, current_seq)
            current_seq = 1
        
        set_array.add(num)
    
    long_seq = max(long_seq, current_seq)
    return long_seq

#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+


# Item In Common
class Test_Item_In_Common(unittest.TestCase):    
    def test_empty(self):    
        my_list1 = []
        my_list2 = []

        self.assertFalse(item_in_common(my_list1, my_list2))

    def test_same_items(self):    
        my_list1 = [1, 2]
        my_list2 = [1, 2]

        self.assertTrue(item_in_common(my_list1, my_list2))
    
    def test_multi_same(self):    
        my_list1 = [1, 2]
        my_list2 = [1, 2, 3]

        self.assertTrue(item_in_common(my_list1, my_list2))

    def test_no_same(self):    
        my_list1 = [1, 2]
        my_list2 = [4, 3]

        self.assertFalse(item_in_common(my_list1, my_list2))

    def test_one_same(self):    
        my_list1 = [1, 2]
        my_list2 = [2, 3]

        self.assertTrue(item_in_common(my_list1, my_list2))
    
    def test_one_empty(self):    
        my_list1 = [1, 2]
        my_list2 = []

        self.assertFalse(item_in_common(my_list1, my_list2))

# Find Duplicates
class Test_Find_Duplicates(unittest.TestCase):    
    def test_empty(self):    
        my_list1 = []
        output =[]

        self.assertEqual(output, find_duplicates(my_list1))

    def test_one_item(self):    
        my_list1 = [1]
        output =[]

        self.assertEqual(output, find_duplicates(my_list1))
    
    def test_multi(self):    
        my_list1 = [1, 2, 1, 2, 3]
        output =[1, 2]

        self.assertEqual(output, find_duplicates(my_list1))

    def test_no_duplicates(self):    
        my_list1 = [1, 2]
        output =[]

        self.assertEqual(output, find_duplicates(my_list1))

    def test_one_duplicate(self):    
        my_list1 = [1, 2, 1]
        output =[1]

        self.assertEqual(output, find_duplicates(my_list1))
    
    def test_all_dupli(self):    
        my_list1 = [2, 2, 2]
        output =[2]

        self.assertEqual(output, find_duplicates(my_list1))

# First Non-Repeating Character
class Test_First_Non_Repeating_Character(unittest.TestCase):    
    def test_empty(self):    
        my_string = ''
        output = None

        self.assertEqual(output, first_non_repeating_char(my_string))

    def test_normal(self):    
        my_string = 'hello'
        output = 'h'

        self.assertEqual(output, first_non_repeating_char(my_string))
    
    def test_one_char(self):    
        my_string = 'a'
        output = 'a'

        self.assertEqual(output, first_non_repeating_char(my_string))

    def test_dupli_num(self):    
        my_string = '5221'
        output = '5'

        self.assertEqual(output, first_non_repeating_char(my_string))

    def test_dupli_space(self):    
        my_string = ' bleh'
        output = ' '

        self.assertEqual(output, first_non_repeating_char(my_string))
    
    def test_dupli_special_char(self):    
        my_string = '$hello'
        output = '$'

        self.assertEqual(output, first_non_repeating_char(my_string))
    
    def test_all_dupli(self):    
        my_string = 'aabbcc'
        output = None

        self.assertEqual(output, first_non_repeating_char(my_string))

# Group Anagrams
class Test_Group_Anagrams(unittest.TestCase):    
    def test_empty(self):    
        my_list1 = []
        output =[]

        self.assertEqual(output, group_anagrams(my_list1))

    def test_no_anagram(self):    
        my_list1 = ["apple", "orange"]
        output = [['apple'], ['orange']]

        self.assertEqual(output, group_anagrams(my_list1))
    
    def test_one(self):    
        my_list1 = ["tan", "nat", "bat"]
        output = [['tan', 'nat'], ['bat']]

        self.assertEqual(output, group_anagrams(my_list1))

    def test_multi(self):    
        my_list1 = ["listen", "silent", "triangle", "integral", "garden", "ranged"]
        output = [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

        self.assertEqual(output, group_anagrams(my_list1))

# Two Sum
class Test_Two_Sum(unittest.TestCase):    
    def test_empty(self):    
        my_list1 = []
        target = 1
        output =[]

        self.assertEqual(output, two_sum(my_list1, target))

    def test_no_solution(self):    
        my_list1 = [1, 2]
        target = 1
        output =[]

        self.assertEqual(output, two_sum(my_list1, target))
    
    def test_dupli(self):    
        my_list1 = [1, 1, 2, 2]
        target = 3
        output = [1, 2]

        self.assertEqual(output, two_sum(my_list1, target))

    def test_one_num(self):    
        my_list1 = [1]
        target = 1
        output =[]

        self.assertEqual(output, two_sum(my_list1, target))

    def test_one_solution(self):    
        my_list1 = [1, 2, 3, 5]
        target = 7
        output =[1, 3]

        self.assertEqual(output, two_sum(my_list1, target))

# Subarray Sum
class Test_Subarray_Sum(unittest.TestCase):    
    def test_empty(self):    
        my_list1 = []
        target = 0
        output =[]

        self.assertEqual(output, subarray_sum(my_list1, target))

    def test_no_solution(self):    
        my_list1 = [1, 2, 4, 5]
        target = 20
        output =[]

        self.assertEqual(output, subarray_sum(my_list1, target))
    
    def test_multi_solution(self):    
        my_list1 = [1, 2, 3, 4, 1]
        target = 10
        output = [0, 3]

        self.assertEqual(output, subarray_sum(my_list1, target))

    def test_neg_num(self):    
        my_list1 = [-1, 2, 3, -4, 5]
        target = 0
        output = [0, 3]

        self.assertEqual(output, subarray_sum(my_list1, target))

    def test_one_item(self):    
        my_list1 = [1, 2, 3, 5]
        target = 1
        output =[0, 0]

        self.assertEqual(output, subarray_sum(my_list1, target))
    
    def test_at_start(self):    
        my_list1 = [1, 2, 3, 5, 6, 9]
        target = 6
        output =[0, 2]

        self.assertEqual(output, subarray_sum(my_list1, target))
    
    def test_at_end(self):    
        my_list1 = [1, 2, 3, 5, 6, 9]
        target = 15
        output =[4, 5]

        self.assertEqual(output, subarray_sum(my_list1, target))

# Remove Duplicates
class Test_Remove_Duplicates(unittest.TestCase):    
    def test_empty(self):    
        my_list1 = []
        output =[]

        self.assertEqual(output, remove_duplicates(my_list1))

    def test_one_item(self):    
        my_list1 = [1]
        output =[1]

        self.assertEqual(output, remove_duplicates(my_list1))
    
    def test_multi(self):    
        my_list1 = [1, 2, 1, 2, 3]
        output =[1, 2, 3]

        self.assertEqual(output, remove_duplicates(my_list1))

    def test_no_duplicates(self):    
        my_list1 = [1, 2]
        output = [1, 2]

        self.assertEqual(output, remove_duplicates(my_list1))
    
    def test_all_dupli(self):    
        my_list1 = [2, 2, 2]
        output =[2]

        self.assertEqual(output, remove_duplicates(my_list1))

# Has Unique Chars
class Test_Has_Unique_Chars(unittest.TestCase):    
    def test_empty(self):    
        my_string = ''

        self.assertTrue(has_unique_chars(my_string))

    def test_all_uni(self):    
        my_string = 'abcdefg'

        self.assertTrue(has_unique_chars(my_string))
    
    def test_mixed_non_unique(self):    
        my_string = 'hello'

        self.assertFalse(has_unique_chars(my_string))

    def test_nums(self):    
        my_string = '1234'

        self.assertTrue(has_unique_chars(my_string))

    def test_nums_non_uniq(self):    
        my_string = '1123'

        self.assertFalse(has_unique_chars(my_string))
    
    def test_dupli_special_char(self):    
        my_string = '@#!@'

        self.assertFalse(has_unique_chars(my_string))
    
    def test_non_dupli_special_char(self):    
        my_string = '#!@'

        self.assertTrue(has_unique_chars(my_string))

# Find Pairs
class Test_Find_Pairs(unittest.TestCase):    
    def test_emptys(self):    
        my_list1 = []
        my_list2 = []
        target = 1
        output =[]

        self.assertEqual(output, find_pairs(my_list1, my_list2, target))
    
    def test_one_empty(self):    
        my_list1 = [1]
        my_list2 = []
        target = 1
        output =[]

        self.assertEqual(output, find_pairs(my_list1, my_list2, target))
    
    def test_other_empty(self):    
        my_list1 = []
        my_list2 = [1]
        target = 1
        output =[]

        self.assertEqual(output, find_pairs(my_list1, my_list2, target))

    def test_no_solution(self):    
        my_list1 = [1, 2]
        my_list2 = [1]
        target = 4
        output =[]

        self.assertEqual(output, find_pairs(my_list1, my_list2, target))
    
    def test_multi(self):    
        my_list1 = [1, 2, 3, 5]
        my_list2 = [1, 3, 4, 5]
        target = 6
        output = [(5, 1), (3, 3), (2, 4), (1, 5)]

        self.assertEqual(output, find_pairs(my_list1, my_list2, target))

    def test_neg_num(self):    
        my_list1 = [1, 2, 3, 5]
        my_list2 = [-1, 3, 4, 5]
        target = 0
        output = [(1, -1)]

        self.assertEqual(output, find_pairs(my_list1, my_list2, target))

    def test_one_solution(self):    
        my_list1 = [1, 2, 3, 5]
        my_list2 = [-1, 3, 4, 5]
        target = 10
        output = [(5, 5)]

        self.assertEqual(output, find_pairs(my_list1, my_list2, target))
    
    def test_zero(self):    
        my_list1 = [1, 2, 3, 5]
        my_list2 = [1, -3, 4, 5]
        target = 0
        output = [(3, -3)]

        self.assertEqual(output, find_pairs(my_list1, my_list2, target))

# Longest Consecutive Sequence 
class Test_Longest_Consecutive_Sequence (unittest.TestCase):    
    def test_empty(self):    
        my_list1 = []
        output = 0

        self.assertEqual(output, longest_consecutive_sequence(my_list1))

    def test_one_item(self):    
        my_list1 = [1]
        output = 1

        self.assertEqual(output, longest_consecutive_sequence(my_list1))
    
    def test_consec_items(self):    
        my_list1 = [1, 2, 3]
        output = 3

        self.assertEqual(output, longest_consecutive_sequence(my_list1))

    def test_with_gaps(self):    
        my_list1 = [1, 2, 3, 6, 7]
        output = 3

        self.assertEqual(output, longest_consecutive_sequence(my_list1))

    def test_second_seq(self):    
        my_list1 = [1, 2, 4, 5, 6, 7]
        output = 4

        self.assertEqual(output, longest_consecutive_sequence(my_list1))
    
    def test_all_dupli(self):    
        my_list1 = [2, 2, 2]
        output = 1

        self.assertEqual(output, longest_consecutive_sequence(my_list1))
    
    def test_unordered(self):    
        my_list1 = [4, 2, 3, 1]
        output = 4

        self.assertEqual(output, longest_consecutive_sequence(my_list1))

    def test_neg_nums(self):    
        my_list1 = [-2, -1, 0]
        output = 3

        self.assertEqual(output, longest_consecutive_sequence(my_list1))

    def test_no_seq(self):    
        my_list1 = [1, 3, 5, 7]
        output = 1

        self.assertEqual(output, longest_consecutive_sequence(my_list1))


if __name__ == '__main__':
    unittest.main()     