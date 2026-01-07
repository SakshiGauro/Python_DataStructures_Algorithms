import unittest

class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)
    
    def pop(self):
        if self.size() == 0: # empty 
            return None
        return self.stack_list.pop()

def reverse_string(my_string):
    if len(my_string) > 1:
        my_stack = Stack()
        for char in my_string: 
            my_stack.push(char)
            
        new_word = ""
        while (not my_stack.is_empty()):
            new_word += my_stack.pop()
        
        return new_word
    return my_string

def is_balanced_parentheses(my_string):
    my_stack = Stack()
    
    for char in my_string:
        if char == '(':
            my_stack.push(char)
        else:
            if my_stack.is_empty(): 
                return False
            my_stack.pop()
    
    if my_stack.is_empty():
        return True
    return False

def sort_stack (my_stack):
    storted_stack = Stack()
    
    while(not my_stack.is_empty()):
        temp = my_stack.pop()
        while (not storted_stack.is_empty() and storted_stack.peek() > temp):
            my_stack.push(storted_stack.pop())
        
        storted_stack.push(temp)
    
    while(not storted_stack.is_empty()):
        my_stack.push(storted_stack.pop())

#  +=====================================================+
#  |                                                     |
#  |        THE TEST CODE BELOW ARE TEST CASES           |
#  |                                                     |
#  +=====================================================+


# Constructor
class Test_Constructor(unittest.TestCase):    
    def test_stack_init(self):    
        stack = Stack()

        self.assertIsNotNone(stack)
    
    def test_empty_stack(self):    
        stack = Stack()

        self.assertEqual(stack.stack_list, [])
    
    def test_size(self):    
        stack = Stack()

        self.assertEqual(len(stack.stack_list), 0)

# Push
class Test_Push(unittest.TestCase): 
    def test_empty_stack(self):    
        stack = Stack()
        stack.push(5)

        self.assertEqual(stack.stack_list, [5])
    
    def test_multiple(self):    
        stack = Stack()
        stack.push(5)
        stack.push(7)

        self.assertEqual(stack.stack_list, [5, 7])

# Pop
class Test_Pop(unittest.TestCase): 
    def test_empty_stack(self):    
        stack = Stack()
        result = stack.pop()

        self.assertIsNone(result)

    def test_single_item(self):    
        stack = Stack()
        stack.push(5)
        result = stack.pop()

        self.assertEqual(result, 5)
    
    def test_multi_item(self):    
        stack = Stack()
        stack.push(5)
        stack.push(4)
        stack.push(3)

        result = stack.pop()
        result = stack.pop()

        self.assertEqual(result, 4)

    def test_pop_until_empty(self):    
        stack = Stack()
        stack.push(5)
        stack.push(4)

        stack.pop()
        stack.pop()

        self.assertEqual(stack.stack_list, [])

# Reverse String
class Test_Reverse_String(unittest.TestCase): 
    def test_empty(self):    
        word = ''

        self.assertEqual(reverse_string(word), word)

    def test_single_char(self):    
        word = 'a'

        self.assertEqual(reverse_string(word), word)
    
    def test_long_string(self):    
        word = 'hello'

        self.assertEqual(reverse_string(word), 'olleh')

    def test_nums_chars(self):    
        word = '54hello@93!'

        self.assertEqual(reverse_string(word), '!39@olleh45')

    def test_palindrome(self):    
        word = 'racecar'

        self.assertEqual(reverse_string(word), word)
    
    def test_two_char(self):    
        word = 'ra'

        self.assertEqual(reverse_string(word), 'ar')

# Parentheses Balanced
class Test_Parentheses_Balanced(unittest.TestCase): 
    def test_empty(self):    
        word = ''

        self.assertTrue(is_balanced_parentheses(word))

    def test_unbalanced(self):    
        word = ')('

        self.assertFalse(is_balanced_parentheses(word))
    
    def test_balanced(self):    
        word = '()'

        self.assertTrue(is_balanced_parentheses(word))

    def test_large_balanced(self):    
        word = '((()))()(())'

        self.assertTrue(is_balanced_parentheses(word))

    def test_large_unbalanced(self):    
        word = '((())))(())'

        self.assertFalse(is_balanced_parentheses(word))
    
    def test_large_balanced_nested(self):    
        word = '(((())))'

        self.assertTrue(is_balanced_parentheses(word))
    
    def test_large_single_closed(self):    
        word = '(((()'

        self.assertFalse(is_balanced_parentheses(word))

    def test_large_single_open(self):    
        word = '())'

        self.assertFalse(is_balanced_parentheses(word))

# Sort Stack
class Test_Sort_Stack(unittest.TestCase): 
    def test_empty_stack(self):    
        stack = Stack()
        sort_stack(stack)

        self.assertEqual(stack.stack_list, [])
    
    def test_multiple(self):    
        stack = Stack()
        stack.push(5)
        stack.push(1)
        stack.push(3)
        stack.push(7)

        sort_stack(stack)

        self.assertEqual(stack.stack_list, [7, 5, 3, 1])

    def test_already_sorted(self):    
        stack = Stack()
        stack.push(5)
        stack.push(4)
        stack.push(3)
        stack.push(2)
        stack.push(1)

        sort_stack(stack)

        self.assertEqual(stack.stack_list, [5, 4, 3, 2, 1])
    
    def test_reverse_sorted(self):    
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)

        sort_stack(stack)

        self.assertEqual(stack.stack_list, [5, 4, 3, 2, 1])

    def test_reverse_single_element(self):    
        stack = Stack()
        stack.push(1)

        sort_stack(stack)

        self.assertEqual(stack.stack_list, [1])

    def test_duplicates(self):    
        stack = Stack()
        stack.push(1)
        stack.push(5)
        stack.push(1)
        stack.push(3)
        stack.push(2)

        sort_stack(stack)

        self.assertEqual(stack.stack_list, [5, 3, 2, 1, 1])


if __name__ == '__main__':
    unittest.main()