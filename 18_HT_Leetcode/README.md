# Hash Table: Interview/LeetCode Exercise

## Item In Common

The objective is to take two lists as input and return `True` if there is at least one common item between the two lists, `False` otherwise.

### Code Implementation

```
def item_in_common(list1, list2): 
    my_dict = {}
    for i in list1:
        my_dict[i] = True
        
    for j in list2: 
        if j in my_dict: 
            return True
    
    return False
```

### Explanation

- Store the items from `list1` in the dictionary (`my_dict`).
- Loop through list2.
  - If the item from `list2` is found in the dictionary `my_dict` that means that it is in both of the list.
    - Return `True`. 
- Return `False`.

---

## Find Duplicates

Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).

### Code Implementation

```
def find_duplicates(nums):
    duplicates = []
    my_dict = {}
    
    for i in nums: 
        if i in my_dict and i not in duplicates:
            duplicates.append(i)
        else:
            my_dict[i] = True
            
    return duplicates
```

### Explanation

- Initialize an array, `duplicates` and a dictionary, `my_dict`. 
- Iterate through the array of numbers (`nums`)
  - If the number is in the dictionary but not in the duplicates list.  
    - Add the number to the array of duplicates. 
  - Otherwise, add the number to the dictionary. 
- Return the list of duplicates. 

---

## First Non-Repeating Character

The objective is find the first non-repeating character in the given string using a hash table (_dictionary_). If there is no non-repeating character in the string, the function should return `None`.

### Code Implementation

```
def first_non_repeating_char(string):
    my_dict = {}
    
    for char in string:
        my_dict[char] = my_dict.get(char, 0) + 1
    
    for char in string:
        if my_dict[char] == 1:
            return char
    return None
```

### Explanation

- Initialize a dictionary, `my_dict`.
- Iterate through each character of the string. 
    - Use the `get` method to get the character count. If the character is not in the hash table, its count is initialized to 0. The count is then incremented by 1 for each occurrence.
- The second loops through each character of the string.
  - If the count is `1`, return the character.
- Return None if no non-repeating character is in the string.

---

## Group Anagrams

The objective is to group the anagrams in the array together using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams.

> **An example:**
>
> Strings: `["eat", "tea", "tan", "ate", "nat", "bat"]` -> `[["eat","tea","ate"],["tan","nat"],["bat"]]`

### Code Implementation

```
def group_anagrams(strings):
    anagram_groups = {}
    
    for word in strings:
        canonical = ''.join(sorted(word))
        if canonical in anagram_groups:
            anagram_groups[canonical].append(word)
        else:
            anagram_groups[canonical] = [word]
            
    return list(anagram_groups.values())
```

### Explanation

- Initialize a dictionary, `anagram_groups` to groups of anagrams.
- Iterate through each word of the array of strings.
    - Sort the characters in each string to get its canonical form. In the context of this code, "canonical" means the standardized or normalized form of a string that can be used to compare it to other strings to see if they are anagrams.
- If the canonical exists in the hash table. 
  - Append it to the existing list of anagrams 
- Otherwise.
  - Add to the hash table as a new group of anagrams.
- Return the list of lists of anagrams.

---

## Two Sum

Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.

> **An example:**
>
> nums = `[5, 1, 7, 2, 9, 3]`, target = `10` -> Output: `[1, 4]`
> nums = `[3, 3]`, target = `6` -> Output: `[0, 1]`

### Code Implementation

```
def two_sum(nums, target):
    num_list = {}
    
    for index, num in enumerate (nums):
        complement = target - num
        if complement in num_list:
            return [num_list[complement], index]
        else:
            num_list[num] = index
            
    return []
```

### Explanation

- Initialize a dictionary, `num_list`.
- Iterate through each number of the array of numbers. Use the `enumerate` function to get the `index` of each number. 
    - Calculate the `complement` by subtracting the **number** to the **target**.
    - If the complement exists in the dictionary. 
      - Return the index of the complement and the current index. 
    - Otherwise. 
      - Add the number to the dictionary with their index. 
