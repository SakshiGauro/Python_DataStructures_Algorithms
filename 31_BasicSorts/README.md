# Basic Sorts
Sorting is defined as an arrangement of data in a certain order like sorting numbers in increasing order or decreasing order, sorting students by marks and sorting names alphabetically. 

## Bubble Sort
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.

The algorithm iterates through the array multiple times, with each pass pushing the largest unsorted element to its correct position at the end.

### Code Implementation
```
def bubble_sort (my_list): 
    for i in range(len(my_list), 1, -1):
        for j in range(i - 1):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
                
    return my_list
```

#### Explanation
- The outer loop of the code runs from `len(my_list) - 1` to `1` **(inclusive)** using the range function, with a step size of `-1`. This outer loop will make n-1 passes through the list where n is the length of the list. By starting from the end of the list, this loop ensures that each iteration finds the maximum element and moves it to the end of the unsorted part of the list.
  - The inner loop runs over each pair of **adjacent elements** in the unsorted part of the list. It starts at index `0` and runs up to `i - 1`, where i is the current index of the outer loop. 
    - This loop checks whether the element at index `j` is greater than the element at index `j + 1`. 
    - If it is, 
      - then it swaps the elements, which moves the larger element to the right. 
  - After this loop completes, the largest element in the unsorted part of the list is moved to the end.
- After the outer and inner loops have run, the sorted list is returned.

---

## Selection Sort
Selection Sort is a comparison-based sorting algorithm. It sorts an array by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element. This process continues until the entire array is sorted.
- First we find the smallest element and swap it with the first element. This way we get the smallest element at its correct position.
- Then we find the smallest among remaining elements (or second smallest) and swap it with the second element.
- We keep doing this until we get all elements moved to correct position.

### Code Implementation
```
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
```

#### Explanation
- The outer loop of the code runs from `0` to `len(my_list)` using the `range` function. This outer loop will make `n` passes through the list where `n` is the length of the list. Each pass will ensure that the smallest element in the remaining unsorted part of the list is moved to the **beginning**.
  - The variable `min_index` keeps track of the index of the **smallest** element in the unsorted part of the list. It starts at the current index `i` of the outer loop.
  - The inner loop runs over each element of the unsorted part of the list, starting from `i+1` and running up to the **end of the list**. 
    - It compares each element to the current minimum element. 
      - Update `min_index` if it finds a smaller element.
  - If the `min_index` is not `i`, 
    - Swap the elements at indices `i` and `min_index` using a temporary variable called `temp`. This moves the smallest element to the beginning of the unsorted part of the list.
- After the outer and inner loops have run, the sorted list is returned.

---

## Insertion Sort 
Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list.
- The insertionSort function takes an array arr as input. It first calculates the length of the array (n). If the length is 0 or 1, the function returns immediately as an array with 0 or 1 element is considered already sorted.
- For arrays with more than one element, We start with second element of the array as first element in the array is assumed to be sorted.
- Compare second element with the first element and check if the second element is smaller than, swap them.
- Move to the third element and compare it with the first two elements and put at its correct position. 
- Repeat until the entire array is sorted.

### Code Implementation
```
def insertion_sort(my_list): 
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i-1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
            
    return my_list
```

#### Explanation
- The outer loop of the code runs from `1` to `len(my_list)` using the `range` function. This outer loop will iterate over each element of the list starting from the second element.
  - The variable temp is used to store the current element being sorted.
  - The variable `j` is used to iterate over the already sorted part of the list, starting from the index before the current element `i`.
  - The while loop checks if the current element is less than the previous element and the previous element is greater than or equal to zero (i.e., the index is still in the bounds of the list). 
  - If both conditions are true
    - It swaps the current element with the previous element
    - Decrements j by 1.
  - Once the while loop completes, the current element has been inserted into its correct position in the already sorted part of the list.
  - The outer loop continues this process until all elements have been sorted and inserted into their correct positions.
- After the outer and inner loops have run, the sorted list is returned.

---

## Big O

| Sorts           | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
|-----------------|------------------------|---------------------------|-------------------------|------------------|
| Bubble Sort     | `O(n)`                 | `O(n^2)`                  | `O(n^2)`                | `O(1)`           |
| Selection Sort  | `O(n^2)`               | `O(n^2)`                  | `O(n^2)`                | `O(1)`           |
| Insertion Sort  | `O(n)`                 | `O(n^2)`                  | `O(n^2)`                | `O(1)`           |

---

_source: https://www.geeksforgeeks.org/python/sorting-algorithms-in-python/_

---
