hasLaptop = True
roleCode = 6

if (not(hasLaptop) and roleCode > 4):
    print("The employee must be provided a laptop")
    print("The employee is of a higher role")
else:
    print("The employee already has a laptop or has a role code lesser than manager")

print("Get back to business")


#Elif
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


#Thisis valid
a = 2
b = 330
print("A") if a > b else print("B")


# And condition

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or condition
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# Nested if
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# Pass stmt
a = 33
b = 200

if b > a:
    pass
