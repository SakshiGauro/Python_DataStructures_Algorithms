# Hash Table

A Hash Table is a data structure designed to be fast to work with. 

You use hash tables in Python every time you use a dictionary. Dictionaries store data as `key:value` pairs and use a **hash function** to map the immutable keys to a specific index (or "bucket") in memory. This allows for highly efficient data retrieval, insertion, and deletion operations with an average time complexity of `O(1)` **(constant time)**.

### Core Characteristics
- **Key-Value Storage:** Hash tables store data as unique key-value pairs.
- **Use of a Hash Function:** A mathematical algorithm, the hash function, takes an input key and converts it into a fixed-size index (or **"hash code"**).
- **One-way:** The hash function's property that it's computationally difficult to reverse the output hash back to its original input key.
- **Deterministic:** Always produces the same output (hash value) for the same input (key).

### Big 0:

| Methods         | Time Complexity (Avg) | Time Complexity (Worse) |
|-----------------| ----------- |------------------------|
| **Hash method** | O(1) | O(1)                   | 
| **Set method**  | O(1) | O(n)                   |
| **Get method**  | O(1) | O(n)                   |

### HT Collisions

A **collision** happens when two Hash Table elements have the same hash code, because that means they belong to the same **bucket**.

#### Collision Resolutions:
- **Separate chaining:** A collision resolution technique where each bucket in the hash table's array holds a **linked list** to store multiple key-value pairs that hash to the same index, effectively creating "chains" of items. 
- **Open Addressing:** All elements are stored in the hash table itself. Each table entry contains either a record. When searching for an element, we examine the table slots one by one until the desired element is found, or it is clear that the element is not in the table.
  - Linear Probing: In linear probing, the hash table is searched sequentially that starts from the original location of the hash. If in case the location that we get is already occupied, then we check for the next location.
  
---

## Constructor
This section introduces the **constructor** for a hash table. The goal is to initialize a hash table with a data map.

number/address upto 6, prime numbers increases the randomness of the key value paris. So removing them, reduces collisons 

### Requirements

**HashTable Class**
- A constructor that accepts a `size` with default size to 7
- Create a list named data_map of length size, initialized with None values

### Code Implementation
```
class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  
```

### Explanation

**__hash Method**
- `def __hash(self, key):`: Function Definition that takes in a string key. 
- `my_hash = 0`: Store the hash index. 
- `for letter in key:`: Iterate through each character of the hash key. 
- `my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)`: 
  - `ord(letter)` -> ordinal number, ascii number of each letter
  - `* 23`: Multiply with 23, a prime number to reduce the occurrence of collisons.
  - `% len(self.data_map)`: Modulus divison so that the number is between 0 to map size.

**HashTable Class**
- `class HashTable:`: Defines the **HashTable** class, which manages the table.
- `def __init__(self, size = 7):`: Constructor for the `HashTable` class called when you create a new instance. The default size is 7.
- `self.data_map = [None] * size`: Creates a data map with the size.

---

## Set
The `set` method inserts a key-value pair into the hash table.

### Code Implementation
```
def set_item(self, key, value):
    index = self.__hash(key)
    if (self.data_map[index] is None):
        self.data_map[index] = []
    self.data_map[index].append([key, value])
```

### Explanation
- `index = self.__hash(key)` → Get the index using the hash key function.
- `if (self.data_map[index] is None):` → Check if the table is empty.
    - If the HT is empty, replace None with an empty list.
- `self.data_map[index].append([key, value])` → Update the table.

---

## Get
The `get` method for the HashTable class that retrieves the value associated with a given key from the hash table.

### Code Implementation
```
def get_item(self, key):
    index = self.__hash(key)
    if (self.data_map[index] is not None): 
        for i in range(len(self.data_map[index])):
            if self.data_map[index][i][0] == key:
                return self.data_map[index][i][1]
    return None
```

### Explanation
- `index = self.__hash(key)` → Get the index using the hash key function.
- `if (self.data_map[index] is not None):` → Check if the index is not empty.
    - `for i in range(len(self.data_map[index])):`: If the HT has items, iterate through each item (`[key, value]`) in that list 
      - `if self.data_map[index][i][0] == key:`: → If the key matches.
        - `return self.data_map[index][i][1]`: Return the value.
- Return `None` if keys do not match. 

---

## Keys
The `keys` method for the HashTable class that returns a list of all the keys present in the hash table.

### Code Implementation
```
def keys(self):
    all_keys = []
    for i in range(len(self.data_map)):
        if self.data_map[i] is not None:
            for j in range(len(self.data_map[i])):
                all_keys.append(self.data_map[i][j][0])
                
    return all_keys
```

### Explanation
- `all_keys = []` → Store the keys. 
- `for i in range(len(self.data_map)):`: Iterate through the indexes in that table.
  - `if (self.data_map[index] is not None):` → Check if the index has values.
      - `for j in range(len(self.data_map[i])):`: Iterate through  each item (`[key, value]`) in that index.
        - `all_keys.append(self.data_map[i][j][0])`: → Append the key in the `all_keys`
- Return `all_keys`.

---

## Interview Question: Duplicates in a list
See if two lists has same item.

### Approach 1: Nested Loop
```
def item_in_common_nested(list1, list2):
    for i in list1:
        for j in list2: 
            if i == j:
                return True
    return False
```

#### Explanation
- Nested loop to compare each item from `list1` to `list2`. 
- Time Complexity of `O(n^2)`.

### Approach 2: Using Dictionary
```
def item_in_common_dict(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    
    for j in list2:
        if j in my_dict:
            return True
    return False
```

### Explanation
- Store items from `list1` in a dictionary. 
- Iterate through `list2`.
  - Check if the item from `list2` is in the **dictionary**.
- Otherwise, return `False`. 
- Time Complexity of `O(2n)` = `O(n)` because we iterate through the list two separate times. 

---






