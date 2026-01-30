def functionThree():
    print("Three") # prints first

def functionTwo():
    functionThree()
    print("Two")   # prints second

def functionOne():
    functionTwo()
    print("One")  # prints last

def factorial(num):
    if num == 1: # base
        return 1
    return num * factorial(num-1)

functionOne()

print(factorial(4))