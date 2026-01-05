import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self, value=None):
        if value is None:
            self.top = None
            self.height = 0
        else:
            new_node = Node(value)
            self.top = new_node
            self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0: # empty
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp

    def to_stack(self):
        values = []
        current = self.top
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
    def test_stack_init(self):    
        stack = Stack(7)

        self.assertIsNotNone(stack)

    def test_head(self):    
        stack = Stack(7)

        self.assertEqual(stack.top.value, 7)

    def test_height(self):    
        stack = Stack(7)

        self.assertEqual(stack.height, 1)

    def test_node_next(self):    
        stack = Stack(7)

        self.assertIsNone(stack.top.next)

    def test_value(self):    
        stack = Stack(7)

        self.assertEqual(stack.top.value, 7)

# Push
class Test_Push(unittest.TestCase): 
    def test_non_empty_stack(self):    
        stack = Stack(7)
        stack.push(5)

        self.assertEqual(stack.to_stack(), [5, 7])
    
    def test_multi_values(self):    
        stack = Stack(7)
        stack.push(5)
        stack.push(4)
        stack.push(3)
        stack.push(2)
        stack.push(1)

        self.assertEqual(stack.to_stack(), [1, 2, 3, 4, 5, 7])
    
    def test_top_change(self):    
        stack = Stack(7)
        stack.push(5)

        self.assertEqual(stack.top.value, 5)
    
    def test_height_change(self):    
        stack = Stack(7)
        stack.push(5)

        self.assertEqual(stack.height, 2)

    def test_empty_stack(self):    
        stack = Stack()
        stack.push(5)

        self.assertEqual(stack.to_stack(), [5])

# Pop
class Test_Pop(unittest.TestCase): 
    def test_empty_stack(self):    
        stack = Stack()
        result = stack.pop()

        self.assertIsNone(result)

    def test_top_change(self):    
        stack = Stack(7)
        stack.push(5)

        stack.pop()

        self.assertEqual(stack.top.value, 7)

    def test_height_change(self):    
        stack = Stack(7)
        stack.push(5)
        stack.push(3)

        stack.pop()

        self.assertEqual(stack.height, 2)

    def test_single_item(self):    
        stack = Stack(7)
        result = stack.pop()

        self.assertEqual(result.value, 7)

    def test_pop_until_empty(self):    
        stack = Stack(7)
        stack.push(5)
        stack.push(4)

        stack.pop()
        stack.pop()
        stack.pop()

        self.assertEqual(stack.to_stack(), [])


if __name__ == '__main__':
    unittest.main()
