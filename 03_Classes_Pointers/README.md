# Classes and Pointers in Python 

Classes allow us to **bundle data (attributes) and behavior (methods)** together. They are a core part of **Object-Oriented Programming (OOP)**.

## Classes
### Coding example: Cookie Class
#### Initializing Class
```
class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
```

**Explanation**
- `class Cookie:` Defines a **class** named `Cookie`.
- `def __init__(self, color):` This is the constructor.
  - It runs automatically when a new object is created.
  - `self` refers to the current object instance.
  - `self.color` = color stores the color as an instance variable.
- `def get_color(self):` Used to retrieve the cookie’s color.
- `def set_color(self, color):` Used to **update** the cookie’s color.

#### Creating Objects (Instances)
```
cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())
```

Each object:
- Has its **own copy** of color
- Is stored at a **different** memory location

Changing `cookie_one` does not affect `cookie_two`.

**Output**
```
Cookie one is green
Cookie two is blue

Cookie one is now yellow
Cookie two is still blue
```

## Pointers & References

Python variables don’t store values directly.
They store **references (pointers)** to objects in memory.

### Coding example: 
#### Integers (Immutable)
```
num1 = 11
num2 = num1
```
Both `num1` and `num2` point to the **same integer object**.

```
print("Before num2 value is updated:")
print("num1 =", num1) // 11
print("num2 =", num2) // 11

print("\nnum1 points to:", id(num1)) // 140720456037480
print("num2 points to:", id(num2)) // 140720456037480

```

**Updating `num2`**
```
num2 = 22 
```
- A **new integer object** is created
- `num2` now points to a new memory location
- `num1` remains unchanged

```
print("\nAfter num2 value is updated:")
print("num1 =", num1) // 11
print("num2 =", num2) // 22

print("\nnum1 points to:", id(num1)) // 140720456037480
print("num2 points to:", id(num2)) // 140720456037832
```

### Dictionaries (Mutable)
```
dict1 = {'value': 11}
dict2 = dict1 
```
Both variables point to the **same dictionary object.**

```
print("\n\nBefore value is updated:")
print("dict1 =", dict1) // {'value': 11}
print("dict2 =", dict2) // {'value': 11}

print("\ndict1 points to:", id(dict1)) // 2306642251584
print("dict2 points to:", id(dict2)) // 2306642251584
```

**Changing `dict2`**
```
dict2['value'] = 22
```
**Now:**
- The dictionary itself is modified
- Both `dict1` and `dict2` reflect the change

```
print("\nAfter value is updated:")
print("dict1 =", dict1) // {'value': 22}
print("dict2 =", dict2) // {'value': 22}

print("\ndict1 points to:", id(dict1)) // 2306642251584
print("dict2 points to:", id(dict2)) // 2306642251584
```

**Key Rule**

Dictionaries are **mutable**. 

You can change their contents without creating a new object.

---

## Immutable vs Mutable Summary

| Type    | Mutable? | Example    |
| ------- | -------- | ---------- |
| `int`   | ❌ No     | `num = 5`  |
| `float` | ❌ No     | `3.14`     |
| `str`   | ❌ No     | `"hello"`  |
| `tuple` | ❌ No     | `(1, 2)`   |
| `list`  | ✅ Yes    | `[1, 2]`   |
| `dict`  | ✅ Yes    | `{'a': 1}` |
| `set`   | ✅ Yes    | `{1, 2}`   |

---

### Garbage Collection

Python automatically manages memory using **garbage collection.**
- When no variables reference an object anymore
- Python frees that memory **automatically**
- You do not manually delete memory like in C/C++

This makes Python safer and easier to use.

---