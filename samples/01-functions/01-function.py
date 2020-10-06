# Function with arguments
def hello(fname, lname):
    print("Hello " + fname + "-" + lname)

hello("Deiveehan", "Nallazhagappan")

# Arbitrary functions
def children(*kids):
    print(kids)

children("Keerthi", "Maanu")

#Default value
def whichCountry(country = "Canada"):
    print(country)

whichCountry("US")
whichCountry("Norway")
whichCountry()

#You can pass a list as an argument to a function
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return
def add(a, b):
    return (a+b)

sum = add(5, 10)
print("Sum of a + b: " + str(sum))


# Recursive function
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
