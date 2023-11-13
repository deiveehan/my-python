class A:
    def say_hello(self):
        return "Hello from A"

class B(A):
    def say_hello(self):
        return "Hello from B"

class C(A):
    def say_hello(self):
        return "Hello from C"

class D(B, C):
    pass

# Using the class D
d = D()
print(d.say_hello())  # Will output: Hello from B

# Printing the Method Resolution Order
print(D.mro())  # Shows the order in which methods are resolved
