# Multiply all the elements in a list
def multiply_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] * multiply_list(l[1:])

# Return the factorial of n
def factorial(n):
    if n == 1:
        return n
    else:
        return factorial(n-1) * n

# Count the number of elements in the list l
def count_list(l):
    count = 1
    if len(l) == 1:
        return 1
    else:
        count = count_list(l[1:]) + 1
    return count 

# Sum all of the elements in a list
def sum_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return l[0] + sum_list(l[1:])
 

# Reverse a list without slicing or loops
def reverse(l):
    if len(l) == 1:
        return l
    else:  
        popped = l.pop(0)       
        reverse(l)        
        l.append(popped)               
    return l


# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if l[0] == i:
        return True
    elif len(l) == 1:
        return False
    else:
        return find(l[1:], i)

# Determines if a string is a palindrome
def palindrome(some_string):
    if len(some_string) <= 1:
        return some_string
    elif some_string[0] == some_string[-1]:
        palindrome(some_string[1:-1])
        return True
    return False

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return width, height
    else:
        if width > height:
            return fold_paper(width/2.0, height, folds-1)
        else:
            return fold_paper(width, height/2.0, folds-1)


# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    if n == 0:
        print n
    else:
        count_up(target, n-1)
        print n
