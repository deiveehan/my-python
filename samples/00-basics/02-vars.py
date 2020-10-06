# basic numeric datatypes
a = 10
b = 10.4
print(a+b)

# String datatype
doublevar = "Sam said, \" That's a cool bike \""
singlevar = 'Sam said, "That\'s a great bike "'
print(doublevar)
print(singlevar)

# String functions
firstName = "Deiveehan"
lastName = "Nallazhagappan"
print("First char", firstName[0])
print("Length", len(firstName))
print(firstName.lower())
print(firstName.upper())

# String concatenation
print(firstName + " " + lastName)
print(firstName, "-", lastName)

version = 3
# print("Python version " + version + "!")    #does not work
print("Python version " + str(version) + "!")


x = "Hello World"
print(type(x))
x = 20
print(type(x))

x = 20.5
print(type(x))

x = 1j
print(type(x))

x = ["apple", "banana", "cherry"]
print(type(x))

x = ("apple", "banana", "cherry")
print(type(x))

x = {"name" : "John", "age" : 36}
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(type(x))

x = True
print(type(x))

x = b"Hello"
print(type(x))

x = bytearray(5)
print(type(x))


