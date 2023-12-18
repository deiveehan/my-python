cars = ["Ford", "Volvo", "BMW"]
print(cars)

x = cars[0]
print(x)

cars[0] = "Toyota"
print(cars)

lengthofcars = len(cars)
print(lengthofcars)

for car in cars:
    print(car)

cars.append("Honda")
print(cars)

cars.pop(0)
print(cars)

cars.remove("Volvo")
print(cars)
