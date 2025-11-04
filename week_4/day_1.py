# Functions 

def header():
    # Block of code
    return # the value you want to return


def addition():
    num_1 = 1
    num_2 = 2
    sum = num_1 + num_2
    return sum

output = addition() # calling a function. This will return 3.


# print(output)


def subtraction():
    return 2 - 1

output = subtraction()
# print(output)


'''
What can a function return?
string
boolean
integer
float
list
tuple
dictionary
set
function
variable
'''

def introduction():
    return "Hi my name is Miracle"

# print(
#     introduction()
# )

age =  12 # Global variable

def func():
    name = "King" # Local variable
    return "His is name is " + name + " and he is " + str(age)

# print(
#     func()
# )


# Parameters and Arguements
def func_1(words): # parameter
    return words

# print(
#     func_1("This is an argument") # arguement
# )


def reusable_addition(num_one, num_two):
    return num_one + num_two

output_one = reusable_addition(14, 2)
output_two = reusable_addition(4, 4)
output_three = reusable_addition(16, 18)

# print(output_one, output_two, output_three)


# Types of arguement

def func_2(pos1, pos2, pos3):
    return pos1, pos2, pos3

func_2("first value", "second value", "third value") # Positional Arguement

func_2(pos1="First", pos2="Second", pos3="Third") # Keyword arguement

# Default Arguement
def game(mode="easy"):
    return f"Game on!!! mode {mode}"

# print(
#     game()
# )

# print(
#     game("hard")
# )


# ARGS - Variable length arguement
def func_4(*param):
    return param # the structure is a tuple

print(
    func_4("red", "blue", "yellow", "green")
)

# KWARGS - Keyword as an argument
def func_5(**param):
    return param # A dictionary is returned

print(
    func_5(
        name="Miracle",
        email="miracle@mail.com",
        availability=True,
        ratings=8.0
    )
)