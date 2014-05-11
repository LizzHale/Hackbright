# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    new_list = []
    for n in some_list[::-1]:
        if n % 2 != 0:
            #new_list.append(n)
            new_list[0:0] = [n]
        else:
            pass
    return new_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    new_list = []
    for n in some_list[::-1]:
        if n % 2 == 0 and n != 0:
            new_list[0:0] = [n]
        else:
            pass
    return new_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    for n in word_list[::-1]:
        if len(n) >= 4:
            new_list[0:0] = [n]
    return new_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    smallest = some_list[0]
    for each in some_list:
        if each < smallest:
            smallest = each
    return smallest

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    largest = some_list[0]
    for each in some_list:
        if each > largest:
            largest = each
    return largest

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    new_list = []
    for each in some_list[::-1]:
        if each % 2 != 0:
            new_list[0:0] = [each / 2.0]
        else:
            new_list[0:0] = [each / 2]
    return new_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    new_list = []
    for each in word_list[::-1]:
        new_list[0:0] = [len(each)]
    return new_list

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    total = 0
    for each in numbers:
        total += each
    return total

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    total = 1
    for each in numbers:
        total *= each
    return total

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    string = ''
    for each in string_list:
        string += each
    return string

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    total_numbers = len(numbers)
    total = sum_numbers(numbers)
    return total / total_numbers
