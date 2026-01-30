# Recursion     

Recursive functions are functions that **calls itself**. It is always made up of 2 portions, **the base case** and **the recursive case**.

- The **base** case is the condition to stop the recursion.
- The **recursive** case is the part where the function calls on itself.

If there are no base cases, the function keeps calling itself, hence, stack overflow. To ensure this does not happen: 

- Check if the `if` statement is reachable i.e. function reaches base case. 
- A return statement exists to break out of the recursion. 

### Call Stack
In the following example, we'll see how the call stacks work. 

```
def functionThree():
    print("Three") # prints first

def functionTwo():
    functionThree()
    print("Two")   # prints second

def functionOne():
    functionTwo()
    print("One")  # prints last

functionOne()
```

**Explanation:**  
- When we call the functionOne, the program calls functionTwo() which calls functionThree. 
- After the functionThree done executing (printing "Three"), the program goes back to functionTwo. It then prints "Two", followed by "One" in functionOne. 

**Output**
```
Three
Two
One
```
---

### Factorial 
In the following example, we'll see how the recursions work.

```
def factorial(num):
    if num == 1: # base
        return 1
    return num * factorial(num-1)
    
print(factorial(4)) # prints 24
```

**Explanation:**
- `4!` = `4 * 3!` = `4 * 3 * 2!` = `4 * 3 * 2 * 1!` = `4 * 3 * 2 * 1`. 
- Since the factorial of 1 is 1. That is our base case. 
- Our recursive case, the number decreases by 1 each time the recursion function is called. 

---




