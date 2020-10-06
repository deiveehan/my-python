x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + a
print(x(5,33, 54))


# Complex lamda
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
