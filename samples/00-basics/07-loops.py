# For loop
fruits = ["Apple", "Banana", "Strawberry"]

for fruit in fruits:
    print("The fruit is " + fruit)

# Nested for loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# While loop
i=1
while i < 10:
    print(i)
    i += 1

# While with break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Whiel with continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
