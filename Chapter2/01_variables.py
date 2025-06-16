# Variables are containers for storing data values.

# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
x = 5
y = "John"
print(x)
print(y)


# Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# If you want to specify the data type of a variable, this can be done with casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Get the Type
# You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))

# Single or Double Quotes?
# String variables can be declared either by using single or double quotes
x = "ravi"
# is the same as
x = 'ravi'
# ex:-
x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)

# Case-Sensitive
# Variable names are case-sensitive.

a = 4
A = "Sally"

print(a)
print(A)

# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

myvar = "ravi"
my_var = "ravi"
_my_var = "ravi"
myVar = "ravi"
MYVAR = "ravi"
myvar2 = "ravi"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line

x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

# Note: Make sure the number of variables matches the number of values, or else you will get an error.

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line

x = y = z = "Orange"

print(x)
print(y)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

# Python - Output Variables
# Output Variables
# The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)

# In the print() function, you output multiple variables, separated by a comma
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)