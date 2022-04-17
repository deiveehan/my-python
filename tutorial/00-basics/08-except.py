try:
    print(x)
except:
    print("An exception occurred")


# Nested exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


# Finally block
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# Creating custom exceptions
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

# Type error:
x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