- After the loop ends, return `[]`. 

--- 

## Subarray Sum

Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

> **An example:**
>
> List: `[1, 2, 3, 4, 5]`, target = 9 -> `[1, 3]`
> List: `[5, 4, 3, 2, 9]` -> `[9, 5, 4, 3, 2, 1]`

### Code Implementation

```
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
```

### Explanation

- Initialize a dictionary `subarray` with value of `0` and index `-1` and a `sum`. 
- Iterate through each number of the array of numbers. Use the `enumerate` function to get the `index` of each number.
  - Calculate the `sum` by adding the **number**.
  - Check if the value `(current_sum - target)` exists as a `key` in the dictionary.
    - Return the indices.
  - Otherwise.
    - Add the sum to the dictionary with the index.
- After the loop ends, return `[]`.

---

## Set: Remove Duplicates

The objective is to remove all the duplicates from the list using a set. The Time Complexity should be `O(n)`.

### Code Implementation

```
def remove_duplicates(my_list):
    updated_list = set()
    for num in my_list:
        if not num in updated_list:
            updated_list.add(num)
            
    return list(updated_list)
```

### Explanation

- Initialize an empty set `updated_list`.
- Iterate through each number of the array of numbers.
  - Check if the num doesn't exist in the set.
    - Add that number to the set.
- After the loop ends, return the list with no duplicates.

---

## Set: Has Unique Chars

The objective is to return `True` if all the characters in the string are unique, and `False` otherwise.

### Code Implementation

```
def has_unique_chars(string):
    unique_chars = set()
    
    for char in string:
        if char in unique_chars:
            return False
        else:
            unique_chars.add(char)
    
    return True
```

### Explanation

- Initialize an empty set `unique_chars`.
- Iterate through each character of the string.
  - Check if the char exists in the set.
    - Return False.
  - Otherwise.
    - Add that character to the set.
- After the loop ends, return True.

---

## Set: Find Pairs

You are given two lists of integers, `arr1` and `arr2`, and a `target` integer value, target. Your task is to find all pairs of numbers (one from `arr1` and one from `arr2`) whose sum equals `target`.

Write a function called `find_pairs` that takes in three arguments: `arr1`, `arr2`, and `target`, and returns a list of all such pairs.  Assume that each array does not contain duplicate values.

The tests for this exercise assume that `arr1` is the list being converted to a set.

> **An example:**
>
> arr1 = `[1, 2, 3]`, arr2 = `[4, 5, 6]`, target = 9 -> `[(3, 6)]`
> arr1 = `[0, 1, 2]`, arr2 = `[7, 8, 9]`, target = 10 -> `[(1, 9), (2, 8)]`

### Code Implementation

```
def find_pairs(arr1, arr2, target):
    array1 = set(arr1)
    pairs_array = []
    
    for num in arr2: 
        if (target - num) in array1:
            pairs_array.append((target - num, num))
    
    return pairs_array
```

### Explanation

- Initialize an empty array `pairs_array` to store the pairs.
- Iterate through each number of the second array (`arr2`).
  - Check if value `(target - num)` exists in the array1 (aka first array).
    - Append that pair to the array.
- After the loop ends, return the `pairs_array`.

---

## Set: Longest Consecutive Sequence

Given an unsorted array of integers, write a function that finds the length of the  `longest_consecutive_sequence` (i.e., sequence of integers in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

### Code Implementation

```
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
```

### Explanation

- Initialize an empty set `set_array`, `long_seq` and `current_seq`.
- Sort the list and remove any duplicates. 
- Iterate through each number of the array.
  - Check if the previous number `(num-1)` exists in the set.
    - Increase the `current_seq` by 1.
  - Check if the previous number `(num-1)` doesn't exist in the set.
    - Adjust the `long_seq` by taking the **max** of long_seq and current_seq.
    - Reset the current_seq to 1. 
  - Add that number to the set.
- Adjust the `long_seq` by taking the **max** of long_seq and current_seq.
- Return `long_seq`.

---
