from my_module import my_addition_function
from functools import reduce
# from functools
# Higher Order Functions
# Higher Order functions are functions that take a function as an argument, or return a function.


# Example
def speak():
    return "Ola. Nice to meet you."

def man(name, func):
    return f"{name}: {func()}"

call = man("Jerry", speak)
# print(call)

# Map, Filter, Reduce

# Map a higher order function that returns back a new list.
numbers = [1,2,3,4,5,6,7,8,9]

def multiply_by_2(item):
    return item * 2

map_func = map(multiply_by_2, numbers)
# print(list(map_func))


# Filter: Returns a new filtered list
# def no_remainder(item):
#     print(item)
#     return item % 2 == 0 # Modulos - returns remainders when you divide

# filter_func = filter(no_remainder, numbers)

filter_func = filter(lambda item: item % 2 == 0 , numbers)
# print(list(filter_func))


# Reduce: Returns a reduced value of the iterable
sentence = ["A", "stitch", "in", "time", "saves", "nine"]

def concatenate(param_one, param_two):
    return param_one + " " + param_two

reduce_func = reduce(concatenate, sentence)
# print(reduce_func)

func = lambda: "This is a function"
func_with_parameters = lambda a, b, c, d: a + b + c + d
# print(func_with_parameters(1,2,3,4))


# Function nesting.
def outer_function():
    def inner_function():
        return "I'm coming from the inner function"
    return inner_function()


# List Comprehesion
new_list = [item + 2 for item in numbers if item % 2 == 0] # Any number that does not return a number, add 2 to it.
print(new_list)


def funcA(func):
    # Runn operation first
    func
    # Run another operation

@funcA
def funcB():
    return True