# This is a single line comment use for documentation.


'''
This is a multiline comment
You can see me write text in a new line.
This is use for documentation.
'''

# Variables and Data-types
bootle = "water"

#data types
"QWERTYUIPOF12345768990!@#$55666)(&%)_)*/.mm" # String

1235435 # Integers

12342.45647 # Floats

True 
False # Boolean

first_name = "Miracle" # Snake case

world = "Hello World"
# print(world)

# Arithmetic Operator
'''
+ Addition (Datatypes - Integers, Floats, Strings)
- Subtraction (Datatypes - Integers, Floats)
* Multiplication (Datatypes - Integers, Floats, Strings)
/ Division (Datatypes - Integers, Floats)
// Floor Division (For rounding down values) (Datatypes - Integers, Floats)
'''

concatenation = "Miracle" + "King" # Concatenation
repitition = "Hurray" * 3 # Repitition

first_number = 4
second_number = 6

# Addition
add = first_number + second_number
print("Addition:", add, "Type:", type(add))

# Subtraction
subtract = first_number - second_number
print("Subtraction:", subtract, "Type:", type(subtract))

# Multiplication
multiply = first_number * second_number
print("Multiplication:", multiply, "Type:", type(multiply))

# Division
divide = first_number / second_number
print("Division:", divide, "Type:", type(divide))

# Casting - Changing one data type to another data type
'''
int() - to convert to integer (string, float) - provided the fact that the characters are numbers
str() - ... string (integer, boolean, float)
float() - ... float (integer, string) - provided the fact that the characters are numbers
bool() - ... boolean (string)
'''

# Converting divide to an integer
convert_to_int = int(divide)
print("Converting divide to integer:",convert_to_int, type(convert_to_int))

# Converting add to string
convert_to_str = str(add)
print("Converting add to string:",convert_to_str, type(convert_to_str))

# Re-assigning a variable
nationality = "United States of America"
nationality = "Nigeria"
nationality = "France"
print(nationality)

introduction = "My name is" + " " + first_name + " " + "and i am from" + " "+  nationality
print(introduction)










